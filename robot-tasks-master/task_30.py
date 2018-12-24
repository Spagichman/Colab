#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.001)
def task_9_3():
    cells_count = 1
    while(not wall_is_on_the_right()):
        move_right()
        cells_count += 1
    right_paint = 0
    center_paint = cells_count - 2
    left_paint = 0
    # higher average
    while center_paint > 0:
        if left_paint:
            for i in range(left_paint):
                fill_cell()
                move_left()
        move_left()
        if center_paint:
            for i in range(center_paint):
                fill_cell()
                move_left()

        if right_paint and not wall_is_on_the_left():
            move_left()
            for i in range(right_paint):
                fill_cell()
                if(not wall_is_on_the_left()):
                    move_left()
        while (not wall_is_on_the_right()):
            move_right()
        move_down()
        right_paint += 1
        left_paint += 1
        center_paint -= 2
    # average line
    for i in range(right_paint):
        fill_cell()
        move_left()
    move_left()
    for i in range(left_paint):
        fill_cell()
        if (not wall_is_on_the_left()):
            move_left()
    while (not wall_is_on_the_right()):
        move_right()
    move_down()
    right_paint -= 1
    left_paint -= 1
    center_paint += 2
    # bottom of average
    while center_paint <= cells_count - 2:
        if left_paint:
            for i in range(left_paint):
                fill_cell()
                move_left()
        move_left()
        if center_paint:
            for i in range(center_paint):
                fill_cell()
                move_left()

        if right_paint and not wall_is_on_the_left():
            move_left()
            for i in range(right_paint):
                fill_cell()
                if(not wall_is_on_the_left()):
                    move_left()
        while (not wall_is_on_the_right()):
            move_right()
        if(not wall_is_beneath()):
            move_down()
        right_paint -= 1
        left_paint -= 1
        center_paint += 2
    while not wall_is_on_the_left():
        move_left()
    pass


if __name__ == '__main__':
    run_tasks()
