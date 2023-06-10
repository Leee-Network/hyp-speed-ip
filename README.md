# Hyp Speed IP

**English** 

🚀 A simple, fast, high performance multipurpose TCP relay, primarily developed for building Hypixel reverse proxies.

## Feature Highlights

 - [x] ☝ One click to go
 - [x] 📋 Highly customizable configuration
 - [x] 🔌 TCP zero-copy relay on Linux with `splice(2)`, and 2 more relay modes
 - [x] 👮 Whitelist/Blacklist for IP and Minecraft player name (Access Control)
 - [x] 🔄 Configuration hot reload for lists and Minecraft MOTD
 - [x] 📦 Tailored high performance and lightweight Minecraft network protocol framework
 - [x] 💻 Clean and colorful log outputs, easy to track every connection
 - [x] 🔮 Multiple platforms and architectures
 - And more...


## What can it do?
In many situations you can use Nginx ```proxy_pass``` to easy relay your Minecraft data.  
The complete code is as follows:

```
stream {
    server {
        listen 25565;
        proxy_pass TARGET_SERVER_ADDRESS;
    }
}
```
But start from 2020, Hypixel set up an authentication of the player login address.  
If you do not log in from their official address as known as ```mc.hypixel.net:25565```, you will not be able to join the game.  
The original method is to cheat the server by modifying the ```hosts``` file.  
But that\'s too complicated for people who don\'t know the principle.  
We studied its working principle, and successfully bypassed the detection by modifying the data sent by client at the technical level.  
The product of the research is what you see now as ZBProxy.  
For players, just enter the address of your proxy server, you can join the game **directly** as usual.

### Is it safe?
There is no need to worry about privacy at all, because the connection to any Minecraft server which requires online verification is fully **encrypted**.  
Our code is completely open source, so you can freely check whether there is a backdoor.

## How to use it?
1. Download the compiled executable file at [Actions page](https://github.com/layou233/ZBProxy/actions "Actions"). Login required.  
2. Run it, and your relay service is now established!  
For Linux system, you may need to give permissions to the executable file in order to solve problems that cannot run or run blocked. Just enter the following command:
```bash
chmod +x PATH_TO_THE_FILE
```
3. Ensure the port **25565** is fully open on the server.
4. Enter your proxy server IP into your Minecraft client, and join it for game!  
    (Since the listening port is **25565**, you don\'t need to input the port number in the client, and the client will complete it automatically)  
