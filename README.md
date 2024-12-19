
# Multi-User Chat Application with Local and Remote Connectivity

## About the Project

This Python-based chat application allows multiple users to communicate with each other through a single server. It is designed to be easy to use, with both local and internet-based connectivity options. The project uses ngrok to enable remote communication, making it accessible even when clients are not on the same network.

Whether you’re looking to host a local chat for friends or provide a simple remote chat service, this application is built to simplify the process for beginners and experts alike.

## Project Features

	1.	Multi-User Chatroom: Supports multiple users chatting simultaneously in real-time.
	2.	Secure Access: Protects the server with a customizable password.
	3.	Username Validation: Ensures no duplicate usernames are used in the chatroom.
	4.	Local Connectivity: Works within the same local network.
	5.	Remote Connectivity: Uses ngrok to enable internet-based chat functionality.
	6.	Graceful Server Shutdown: Admin can shut down the server safely, notifying all connected clients.
	7.	Cross-Platform: Works on Windows, Linux, and macOS.

## Project Requirements
	•	Python 3.x
	•	ngrok (for remote connectivity)
	•	A stable internet connection (for remote use).

## Setup and Installation

	Step 1: Clone the Repository

	Download the project from GitHub:
	
	
	git clone https://github.com/k1rbyd/Multi-Chat.git  
	cd Multi-Chat  
	
	
	Step 2: Install Python (if not installed)
		•	Download Python and install it.
		•	Verify installation by running:
	 
	
	python --version  
	
	
	Step 3: Install ngrok (for remote use)
		•	Download ngrok from ngrok.com.
		•	Extract the downloaded file and add it to your system’s PATH.
		•	Verify installation by running:
	
	
	ngrok version  
	

## How to Execute the Project

1. Starting the Server Locally

	1.	Run the server script:

	
	python server.py  
	

	•	You will be prompted to set a server password (e.g., 1234).
	•	The server will display the port it’s running on (default: 5002).

	2.	Connect clients:
	•	On each client machine, run the client script:
	
 	
	python client.py  
	

	•	Enter the server’s local IP (displayed on the server terminal) and port (e.g., 5002).
	•	Enter the server password and a unique username to join the chatroom.

2. Enabling Internet Connectivity with ngrok
	
 	1.	Start the server script as before:

	
	python server.py  
	

	•	The server will run on a port (default: 5002).

	2.	Open a new terminal and expose the server using ngrok:

	
	ngrok tcp 5002  
	

	•	ngrok will generate a URL like tcp://0.tcp.ngrok.io:PORT.

	3.	Connect clients remotely:
	•	Run the client script on each client machine:

	
	python client.py  
	

	•	Use the ngrok-generated URL and port when prompted.
	•	Enter the server password and a unique username to join the chatroom.

3. Freeing Up the Port (if needed)

If the server fails to start because the port is already in use, free it with:


lsof -i :5002  
kill -9 <PID>  


## File Descriptions

### server.py

The server-side script that:
	•	Starts the chat server.
	•	Accepts and authenticates client connections.
	•	Relays messages between clients.
	•	Handles graceful server shutdowns.

### client.py

The client-side script that:
	•	Connects to the server using IP and port.
	•	Allows users to send and receive messages.
	•	Handles disconnections gracefully.

## How It Works

For the Server
	•	The server runs on a specified port (default: 5002).
	•	Clients connect using the server’s IP and port.
	•	All client messages are relayed to other connected users.
	•	The server shuts down safely with the shutdown command, notifying all clients.

For the Clients
	•	Clients use the server’s IP, port, and password to connect.
	•	A unique username is required to join.
	•	Messages sent by one user are broadcast to all other users.
	•	Clients can exit the chatroom by typing tata.

## Sample Usage Scenarios

Local Chatroom
	•	Host a chatroom for friends connected to the same Wi-Fi or LAN.
	•	Use the local IP of the server to connect clients.

Remote Chatroom
	•	Host a chatroom accessible over the internet.
	•	Use ngrok to expose the server to remote users.

## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

