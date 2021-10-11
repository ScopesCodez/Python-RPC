import time, json, pypresence.exceptions
from pypresence import Presence
from colorama import Fore, Style, init
import os
init() #colorama initialize idk

with open('config.json') as ok:
    config = json.load(ok)

def presence():
    try:
        rpc = Presence(config.get('applicationid'))
        rpc.connect()
        os.system("clear||cls")
        os.system("title [Python RPC] - Rich Presence Set.")
        print(f'[{Fore.GREEN+Style.BRIGHT}*{Fore.RESET}] https://discord.com/developers/applications\n[{Fore.GREEN+Style.BRIGHT}*{Fore.RESET}] https://github.com/tokenlogger/Python-RPC/\n[{Fore.GREEN+Style.BRIGHT}+{Fore.RESET}] Set presence.')
        while True: #loop to keep the presence running
            rpc.update(details=config.get('details'), large_image=config.get('largeimage'), small_image=config.get('smallimage'), large_text=config.get('largeimagetect'), buttons=(config.get('buttons')))
            time.sleep(15)
    except pypresence.exceptions.InvalidID:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Invalid Application ID{Fore.RESET}.")
    except pypresence.exceptions.InvalidPipe:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Discord Process Not Found{Fore.RESET}.")
    except pypresence.exceptions.InvalidArgument:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Invalid Argument{Fore.RESET}.")
    except pypresence.exceptions.ArgumentError:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Argument Error{Fore.RESET}.")
    except pypresence.exceptions.ServerError:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Server Error{Fore.RESET}.")
    except pypresence.exceptions.DiscordError:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Discord Error{Fore.RESET}.")
    except pypresence.exceptions.EventNotFound:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Exception: {Fore.CYAN+Style.BRIGHT}Event Not Found{Fore.RESET}.")
    except pypresence.exceptions.PyPresenceException as a:
        print(f"[{Fore.RED+Style.BRIGHT}!{Fore.RESET}] Unknown Exception: {Fore.CYAN+Style.BRIGHT}{a}{Fore.RESET}.")
presence()
