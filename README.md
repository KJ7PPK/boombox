# boombox
Boombox is a 20-cue fireworks cue controller, meant to be a low-cost alternative to expensive and restrictive commercial fireworks sequencing systems. It leverages a Pico MCU & a lot of soldering to trigger mosfets that are wired to spring-loaded speaker terminals that activate electronic fuses. I haven't worked on this in over a year, but I was able to connect to the Pico's hot spot, view the control webpage, and trigger GPIO pins. 

I'd 3D printed the fuse terminal blocks and started assembling and soldering before life got in the way. I'm uploading here in hopes that I will pick it up again for an upcoming NYE celebration or just for fun since I have a bin with all the parts I need. I'll populate this more with specific hardware & figure out what's going on with all my firmware files when time allows. For now, this beats rotting away in the recesses of my "WIP SCRATCH" folder. 

_Rough Outline_
**Hardware**
1. Pi Pico 2W
2. 10-pin military/aviation-type screw on connectors
3. Standard red/black spring-clamp speaker terminal connectors.
4. 10-conductor flexible cabling.
5. PCB breadboard
6. MOSFETs
7. misc. TBD
8. 3D printed parts: enclosure for main controller, enclosures for 4x 5-cue terminal blocks

**Planned Features**
1. Handles 20 individual cues with electronic disposable fuses.
2. Triggers each cue via GPIO pin connected to mosfet to create short to ignite electric fuse.
3. Built-in Wi-Fi hotspot allows you to connect and control/program on the fly from your phone or laptop.
4. Sequence building, cue delays, etc.
5. Music segment analysis and synchronization.
6. Firework type / duration definitions
7. Expandable to ?? cues with additional Picos & cues connecting to the primary via Wi-Fi.
8. Redundant safety measures including manual arming & confirmations per cue.
9. Tracks which cues have been triggered in the current session.

<img width="605" height="550" alt="image" src="https://github.com/user-attachments/assets/b0c614b9-12e3-44ac-bdb9-b7adcc219cfa" />
