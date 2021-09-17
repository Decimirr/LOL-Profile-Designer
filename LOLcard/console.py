import platform
import os
from LOLcard import errors

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


def error(error_code):
    error_text = errors.ERRORMSG[error_code]

    if error_text:
        print(error_text)
        exit(error_code)
    else:
        print(errors.ERROR000)
        exit(1)
