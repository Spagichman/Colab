#!/usr/bin/python3

from pyrob.api import *
def runWellAill():
    if wall_is_above():
        while not wall_is_on_the_left():
            move_left()
            if not wall_is_above():
                break
        else:
            while not wall_is_on_the_right():
                move_right()
                if not wall_is_above():
                    break
            else:
                return 0
            return 1
    else:
        return 0
            
        
            
@task
def task_8_28():
    runWellAill()
    while not wall_is_above():
            move_up()
    while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
