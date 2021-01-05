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
* jinja2

That should be it for dependencies, but it's been a while since I set it up. If you see something else that needs to go here, create an issue. 

## Setup 
Use git to clone this repository. Then I suggest using a service to keep it running. Below is the service config I use at `/etc/systemd/system/dobot.service`.

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
```

After creating that file and checking to make sure the paths are correct, run the following command to have the systemd discover it. Depending on your user permissions, you may need to use sudo. 

```systemctl daemon-reload```

The next command is optional but will ensure it is always enabled.

```systemctl enable dobot.service```

The next one will start it.

```systemctl start dobot.service```

## How It Works
First, it uses websockets to keep everything synced. This is great if you need to have the ability to control it from more than one device. 

The home page of the server has standard controls for the arm. 

Note that it is important to always home the arm before using it after turning it on. This is especially important when trying to repeat specific movements. 

I've tried to design it so that it's easy to create new addons in the future. This is done by using jinja2 for templating and conf files for specifying what addons to use. Right now the only addon is the spoon addon. 

### Spoon Addon
This addon uses a json file to store profiles for different types of spoons. You can easily swap between profiles in the user interface. I still need to add a way to create, edit, and delete profiles in the browser, but it's possible to do those by editing the json file directly. 

The controls on this addon should be pretty self-explanatory, but essentially there are two types of movement in the controls.

1) Performing a motion
2) Going to a specific position

When performing a motion, it chains two or more positions together. 

* The "lower" motion goes the "back" position then the "down" position. 
* The "scoop" motion goes the "down" position then the "scoop" position. 
* The "lower" motion goes the "scoop" position then the "up" position. 

When gusing the position buttons, the arm just goes straight to that position. 

* The "up" position puts the spoon in a position that should be close to the mouth. 
* The "back" position should put the spoon at the top of the back of the bowl. 
* The "down" position puts the spoon either at the bottom of the bowl or close to it. I have profiles that do both and I switch between them depending on how full the bowl is. 
* The "scoop" position should bring the spoon up just out of the bowl in a level position so nothing falls off (usually). 