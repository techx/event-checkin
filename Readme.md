event-checkin
=============

This is a check-in system written in python to print nametags for people who come to our events. At our events, there will a line where people type in their username and it looks up their information from that to print their nametag.

Drivers
-------

Before you do anything, make sure these drivers are installed on your computer:

- Macs: http://download.dymo.com/dymo/Software/Mac/DLS8Setup.8.5.3.dmg
- Linux: http://www.dymo.com/en-US/dymo-label-sdk-and-cups-drivers-for-linux-dymo-label-sdk-cups-linux-p--1

Operation/Setup
---------------

*This software does not work with Windows*

This printing works on both Mac and Linux. To set up, plug in the printer and find the printer name. It's usually one of the following:

- Macs: `DYMO_LabelWriter_450` or `DYMO_LabelWriter_450_Turbo`
- Linux: `LabelWriter-450` or `LabelWriter-450-Turbo`

These names have to be correct for the printing to work. Next, copy the `.env.config` file over to `.env` and edit the appropriate values. This file will be loaded with the environment variables on startup. Finally run `python app.py` to run the checkin software. Every time someone is checked in, it will save the current timestamp and the person's email to `checked-in-emails.log`.

To exit the checkin software, press Control-C twice rapidly (or just hold it).

Labels
------

For nametag-like labels, the correct size is probably `LABEL_WIDTH=760 LABEL_HEIGHT=410`
For square, badge-like labels, the correct size is probably `LABEL_WIDTH=410 LABEL_HEIGHT=410`, but this could be wrong.

Directory structure
-------------------

**app.py**:
Used to bootstrap the program and contains the Checkin, Print, Log loop.

**app/checkin**:
Used to check people in and create a `User` object with the appropriately filled in fields. This user object is handed off to the printer to print, and to the logger to log.

**app/logger**:
Used to log the checked in users to either a file or webservice. Currently, just writes to a file.

**app/model**:
Used to hold all the models needed for the checkin library. Basically just the *User* model.

**app/printer**:
Used to deal with rendering nametags and printing them. If you want to change how the nametags look, you can do it here.


Bugs
----

Every time a label prints, the USB disconnects and reconnects. The consequence of this is that when you print two labels rapidly one after another, there is about an 8 second delay as the USB disconnects, finds the printer again, and starts the next job. Still looking for a fix for this one!
