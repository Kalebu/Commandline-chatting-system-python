# Commandline chat app in Python 


## Intro 

Hi Guys this repo consist of a source code for a simple 

commandline chatting app made in python using socket 

This repo is continuation of an [Article](https://kalebujordan.com/chat-application-python/) on [my blog](https://kalebujordan.com/)

Therefore you can try checking first before playing with the source code 


## Getting started 

To get started just clone the repository using *git* command  or pressing download

button option at the right side of the repository

**Cloning**

```bash
$ git clone https://github.com/Kalebu/Commandline-chatting-system-python
$ cd Commandline-chatting-system-python
Commandline-chatting-system-python $ tree
.
├── client.py
├── README.md
└── server.py

0 directories, 3 files
```



This repo consist of two **Python scripts** named *client.py* and *server.py*

as I have explained on the tutorial, whereby **server.py** will serve as our server node 

and **client.py** will serve as our client node 


### Running our scipt 

**Note**

You should start running the server script before running the client script because if you do 

otherwise, the client will exit immediately as result of not finding a server node to connect

**running server.py**

```bash
$ python server.py

```

**running client.py**

```bash
$ python client.py
Enter server_ip: 127.0.0.1
Finding connection
Connection succesful made to the server
```

**Note**

If the server script is run on the different pc or laptop enter your server pubic IP on client 

enter ip prompt 

## Do some chatting 

Now youre script should be running and able to communicate with each other, you try writing message to any of those script

and then press enter to send the message to the another node whether it's server or client 


### Share and Give it a star
```

If you find it useful, don't be shy , share it will your fellow [Twitter](https://twitter.com/) and other dev communities

```
