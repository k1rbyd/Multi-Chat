
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

This guide explains how to execute the chat application in different scenarios, ensuring even beginners can follow along easily.

### 1. Starting the Server Locally

	Case 1: All Clients and Server on the Same Device
	
	If the server and clients are running on the same device, follow these steps:
		1.	Start the Server:
	Run the server script:
	
	python server.py
	
		•	You will be prompted to create a server password. For example, enter 1234.
		•	The server will start and display the port it’s running on, which by default is 5002.
	
		2.	Connect Clients:
		•	Run the client script on the same device:
	
	python client.py
	
	
		•	Enter the following details when prompted:
		•	Server IP: Use localhost (since everything is on the same device).
		•	Port: Enter 5002 (default port).
		•	Password: Enter 1234 (or the password you set earlier).
		•	Username: Enter a unique username (e.g., User1).
	Once connected, you can start chatting!
	
	Case 2: Clients and Server on the Same Local Network
	
	If the server and clients are on the same Wi-Fi or LAN, follow these steps:
		1.	Start the Server:
		•	Run the server script on the device hosting the server:
	
	python server.py
	
	
		•	Set a password (e.g., 1234) when prompted.
		•	The terminal will display the local IP and the port (default: 5002).
	
		2.	Connect Clients:
		•	Run the client script on other devices connected to the same network:
	
	python client.py
	
	
		•	Enter the following details when prompted:
		•	Server IP: Use the local IP of the server device (e.g., 192.168.1.5).
		•	Port: Enter 5002 (default port).
		•	Password: Enter 1234.
		•	Username: Enter a unique username.
	Clients connected via the same network can now chat in real time!

### 2. Enabling Internet Connectivity with ngrok

	For remote communication over the internet, ngrok allows you to expose your local server to the world.
	
	Case 3: Server and Clients on Different Networks
	
	Follow these steps to connect clients over the internet:
		1.	Start the Server:
		•	Run the server script on the host device:
	
	python server.py
	
	
		•	Set a password (e.g., 1234) when prompted.
		•	The terminal will display the port the server is running on (default: 5002).
	
		2.	Expose the Server with ngrok:
		•	Open a new terminal and run ngrok to expose the server:
	
	ngrok tcp 5002
	
	
		•	ngrok will generate a public URL. For example:
	
	Forwarding: tcp://0.tcp.ngrok.io:17423
	
		•	In this example, 0.tcp.ngrok.io is the IP, and 17423 is the port.
	
		3.	Connect Clients Remotely:
		•	Run the client script on remote devices:
	
	python client.py
	
	
		•	Enter the following details when prompted:
		•	Server IP: Use 0.tcp.ngrok.io (from the ngrok URL).
		•	Port: Enter 17423 (from the ngrok URL).
		•	Password: Enter the server password (e.g., 1234).
		•	Username: Enter a unique username.
	Remote clients can now join the chatroom from anywhere in the world!

### 3. Freeing Up the Port (if needed)

	If the server fails to start because the default port (5002) is already in use, free it up by following these steps:
		1.	Run the following command to check the process using the port:
	
	lsof -i :5002
	
	
		2.	Identify the PID (Process ID) from the output.
		3.	Kill the process using:
	
	kill -9 <PID>

	Now, you can restart the server without any issues.

## Summary of Execution
	•	Local: Clients connect using localhost and the port (e.g., 5002).
	•	Local Network: Clients use the server’s local IP (e.g., 192.168.1.5).
	•	Internet: ngrok generates a public URL (e.g., tcp://0.tcp.ngrok.io:17423) for remote connectivity.

## Example

	If ngrok generates the URL tcp://0.tcp.ngrok.io:17423:
		•	Server IP: 0.tcp.ngrok.io
		•	Port: 17423
	
	Remote clients would input this IP and port in the client script to connect.

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

![License](https://img.shields.io/github/license/k1rbyd/Multi-Chat)  
![Python](https://img.shields.io/badge/python-3.x-blue)  

