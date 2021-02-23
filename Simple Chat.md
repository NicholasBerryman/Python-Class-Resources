# Making a simple chat program with Python sockets

## What is a socket?
Sockets are objects that computers use to send/recieve data to/from other computers.  
  
Sockets need to know 2 pieces of information before a connection can be made:  
* The target computer's address  
  * This is usually a string that looks like "123.456.789.123"
  * When you want to make a connection to and from a single computer, use "127.0.0.1"
* The port to connect on
  * This is a number that should be the same on both computers. It tells the computer which messages belong to this program, as opposed to other programs.
  
## Making Sockets in Python
To make a connection with sockets in Python you first need to make 2 files - a client and a server.
  * The server recieves connection requests, while the client sends connections requests
Inside each file you need to import the 'socket' library:
```python 
import socket
```

Once you've imported the socket library, you need to make a socket. This step is different for the client and server programs.
For the client:
```python
clientSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSock.connect(("[TARGET_ADDRESS]",[TARGET PORT]))
```
The first line makes a socket variable. It tells it to connect using the internet (socket.AF_INET), and to send data as a 'stream' (socket.SOCK_STREAM) rather than as lots of separate .little packages
The second line tells the socket to connect to the server at an address and port that you can decide yourself.

For the server:
```python
serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSock.bind(("[LOCAL_ADDRESS]",[TARGET PORT]))
serverSock.listen(1)
client, address = serverSock.accept()
```
The first line makes a socket variable. It tells it to connect using the internet (socket.AF_INET), and to send data as a 'stream' (socket.SOCK_STREAM) rather than as lots of separate .little packages
The second line tells the socket to set up as a server at the local computer address (if you're not sure what this is, just use 127.0.0.1), and a port that you can decide yourself. This should be the same port as your client.
The third line tells the socket to be ready for 1 client to connect.
The fourth line waits for a client to connect. It then sets the variable 'client' to be the socket that connects to that client, and the variable 'address' to be the address of that client.

## Using sockets in Python

Once you've made your sockets, you'll need to make some code to send messages between them.
The simplest way to do that is using the 'input' function, in a text based program, so we'll start there.
The code should be very similar for both the server and client:
* First you'll need to make an infinite loop - that way your program will be able to send and receive messages for as long as you want until you close it.
* Next, in that loop, you'll need to make a message variable that asks the user for input.
* Then, you'll need to send that message to the next computer:
    * `client.send(message.encode())`
    * You need to use '.encode()', because that turns the message into the 1s and 0s that sockets expect to send
* Then, you'll need to wait until you recieve a message:
    * `recievedMessage = client.recv(1024)`
    * The number in the brackets is the maximum message size. Make sure it's big enough, but things won't work if it's TOO big. 1024 is a good maximum size to use most of the time.
* Finally, you'll need to print out the message that you recieve:
    * `print("Received:",recvMsg.decode())`
    * You need to use '.decode()', because that decodes back into text from the 1s and 0s that sockets expect to recieve
    
## Testing out the program

Once you've done all your code, then you're ready to test your program. All you need to do is run both the server and the client, and then take turns sending messages.
This program makes you take turns with messages, but when you're done here, put your hand up, and we'll go to the next exersise, where we can send messages whenever we want, using tkinter and threads.

