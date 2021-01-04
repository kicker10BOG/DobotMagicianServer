# DobotMagicianServer
A web server for controlling a Dobot Magician robotic arm

## Why

I needed to replace my 20+ year old machine and all of the specialized devices were just too expensive, so I got a Dobot Magician because it's much less expensive and more versatile than any of the specialized devices. Being in software development, I knew I could write code to make it work how I wanted. And being decent with Fusion 360 made me confident I could design the necessary models. 

Video of how it works: https://www.youtube.com/watch?v=Gtf_Rhcddrw

The video shows a pi zero w, but I'm using a pi 3b+ now as I think there's something in the code I need to fix so it works more reliably over longer periods of time. Right now the Dobot service I setup needs to be restarted every so often or it stops serving and the 3b+ handles that much better than the zero w. I'll work on that when I get time.

Feel free to take the models and code and modify them for anything you need. I want this to be easily accessible an modifiable by anyone who needs it. I'm including the f3d and step files to make that easier.

I want to thank luismesas for creating the pydobot project. It made getting this to work much easier. I use a modified version of his library. You can find that project at https://github.com/luismesas/pydobot

## Dependencies
You're going to need to use pip to install the following libraries:

* cherrypy
* ws4py
* pyserial

That should be it for dependencies, but it's been a while since I set it up. If you see something else that needs to go here, create an issue. 

## Setup 
Use git to clone this repository. Then I suggest using a service to keep it running. Below is the service config I use.

```
[Unit]
Description=Dobot Magacian Server
After=network.target
StartLimitIntervalSec=0
[Service]
Type=simple
Restart=always
RestartSec=1
User=pi
WorkingDirectory=/home/pi/DobotMagicianServer
ExecStart=/usr/bin/python3 DobotServer.py

[Install]
WantedBy=multi-user.target
/etc/systemd/system/dobot.service (END)                                          
```