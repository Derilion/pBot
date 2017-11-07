#! /usr/bin/python

"""Core source file for the keystore program pVault"""

__author__ = "Maximilian Bier"
__version__ = "0.1a"
__status__ = "Prototype"

if __name__ == '__main__':

    from Parser.Input import InputHandler

    loop = True
    print("::Bot started::")
    while loop:
        user = input()
        loop = InputHandler.lookforkeywords(user)

