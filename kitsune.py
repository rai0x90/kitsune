from riposte import Riposte
from colorama import Fore, Style, init
from modules.routers import *
import sys
import os


repl = Riposte()
init(autoreset = True)

BANNER = Fore.MAGENTA + """
 000      000        000                                                                     
 000     000   000   000             Y0000   000     000   000  A000A         .d0000000b.    
 000   000     000   000          0000       000     000   00000    0000     d000P   Y000b   
 000000              000000     0000         000     000   000        000   d000P     Y00b   
 000  000      000   000           Y0000     000     000   000        000   000000000000000  
 000   000     000   000              Y000   000     000   000        000    Y00000b.       
 000    000    000   Y00b.         0000Y     000     000   000        000      Y000000b.     
 000     000   000    'Y0000    0000Y          Y0000Y      000        000        'Y000000    

                                  <<< @rai, OniSec >>>

                                ╔═════════════════════════╗
                                ║   [1] Website           ║  
                                ║   [2] Windows           ║  
                                ║   [3] Linux             ║  
      Hacking Options ==>       ║   [4] Mac OS X          ║  
                                ║   [5] Person            ║   
                                ║   [6] Embedded Devices  ║  
                                ╚═════════════════════════╝  
                                            

"""


class Application:
    def __init__(self):
        self.module = None

class kitsuneRiposte(Riposte):
    @property
    def prompt(self):
        if app.module:
            return f"\033[1m\033[36m[kitsune]({app.module}) :> "
        else:
            return self._prompt     # ref to prompt param

app = Application()
kit = kitsuneRiposte(banner = BANNER, prompt = '\033[36m' + "[kitsune] :> ")
init(autoreset = True)

@kit.command("exit")
def exit():
    kit.success("kitsune exited")
    sys.exit()

@kit.command("set")
def set_module(module_name: str):
    app.module = module_name
    kit.success("module set")

@kit.command("unset")
def unset_module():
    app.module = None
    kit.success("module unset")


@kit.command("hack")
def hack(hack_option: int):
    if hack_option == 1:
        target = input("what is the URL of target (google.com): ")
        kit.print('\033[1;33m' + "[!] website recon starting...")
        os.system('python3 modules/website/autoscan.py -t ' + target + ' --linkedin')
    if hack_option == 2:
        kit.print('\033[1;33m' + "[!] win machine recon starting...")
    if hack_option == 3:
        kit.print('\033[1;33m' + "[!] linux machine recon starting...")
    if hack_option == 4:
        kit.print('\033[1;33m' + "[!] mac os machine recon starting...")
    if hack_option == 5:
        kit.print('\033[1;33m' + "[!] starting OSINT...")
    if hack_option == 6:
        kit.print('\033[1;33m' + "[!] starting RouterSploit...")
        os.system('python3 modules/routers/routersploit/rsf.py')

kit.run()


