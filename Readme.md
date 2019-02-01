event-checkin
=============

This is a check-in system written in python to print nametags for people who come to our events. At our events, there will a line where people type in their username and it looks up their information from that to print their nametag.

Drivers and Requirements
------------------------

Before you do anything, make sure these drivers are installed on your computer:

- Macs: http://download.dymo.com/dymo/Software/Mac/DLS8Setup.8.5.3.dmg
- Linux: http://www.dymo.com/en-US/dymo-label-sdk-and-cups-drivers-for-linux-dymo-label-sdk-cups-linux-p--1
- Windows: http://download.dymo.com/dymo/Software/Win/DLS8Setup.8.7.3.exe

Also make sure you have Python installed, along with the Flask, requests, and Pillow libraries. You can create a python3 virtual environment, activate it, and then run `pip install -r requirements.txt`.

Operation/Setup
---------------

Mac/Linux/Windows Instructions:

This printing works on both Mac and Linux. To set up, plug in the printer and find the printer name. It's usually one of the following on the TechX laptops (for other laptops, look through your devices and printers to find the name):

- Macs: `DYMO_LabelWriter_450` or `DYMO_LabelWriter_450_Turbo`
- Linux: `LabelWriter-450` or `LabelWriter-450-Turbo`
- Windows: `DYMO LabelWriter 450` or `DYMO LabelWriter 450 Turbo`

These names have to be correct for the printing to work. Next, copy the `sample-config.json` file over to `config.json` and edit the appropriate values. This file will be loaded with the environment variables on startup. `LABEL_WIDTH` and `LABEL_HEIGHT` are two essentially magic numbers that correspond to the dimensions of the image this program sends to the label printers to print. Fiddle around with it, testing different aspect ratios and values until the resulting prints turn out nicely.

Finally run `python runserver.py` to run the checkin software. Every time someone is checked in, it will save the current timestamp and the person's email to `log.csv`.

To exit the checkin software, press Control-C twice rapidly (or just hold it).

Windows Instructions (Not Currently Working):

Please also update your computer's ip address in the config file above (with the name of printer and size of label). This can be found with a google search.

If you get an error involving the lpr command being invalid, take the following steps:

Go to Control Panel/Programs/Turn Windows Features on or off. Then, expand "Print and Document Services" and check "LPD Print Service" and "LPR Port Monitor."

This may be helpful for future fixing: https://www.blackice.com/Help/Internet/BILPDManager/WebHelp/How_to_set_up_LPR_LPD_Printer_on_Windows_10_and_Windows_Server_2016.htm

Labels
------

For nametag-like labels, the correct size is probably `LABEL_WIDTH=760 LABEL_HEIGHT=410`
For square, badge-like labels, the correct size is probably `LABEL_WIDTH=410 LABEL_HEIGHT=410`, but this could be wrong.

To modify the content printed on the labels, edit the `create_image` method of `checkin/printer/image.py`. There are a handful of methods in this file to facilitate image creation, but the most helpful one is probably `draw_horiz_centered_text`. It may take a few tries to find values for the y-offset parameter that work with the labels you're using.

While you're finding values that work, comment out the call to `lpr` in `checkin/printer/__init__.py` to temporarily disable printing so that you can debug the output images without wasting labels. The output images are located in `checkin/printer/labels`.

Directory structure (probably outdated)
---------------------------------------

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
