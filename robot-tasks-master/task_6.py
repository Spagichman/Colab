#!/usr/bin/python3

from pyrob.api import *
def runLetAll(n):
    for i in range(n):
        if not wall_is_on_the_right():
            move_right()
        elif not wall_is_beneath():
            move_down()
        elif not wall_is_on_the_left():
            move_left()
        elif not wall_is_above():
            move_up()
        elif i != n :
            return 1
    return 0

def runIfWall():
    while 1:
        if not runLetAll(1):
            if not(wall_is_beneath() or wall_is_on_the_left() or wall_is_above()):
                return 0

@task
def task_5_3():
    while not wall_is_beneath():
        move_right()
    runIfWall()


if __name__ == '__main__':
    run_tasks()