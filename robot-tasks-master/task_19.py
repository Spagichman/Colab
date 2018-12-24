#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while not wall_is_on_the_right():
        move_right()
    other = 0
    if wall_is_above() and wall_is_beneath():
        other = 1
    if other:
        while not wall_is_on_the_left():
            move_left()
        if wall_is_above() and wall_is_beneath():
            while not wall_is_on_the_right():
                move_right()
        while not wall_is_above():
            move_up()
    else:
        while not wall_is_above():
            move_up()
        while not wall_is_on_the_left():
            move_left()
    pass


if __name__ == '__main__':
    run_tasks()
