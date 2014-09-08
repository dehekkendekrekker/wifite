#!/usr/bin/python
import curses
import sys
import ConfigParser
import stations
import targeter
import attacker
import traceback
import display
import time


""" Read config """
config = ConfigParser.ConfigParser()
config.read("neofite.ini")

""" Init main screen """


def main(screen):
    main_screen = display.Dispay(screen)

    """ Acquire targets """
    target_selector = targeter.Targeter(config)

    i = 0

    while True:
        found_stations = stations.load_stations("test-01.csv")
        target_selector.set_possible_targets(found_stations.aps)
        main_screen.add_status_message(str(i))
        main_screen.update(target_selector.targets)
        i+=1



try:
    curses.wrapper(main)
except KeyboardInterrupt:
    print "Got KeyboardInterrupt exception. Exiting..."
    exit()






