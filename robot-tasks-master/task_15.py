#!/usr/bin/python3

from pyrob.api import *

def runWellAill(n):
    i = 0
    while i != n:
        if wall_is_above() and (not wall_is_on_the_right()):
            while wall_is_above() and (not wall_is_on_the_right()) :
                move_right()
            i+=1
        if i == n:
            return 0
        if wall_is_on_the_right() and (not wall_is_beneath()):
            while wall_is_on_the_right() and (not wall_is_beneath()):
                move_down()
            i+=1
        if i == n:
            return 0
        if wall_is_beneath() and (not wall_is_on_the_left()):
            while wall_is_beneath() and (not wall_is_on_the_left()):
                move_left()
            i+=1
        if i == n:
            return 0
        if wall_is_on_the_left() and (not wall_is_above()):
            while wall_is_on_the_left() and (not wall_is_above()):
                move_up()
            i+=1
        if i == n:
            return 0
    
        
    

@task
def task_8_21():
    runWellAill(2)


if __name__ == '__main__':
    run_tasks()
