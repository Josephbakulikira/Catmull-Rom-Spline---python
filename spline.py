import pygame
from point import Point
from random import randint
from constants import Width, Height, screen_offset, black, white
from math import sqrt, pow

class Spline:
    def __init__(self):
        self.points = []
        self.pointRadius = 10
        self.resolution = 20
        self.lineWidth = 5
        self.lineColor = white
        self.move = 0

    def CreatePoints(self, n, showLabel=False):
        for i in range(n):
            x = i * Width//n
            y = randint(screen_offset, Height-screen_offset)
            point = Point(x, y, self.pointRadius)
            if showLabel:
                point.label = "P" + str(i)
            self.points.append(point)

    def GetSplinePoints(self, t, loop=False):
        t = t/self.resolution

        if loop == False:
            p1 = int(t) + 1
            p2 = p1 + 1
            p3 = p2 + 1
            p0 = p1 - 1
        else:
            p1 = int(t)
            p2 = (p1 + 1) % len(self.points)
            p3 = (p2 + 1) % len(self.points)
            p0 = p1 - 1 if p1 >= 1 else len(self.points) - 1

        t = t - int(t)

        tt = pow(t, 2)
        ttt = pow(t, 3)

        f1 = -ttt + 2 * tt - t
        f2 = 3 * ttt - 5 * tt + 2
        f3 = -3 * ttt + 4 * tt + t
        f4 = ttt - tt

        _x = (self.points[p0].x * f1 + self.points[p1].x * f2 + self.points[p2].x * f3 + self.points[p3].x * f4) / 2
        _y = (self.points[p0].y * f1 + self.points[p1].y * f2 + self.points[p2].y * f3 + self.points[p3].y * f4) / 2

        return (_x, _y)

    def GetSplineGradient(self, t, loop=False):

        t = t/self.resolution

        if loop == False:
            p1 = int(t) + 1
            p2 = p1 + 1
            p3 = p2 + 1
            p0 = p1 - 1
        else:
            p1 = int(t)
            p2 = (p1 + 1) % len(self.points)
            p3 = (p2 + 1) % len(self.points)
            p0 = p1 - 1 if p1 >= 1 else len(self.points) - 1

        t = t - int(t)

        tt = pow(t, 2)
        ttt = pow(t, 3)

        f1 = -3 * tt + 4 * t - 1
        f2 = 9 * tt - 10 * t
        f3 = -9 * tt + 8 * t + 1
        f4 = 3 * tt - 2 * t

        _x = (self.points[p0].x * f1 + self.points[p1].x * f2 + self.points[p2].x * f3 + self.points[p3].x * f4) / 2
        _y = (self.points[p0].y * f1 + self.points[p1].y * f2 + self.points[p2].y * f3 + self.points[p3].y * f4) / 2

        return (_x, _y)

    def Draw(self, screen, clicked):
        keys = pygame.key.get_pressed()

        for i in range(self.resolution * len(self.points)):
            x, y = self.GetSplinePoints(i, True)
            pygame.draw.rect(screen, self.lineColor, [int(x), int(y), self.lineWidth, self.lineWidth])

        for point in self.points:
            point.update(clicked)
            point.Draw(screen)
