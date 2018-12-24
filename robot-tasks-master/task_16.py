#!/usr/bin/python3

from pyrob.api import *
def runWellAill():
    while not wall_is_above():
        move_up()
    if wall_is_on_the_right():
        while not wall_is_on_the_left():
            move_left()
    else:
        while not wall_is_on_the_right():
            move_right()

@task
def task_8_22():
    runWellAill()


if __name__ == '__main__':
    run_tasks()
