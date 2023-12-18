# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 04:31:11 2023

@author: Hilal
"""
from turtle import Screen, Turtle;

class Paddles():
    
    def __init__(self):
        self.screen = Screen();
        
        self.paddle1 = Turtle();
        self.paddle2 = Turtle();

        self.first_player();
        self.second_player();
        
    def first_player(self): # create paddle 1
        self.paddle1.penup();
        self.paddle1.shape("square");
        self.paddle1.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle1.setposition(350,0)
        self.paddle1.color("white")
    
    def second_player(self): # create paddle 2
        self.paddle2.penup();
        self.paddle2.shape("square");
        self.paddle2.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle2.setposition(-350,0)
        self.paddle2.color("white")
    # move paddles according to the users instructions
    def player1_up(self):
        position = self.paddle1.position();
        self.paddle1.setposition(position+(0,20))
    
    def player2_up(self):
        position = self.paddle2.position();
        self.paddle2.setposition(position + (0,20));
    
    def player1_down(self):
        position = self.paddle1.position();
        self.paddle1.setposition(position + (0,-20));
    
    def player2_down(self):
        position = self.paddle2.position();
        self.paddle2.setposition(position + (0,-20));

