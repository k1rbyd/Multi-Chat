import socket
import select
import sys

def display():
    """
    Displays the user prompt for input.
    """
    you = "\33[33m\33[1m" + " You: " + "\33[0m"
    sys.stdout.write(you)
    sys.stdout.flush()

def main():
    """
    Main function to handle client-side communication.
    """
    # Get the host and port
    if len(sys.argv) < 3:
        host = input("Enter host IP address (e.g., 0.tcp.ngrok.io): ").strip()
        port = int(input("Enter port (e.g., 12591): ").strip())
    else:
        host = sys.argv[1]
        port = int(sys.argv[2])

    # Create and configure socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)

    # Attempt connection
    try:
        s.connect((host, port))
    except socket.error as e:
        print(f"\33[31m\33[1m Can't connect to the server: {e} \33[0m")
        sys.exit()

    # Handle password authentication
    password = input("\33[34m\33[1m Enter the server password: \33[0m")
    s.send(password.encode()) 
    
    # Check server response for password
    data = s.recv(4096).decode()
    if "Incorrect password" in data:
        print(f"\33[31m\33[1m {data} \33[0m")
        sys.exit()

    # Handle username input
    name = input("\33[34m\33[1m Enter username: \33[0m")
    s.send(name.encode())  
    
    display()

    while True:
        # Listen for input or server messages
        socket_list = [sys.stdin, s]
        rList, wList, error_list = select.select(socket_list, [], [])
        
        for sock in rList:
            if sock == s:  # Incoming message from server
                try:
                    data = sock.recv(4096)
                    if not data:
                        print('\33[31m\33[1m \rDISCONNECTED!!\n \33[0m')
                        sys.exit()
                    else:
                        sys.stdout.write(data.decode()) 
                        display()
                except socket.error as e:
                    print(f"\33[31m\33[1m Error receiving data: {e} \33[0m")
                    sys.exit()
            else:  # User input to send to server
                msg = sys.stdin.readline()
                try:
                    s.send(msg.encode())  
                except socket.error as e:
                    print(f"\33[31m\33[1m Error sending data: {e} \33[0m")
                    sys.exit()
                display()

if __name__ == "__main__":
    main()