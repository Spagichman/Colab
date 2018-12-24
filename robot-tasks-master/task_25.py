#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_2_2():
    move_right()
    move_down(2)
    fill_cell()
    move_right()
    fill_cell()
    move_left()
    move_down()
    fill_cell()
    move_up()
    move_left()
    fill_cell()
    move_right()
    move_up()
    fill_cell()
    move_down()
    for i in range(4):
        move_right(4)
        fill_cell()
        move_right()
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up()
        move_left()
        fill_cell()
        move_right()
        move_up()
        fill_cell()
        move_down()
    move_left()
    move_up()
    pass


if __name__ == '__main__':
    run_tasks()
