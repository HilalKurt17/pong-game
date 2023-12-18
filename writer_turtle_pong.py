# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 03:18:48 2023

@author: Hilal
"""
from turtle import Turtle;

class Writer():
    def __init__(self):   # create writer turtle to write score board
        self.turtle1 = Turtle();
        self.turtle2 = Turtle();
        self.turtle1.penup();
        self.turtle2.hideturtle();
        self.turtle1.hideturtle();
        self.turtle1.color("white");
        self.turtle2.color("white");
        self.turtle1.setposition(0,300);
        self.turtle1.pendown();
        for i in range(0,60):
            self.turtle1.setposition(self.turtle1.position()-(0,10));
            self.turtle1.penup();
            self.turtle1.setposition(self.turtle1.position()-(0,10));
            self.turtle1.pendown();
            
            
    def score_table(self,score_paddle1, score_paddle2):
        self.turtle2.clear();
        self.turtle2.penup();
        self.turtle2.setposition(-40,260)
        self.turtle2.write("{0}".format(score_paddle2), font=('Arial', 30, 'normal'));
        
        self.turtle2.penup();
        self.turtle2.setposition(40,260)
        self.turtle2.write("{0}".format(score_paddle1), font=('Arial', 30, 'normal'));