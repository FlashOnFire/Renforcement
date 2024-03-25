# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 10:29:09 2023

@author: ninot
"""

import turtle as trt
import numpy as np
import matplotlib.pyplot as plt
import math as ma

DIMX = 10
DIMY = 10
D = 0.1


def SIM_2D(dimx, temps):
    A = init_mat(dimx)
    dt = (DIMX / dimx) ** 2
    PrecT = round(temps / dt)
    dt = temps / PrecT
    trt.tracer(0, 0)
    for i in range(PrecT):

        A = update_mat(dimx, dt, A)

        if (i % 100 == 0):
            # if (i%500 == 0) : trt.reset()
            trt.penup()
            trt.pencolor(1, 1, 1)
            trt.pensize(100)
            trt.goto(0, 0)
            trt.pendown()
            trt.write(i * dt)
            trt.update()
            afficher_temps(A, dimx)
    trt.done()


def afficher_temps(Mat, dimx):
    zoom = 2
    dimy = dimx
    tmax = max(Mat[0])
    tmin = min(Mat[0])
    for i in range(1, dimx):
        if (max(Mat[i]) > tmax): tmax = max(Mat[i])
        if (min(Mat[i]) < tmin): tmin = min(Mat[i])

    trt.pencolor(0, 0, 0.5)
    trt.speed("fastest")
    trt.goto(0, 0)
    trt.pensize(zoom)
    trt.hideturtle()
    trt.tracer(0, 0)
    trt.pendown()
    for y in range(dimy):  # on a dimy ligne
        for x in range(dimx):  # on a dimx colones
            r = Mat[y][x] / tmax
            v = 0.1
            b = 0.1
            trt.pencolor(r, v, b)
            trt.goto(x * zoom, -y * zoom)
        trt.penup()
        trt.goto(0, -y * zoom)
        trt.pendown()
    # print("new colone")
    trt.update()


# création d'une matrice en 2D avec les params init
def init_mat(dimx):
    Mat = []
    for y in range(dimx):  # on a dimy ligne
        Mat.append([])
        for x in range(dimx):  # on a dimx colones
            if (x == 0):
                Mat[y].append(1)
            else:
                Mat[y].append(0)
    return Mat


# créé une nouvelle matrice avec les nouveaux paramètres
def update_mat(dimx, dt, M):
    global DIMX, DIMY, D

    idx2 = (DIMX / dimx) ** 2
    idy2 = (DIMY / dimx) ** 2
    idxy2 = 1 / (idx2 + idy2)
    idx2 = 1 / idx2
    idy2 = 1 / idy2
    temp = M
    txy: float
    for y in range(1, dimx - 1):
        for x in range(1, dimx - 1):
            txy = (M[x - 1][y - 1] + M[x + 1][y - 1] + M[x + 1][y + 1] + M[x + 1][y + 1] - 4 * M[x][y]) * idxy2
            txy += (M[x - 1][y] + M[x + 1][y] - 2 * M[x][y]) * idx2
            txy += (M[x][y - 1] + M[x][y + 1] - 2 * M[x][y]) * idy2
            # print(txy*dt*D)
            temp[x][y] += txy * dt * D
    # print(temp)
    return temp


SIM_2D(DIMX, 1)