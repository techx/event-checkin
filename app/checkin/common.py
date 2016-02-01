import os


def prompt(message, default=None):
    result = ""
    while True:
        if default is not None:
            prompt = "{:s} [{:s}]: ".format(message, default)
        else:
            prompt = message + ": "
        result = raw_input(prompt).strip()
        if result == "" and default is not None:
            result = default
        if result != "":
            return result
        print "Sorry, you must enter something."

def print_xfair_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print """
                                               Welcome to:

                                                    ,
                                                    #
           @@`      @@'        @@@@@@@@@           ;+@             '@,        +@@@@@@@'
           ;@@     '@@         @@#######           @++`            '@,        +@;::'#@@#
            @@#    @@          @@                 '#':@            '@,        +@,     @@
             @@`  @@,          @@                 @,';@.           '@,        +@,     @@.
             .@@ +@#           @@                #@,,#@@           '@,        +@,     @@.
              #@#@@            @@                @@+,@#@,          '@,        +@,     @@
               @@@`            @@+++++++        @@@@,@:@@          '@,        +@+++#@@@:
               @@@'            @@@@@@@@@       `@@;@,@ @@:         '@,        +@@@@@@#`
              @@,@@`           @@              @@@ @,@`@@@         '@,        +@.  @@
             '@@ :@@           @@             `;    `,   :'        '@,        +@,  :@@
            `@@   @@#          @@             :@`        @;        '@,        +@,   @@,
            @@,    @@.         @@            .@@         '@;       '@,        +@,   `@@
           +@@     :@@         @@            @@`          @@       '@,        +@,    #@#
          `@@       @@@        @@           ,@@           '@+      '@,        +@,     @@`
          ++,        ++.       ++           ++`            ++      ;+,        '+.     ;++

                                            February 1 - 2016
          """
