import time, json
from pypresence import Presence
from pypresence.exceptions import InvalidID
from colorama import Fore, Style, init
init() #colorama initualize idk

with open('config.json') as ok:
    config = json.load(ok)

rpc = Presence(config.get('applicationid'))
rpc.connect()
print(f'[{Fore.GREEN}{Style.BRIGHT}*{Fore.RESET}] https://discord.com/developers/applications')
print(f'[{Fore.GREEN}{Style.BRIGHT}*{Fore.RESET}] https://github.com/tokenlogger/Python-RPC/')
print(f'[{Fore.GREEN}{Style.BRIGHT}+{Fore.RESET}] Set presence.')
while True: #loop to keep the presence running
    rpc.update(details=config.get('details'), large_image=config.get('largeimage'), small_image=config.get('smallimage'), large_text=config.get('largeimagetect'), buttons=(config.get('button')))
    time.sleep(15)
