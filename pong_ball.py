# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 08:35:04 2023

@author: Hilal
"""
from turtle import Screen, Turtle;
import time
import random

class PongBall(Turtle): # create ball
    def __init__(self):
        super().__init__();
        self.shape("circle");  
        self.color("white");
        self.penup();
        self.screen = Screen();
        self.turtle_location = (0,0);
        self.xposition = 5;
        self.yposition = 5;
    
      
    def bounce(self):  # bounce when hit the upper and lower walls
        self.yposition *= -1;
        
    def paddle_bounce(self):  # bounce when hit the paddles
        self.xposition *= -1;
    
    def move(self):
        self.setposition(self.position() + (self.xposition,self.yposition));