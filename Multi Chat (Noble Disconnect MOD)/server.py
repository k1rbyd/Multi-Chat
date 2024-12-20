import socket, select, sys, threading

def send_to_all(sock, message, connected_list, server_socket):
    for socket in connected_list:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                socket.close()
                connected_list.remove(socket)

def shutdown_server(connected_list, server_socket):
    shutdown_msg = "\33[31m\33[1m Server is shutting down! Disconnecting clients...\33[0m\n"
    for sock in connected_list:
        try:
            sock.send(shutdown_msg.encode())
            sock.close()
        except:
            continue
    server_socket.close()
    sys.exit("Server shut down successfully.")

def main():
    password = input("\33[34m\33[1m Enter a password to set up the server: \33[0m")
    
    record = {}
    connected_list = []
    buffer = 4096
    port = 5003
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(10)
    
    connected_list.append(server_socket)
    
    print("\33[32m \t\t\t\tSERVER WORKING \33[0m")
    
    shutdown_thread = threading.Thread(target=shutdown_listener, args=(connected_list, server_socket))
    shutdown_thread.daemon = True
    shutdown_thread.start()
    
    server_shutting_down = False

    while True:
        if server_shutting_down:
            break 
        
        rList, wList, error_sockets = select.select(connected_list, [], [])

        for sock in rList:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                sockfd.send("\33[34m\33[1m Enter the server password: \33[0m".encode())
                entered_password = sockfd.recv(buffer).decode().strip()
                
                if entered_password != password:
                    sockfd.send("\33[31m\33[1m Incorrect password! Connection terminated. \33[0m".encode())
                    sockfd.close()
                    continue
                
                name = sockfd.recv(buffer).decode().strip()
                if name in record.values():
                    sockfd.send("\r\33[31m\33[1m Username already taken!\n\33[0m".encode())
                    sockfd.close()
                    continue
                else:
                    connected_list.append(sockfd)
                    record[addr] = name
                    print(f"Client ({addr[0]}, {addr[1]}) connected as [{name}]")
                    sockfd.send("\33[32m\r\33[1m Welcome to the chat room. Enter 'tata' anytime to exit\n\33[0m".encode())
                    send_to_all(sockfd, f"\33[32m\33[1m\r {name} joined the conversation \n\33[0m".encode(), connected_list, server_socket)
            
            else:
                try:
                    data1 = sock.recv(buffer)
                    if not data1:
                        continue
                    
                    data = data1.decode().strip()
                    try:
                        i, p = sock.getpeername()
                    except Exception as e:
                        print(f"Error retrieving peer name: {e}")
                        continue
                    
                    if data == "tata":
                        msg = f"\r\33[1m\33[31m {record[(i, p)]} left the conversation \33[0m\n"
                        send_to_all(sock, msg.encode(), connected_list, server_socket)
                        print(f"Client ({i}, {p}) is offline as [{record[(i, p)]}]")
                        del record[(i, p)]
                        connected_list.remove(sock)
                        sock.close()
                        continue
                    else:
                        msg = f"\r\33[1m\33[35m {record[(i, p)]}: \33[0m{data}\n"
                        send_to_all(sock, msg.encode(), connected_list, server_socket)

                except Exception as e:
                    print(f"Error handling client: {e}")
                    try:
                        i, p = sock.getpeername()
                        send_to_all(sock, f"\r\33[31m \33[1m{record.get((i, p), 'Unknown')} left unexpectedly\33[0m\n".encode(), connected_list, server_socket)
                        if (i, p) in record:
                            del record[(i, p)]
                    except Exception as nested_e:
                        print(f"Nested error: {nested_e}")
                    finally:
                        if sock in connected_list:
                            connected_list.remove(sock)
                        sock.close()
                    continue

    server_socket.close()

def shutdown_listener(connected_list, server_socket):
    global server_shutting_down
    while True:
        command = input("\33[31m\33[1m Type 'shutdown' to shut down the server: \33[0m").strip()
        if command.lower() == 'shutdown':
            server_shutting_down = True
            shutdown_server(connected_list, server_socket)

if __name__ == "__main__":
    main()