# Making a more complex chat program with Python sockets
In the previous exersise, we looked at how to make a simple chat program in Python, so in this exersise, we'll look at how we can improve it so that both users can send and recieve messages at once.

## Getting started
First, make sure to make a copy of your client and server files from the last activity. We're goind to build off of those copies in this one.
Next we need to import 2 different libraries
  * `threading` - this lets our program do 2 different things at the same time
  * `tkinter` - this lets us make graphics for our program so it's easier to use
    * You can't make our better chat program unless you give it some graphics
Any code we do should be very similar for the server and client programs
    
## Setting up our graphics with tkinter
`tkinter` is a python library that lets us make graphics for our programs.
To do so, we have to make a window, fill that with a fram, and then fill it with all of the components we want to use (text boxes, etc.)

Here's some code to set up a basic chat window:
```python
top = tkinter.Tk() # Sets up the window, named 'top'
top.title("Chat Program!") # Sets the title of our window

msgFrame = tkinter.Frame(top) # Makes a new frame inside our window
msgList = tkinter.Listbox(msgFrame) # Sets up a big textbox inside our frame, so we can see all of the old messages
msgList.pack() # Shows the big textbox
msgFrame.pack() # Shows the frame

msg = tkinter.StringVar() # Sets up a message variable for us to change with a tkinter textbox
msgSendBox = tkinter.Entry(top, textvariable = msg) # Sets up a textbox to change our message variable
msgSendBox.bind('<Return>',sendData) # Tells tkinter to run the 'sendData' function when you press 'enter' in the textbox (we haven't made this function yet!)
msgSendBox.pack() # Shows the textbox

tkinter.mainloop() # should go at the end of your code - tells tkinter to start
```
## Sending and recieiving:
In our old chat program, we used a loop to put our send and recieves in. In this new version, we don't want to use a loop, instead we want it to send whenever tkinter asks it to, and to recieve whenever it gets any data.
To do this, we'll first need to make 2 functions - a send function, and a recieve function
The send function should look like this:
```python
def sendData(event=None): # Make sure to say 'event=None' - this tells tkinter that it doesn't need any extra information to send the data
    msgList.insert(tkinter.END, "Me: "+msg.get()) # Adds our message to our tkinter textbox
    clientSock.send(msg.get().encode()) # Sends the message with our socket
    msg.set("") # Clears our tkinter send textbox
```

The recieve function should look like this:
```python
def recvData():
    while True: # Infinite loop (always checking for data)
        recvMsg = clientSock.recv(1048) # Recieve up to 1048 letters of data
        msgList.insert(tkinter.END, "Received: "+recvMsg.decode()) # Adds our message to our tkinter textbox
```

In the previous section, we set up tkinter to call the `sendData` function, but we still haven't told our program how to recieve data yet!

## Recieving data with threads
Threads let our program do 2 or more things at once. Here, we want o make our program send AND recieve data at the same time. 
Threads help us do this.

To make a thread we need to say:
```python
recvThread = threading.Thread(target=recvData)
recvThread.start()
```
The first line makes a new thread. When you make a thread, you need to say what function it should use. We decided to use the function for recieving data here.
The second line tells the thread to start running in the background. That way it will start recieving data.

## Testing your code!
Once all your code is done up to here - you should be ready to test it out. You can test this code the same way you tested your old code.
Once it all works, put your hand up, and ask me to have a look so we can test it out using both your computer AND my computer.

After we finish that here's an extra challenge for you:

# Making a game using our sockets!
To help us practice our sockets, how about we try to make a game. This game will be a bit like Pokemon - where two players take turns telling their character what attacks they should use to beat the other player.
We won't use any graphics yet, but we might add some later, when it all works!

## Getting started
* First, make 2 new script files - our client and server - most of their code will be the same, and only a few lines will be different, so you might want to just focus on getting one ready before copying the code to the other one and making some small changes.
* Next we want to set up some variables (Give them whatever values you think they should be):
  * `PlayerHP` - The health points of the player
  * `PlayerAttack` - The damage the player does
  * `PlayerDefence` - The amount of armour the player has
  * `EnemyHP` - The health points of the enemy
  * `EnemyAttack` - The damage the enemy does
  * `EnemyDefence` - The amount of armour the enemy has
* Then, we want to make an infinite loop that asks our player what they want to do - attack, defend, or charge up?
  * If they choose `'attack'` - then take away some enemy HP! (Make sure to think about attack and defence here!)
  * If they choose `'defend'` - then boost the player's defence!
  * If they choose `'charge up'` - then boost the player's attack!
* Then do the same for the enemy - that way they can take turns!
* Test out the game in a single file (no sockets yet!), and make sure it works right - try and fix any problems you run into

## Adding our sockets for multiplayer
Once that works we can add our sockets so that you can play with two people on different computers!

For this, all you need to do is change how our enemy gets input!
Right now our enemy uses 'input' to ask what they should do. Instead, we want to make it so our enemy uses `socket.recv` to decide what to do.
Have a look at you simple chat program (the one with no graphics), and see if you can figure out how to combine these two programs to do this.
Don't forget to copy your code into a second file so we have a client AND a server.
Also don't forget to `socket.send()` your player actions to the other computer so they have something for the enemy to `socket.recv`

