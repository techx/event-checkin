event-checkin
=============

A JS app for [TechX][1] that lets users type in their Athena usernames,
confirm, and submit for printing.

**Requirements**

1. You'll need to have the `athenas.json` and `studentinfo.json` files for this to work. You can generate this data by running `bootstrap/bootstrap` on Athena.
2. You'll need the Dymo drivers in order to use the printers via USB. You can download them from [the Dymo website][2].
3.  You'll need to run a webserver in this directory.
    - For Mac/Linux: run `python -m SimpleHTTPServer 8000` in the command line and open `http://localhost:8000` in a webbrowser 
    - For Windows: Download [Mongoose Free Edition][3], paste the file into the directory of this repository, and run it

[1]: http://techx.mit.edu/
[2]: http://dymo.com/en-US/dymo-user-guides
[3]: http://cesanta.com/mongoose.shtml