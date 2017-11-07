from Parser.Output import OutputHandler
import random


class Timer:
    """Skill for bot parser"""

    # Keywords for Parser
    TIMER_KEYWORDS = ("timer", "countdown")
    TIMER_SET = ("set", "create", "setze")
    TIMER_STOP = ("stop", "stoppe")
    TIMER_UNITS = ("minutes", "minute", "hours", "hour", "seconds", "second")

    TIMER_TOOMUCHTIME_RESPONSES = ("I do not have THAT much time to hang around",
                                   "In this time I will do much better stuff. Like sleeping.",
                                   "It's just too long, mate")
    TIMER_ARGUMENT_RESPONSES = ("I can try to set a countdown without a countdown time, but I won't",
                                "Just tell me how to set the timer")

    # Function parameters
    maxtime = 36000             # maximum countdown time is 10 hours

    # parser function
    @staticmethod
    def checktimer(words):
        """timer related skills"""
        for word in words:
            if word.lower() in Timer.TIMER_KEYWORDS:
                timer = Timer.checktimerinfo(words)
                return timer
        return False

    # parse for information
    @staticmethod
    def checktimerinfo(words):
        """get order, time and unit"""

        start = False
        stop = False
        time = 0
        unit = False

        # need time (smaller than certain time)
        for word in words:
            if word.lower() in Timer.TIMER_SET:
                start = True
            if word.lower() in Timer.TIMER_STOP:
                stop = True
            if Timer.checkint(word):
                time = int(word)
            if word.lower() in Timer.TIMER_UNITS:
                unit = word.lower()
        if start != stop and time != 0 and unit:
            # calc time in seconds
            if unit == "minute" or unit == "minutes":
                time = time * 60
            elif unit == "hours" or unit == "hour":
                time = time * 3600

            if time <= Timer.maxtime:
                # start timer
                Timer.response("Timer started with " + str(time) + " Seconds")
                return True
            else:
                Timer.response(random.choice(Timer.TIMER_TOOMUCHTIME_RESPONSES))
                return True
        else:
            Timer.response(random.choice(Timer.TIMER_ARGUMENT_RESPONSES))
            return True

    @staticmethod
    def checkint(word):
        """checks string if it is an integer"""
        try:
            int(word)
            return True
        except ValueError:
            return False

    @staticmethod
    def response(response):
        """adapter for central response function"""
        OutputHandler.response(response)