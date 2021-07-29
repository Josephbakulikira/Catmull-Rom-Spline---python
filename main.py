import pygame
import os

from constants import size, Width, Height, black
from event import HandleEvent
from point import Point
from spline import Spline
from math import atan2, degrees
import pickle

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

# load Assets
filename = 'editedSpline'

current_directory = os.path.dirname(os.path.abspath(__file__))
carImage_path = os.path.join(current_directory, "./assets/car.png")
car_sprite = pygame.image.load(carImage_path)
sprite = pygame.transform.scale(car_sprite, (100, 50))

CarPosition = 0.0
speed = 1

#  -- create new Spline
# curve = Spline()
# curve.CreatePoints(10, True)

# or

# load the saved spline
curve = pickle.load(open(filename, 'rb'))

MouseClicked = False
run = True
while run:
    screen.fill( (10, 10, 10) )
    clock.tick(fps)
    keys = pygame.key.get_pressed()

    run, MouseClicked = HandleEvent()
    curve.Draw(screen, MouseClicked)

    if keys[pygame.K_UP] or keys[pygame.K_w]:
        CarPosition += speed
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        CarPosition -= speed

    if CarPosition >= len(curve.points) * curve.resolution:
        CarPosition -= len(curve.points) * curve.resolution
    if CarPosition < 0:
        CarPosition += len(curve.points) * curve.resolution

    p1 = curve.GetSplinePoints(CarPosition, True)
    g1 = curve.GetSplineGradient(CarPosition, True)

    angle = atan2(-g1[1], g1[0])

    rotated = pygame.transform.rotate(sprite, degrees(angle))
    rect = rotated.get_rect()
    x, y = p1[0] - rect.width//2, p1[1] - rect.height//2
    screen.blit(rotated,(x, y))

    pygame.display.flip()
    MouseClicked = False

#save our edited curve spline class
pickle.dump(curve, open(filename, 'wb'))

pygame.quit()
