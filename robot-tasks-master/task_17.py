#!/usr/bin/python3

from pyrob.api import *
def runWellAill():
    while not cell_is_filled():
        move_up()
    move_right()
    if cell_is_filled():
        return
    else:
        move_left(2)

@task
def task_8_27():
    runWellAill()


if __name__ == '__main__':
    run_tasks()
