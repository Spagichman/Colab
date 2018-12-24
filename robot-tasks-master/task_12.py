#!/usr/bin/python3

from pyrob.api import *
def _wall():
    if (not wall_is_above() )and wall_is_beneath():
        fill_cell()
    

@task
def task_8_6():
    while not wall_is_on_the_right():
        _wall()
        move_right()
    _wall()


if __name__ == '__main__':
    run_tasks()
