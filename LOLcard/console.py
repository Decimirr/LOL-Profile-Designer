import platform
import os


MAIN = '\
┌──────────────────────────────────────┐\n\
│         LOL Profile Designer         │\n\
│ enter your summoner name (KR server) │\n\
└──────────────────────────────────────┘'


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
        return
    elif platform.system() == 'Linux':
        os.system('clear')
        return

