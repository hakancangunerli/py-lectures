import pygame 
from turtle import* 

distance=0
for x in range(0,100):
  distance += 0.1
  forward(distance)
  right(12)
  