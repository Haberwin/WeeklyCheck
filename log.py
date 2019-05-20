#!/usr/bin/python
#coding:utf-8

from __future__ import print_function
import sys

class Log():
    class Color(object):
        BLACK  = 30
        BLUE   = 34
        GREEN  = 32
        CYAN   = 36
        RED    = 31
        PINK   = 35
        YELLOW = 33
        WHITE  = 37

    @staticmethod
    def SetColor(color):
        sys.stdout.write("\033[1;%sm" % (color))

    @staticmethod
    def ResetColor():
        sys.stdout.write("\033[0m")

    @staticmethod
    def Pink(text):
        Log.SetColor(Log.Color.PINK)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Cyan(text):
        Log.SetColor(Log.Color.CYAN)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Black(text):
        Log.SetColor(Log.Color.BLACK)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Blue(text):
        Log.SetColor(Log.Color.BLUE)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Green(text):
        Log.SetColor(Log.Color.GREEN)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Red(text):
        Log.SetColor(Log.Color.RED)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Yellow(text):
        Log.SetColor(Log.Color.YELLOW)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def White(text):
        Log.SetColor(Log.Color.WHITE)
        sys.stdout.write(text)
        Log.ResetColor()

    @staticmethod
    def Tag(tag, msg):
        Log.Black("[%7s]" % tag.lower())
        print(msg)

    @staticmethod
    def Aais(msg):
        Log.Black("[   aais]")
        print(msg)

    @staticmethod
    def Info(msg):
        Log.Green("[   info]")
        print(msg)

    @staticmethod
    def Warning(msg):
        Log.Yellow("[warning]")
        print(msg)

    @staticmethod
    def Error(msg):
        Log.Red("[  error]")
        print(msg)

    @staticmethod
    def Verbose(msg):
        Log.Blue("[verbose]")
        print(msg)
