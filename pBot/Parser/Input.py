import random
import re
from Parser.TimerSkill import Timer
from Parser.Output import OutputHandler


class InputHandler:
    """Will determine how to parse inputs from the bot"""

    # keyword sets for individual skills

    GREETING_KEYWORDS = ("hello", "hallo", "hi", "hey", "heyo")
    GREETING_RESPONSES = ["Hi!", "Hey", "How are you?", "What is the mighty user up to?", "Hello mighty user"]

    QUESTION_KEYWORDS = ("what", "how")
    UNCLEAR_QUESTION_RESPONSES = ["Questions like that will get you nowhere.", "This is out of my scope",
                                  "I didn't quite get the question"]

    WEATHER_KEYWORDS = ("weather", "warm")

    ALARM_KEYWORDS = ("alarm", "wecker", "wake")

    END_KEYWORDS = ("that's it", "that is it", "goodbye", "bye", "cu", "ciao", "end")
    END_RESPONSES = ["And back to cryo", "Notice me, senpai...", "Mighty user my ass", "See you on the other side"]

    NO_SKILL_RESPONSES = ["Me nix comprende", "You should know I can't understand that", "If you say so",
                          "I dont't understand"]

    @staticmethod
    def splitinput(botinput):
        """will split input strings in single words"""
        words = re.sub("[^\w]", " ", botinput).split()
        return words

    @staticmethod
    def lookforkeywords(botinput):
        """will compare input from the bot with a few sets of keywords"""
        words = InputHandler.splitinput(botinput)
        greeting = InputHandler.checkgreeting(words)
        question = InputHandler.checkquestion(words)
        timer = Timer.checktimer(words)
        alarm = InputHandler.checkalarm(words)
        end = InputHandler.checkend(words)
        if not (greeting | question | timer | alarm | end):
            OutputHandler.response(random.choice(InputHandler.NO_SKILL_RESPONSES))
        return not end

    @staticmethod
    def checkgreeting(words):
        """Checks, if the user is greeting the bot"""
        for word in words:
            if word.lower() in InputHandler.GREETING_KEYWORDS:
                OutputHandler.response(random.choice(InputHandler.GREETING_RESPONSES))
                return True
        return False

    @staticmethod
    def checkquestion(words):
        """checks for question markers, which demand an answer"""
        for word in words:
            if word.lower() in InputHandler.QUESTION_KEYWORDS:
                weather = InputHandler.checkweather(words)
                if not weather:
                    OutputHandler.response(random.choice(InputHandler.UNCLEAR_QUESTION_RESPONSES))
                return True
        return False

    @staticmethod
    def checkweather(words):
        """checks if a wheather skill should be activated"""
        for word in words:
            if word.lower() in InputHandler.WEATHER_KEYWORDS:
                OutputHandler.response("Lovely weather ahead!")
                return True
            #"apikey: "
        return False



    @staticmethod
    def checkalarm(words):
        """alarm related skills"""
        for word in words:
            if word.lower() in InputHandler.ALARM_KEYWORDS:
                print("here there be a alarm")
                return True
        return False

    @staticmethod
    def checkend(words):
        """Checks for an end to the program"""
        for word in words:
            if word.lower() in InputHandler.END_KEYWORDS:
                OutputHandler.response(random.choice(InputHandler.END_RESPONSES))
                return True
        return False
