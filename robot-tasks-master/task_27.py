#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    move_right()
    fill_cell()
    move_right()
    i = 2
    while not wall_is_on_the_right():
        fill_cell()
        for j in range(i):
            if not wall_is_on_the_right():
                move_right()

        i += 1
    pass


if __name__ == '__main__':
    run_tasks()
