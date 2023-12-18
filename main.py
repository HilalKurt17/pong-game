# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 03:19:29 2023

@author: Hilal
"""
from functions_pong import Paddles;
from writer_turtle_pong import Writer;
import time
from turtle import Screen;
from pong_ball import PongBall



class Create_Screen():
    
    def __init__(self):
        # create screen, paddles and ball objects
        self.screen = Screen();
        self.screen.tracer(0)
        self.create_screen();
        self.paddles = Paddles();
        self.ball = PongBall();
        self.writer = Writer();
        
        # listen to user instructions
        self.screen.listen();
        self.screen.onkeypress(fun=self.paddles.player1_down, key="Down");
        self.screen.onkeypress(fun=self.paddles.player2_up, key="w");
        self.screen.onkeypress(fun=self.paddles.player2_down, key="s");
        self.screen.onkeypress(fun=self.paddles.player1_up, key="Up");
        # set score attributes to 0
        self.score_paddle2 = 0;
        self.score_paddle1 = 0;
        self.game_cond = True;

        self.game_on(self.game_cond); # begin the game
  
    def create_screen(self):
        self.screen.title("PONG GAME");
        self.screen.bgcolor("black")
        self.screen.screensize(800,600)
        self.screen.setworldcoordinates(-400,-300,400,300)
    
    def game_on(self,continue_):
        while continue_:
            goto_begin = False;
            self.screen.update();
            time.sleep(0.02)
            self.ball.move();
        
            if self.ball.ycor()>290 or self.ball.position()[1]<-290: # bounce when ball hits the upper and lower walls
                self.ball.bounce();
            
            if self.ball.xcor() == 330 and ((self.paddles.paddle1.ycor()-50 )<= self.ball.ycor() and self.ball.ycor() <= (self.paddles.paddle1.ycor()+50)):
                self.ball.paddle_bounce(); # bounce when ball hits the first paddle
                
            elif self.ball.xcor() > 340: # if paddle miss the ball begin the game again, increase score of paddle 2
                self.score_paddle2 += 1;
                goto_begin = True;
                winner_ = "paddle2";
                
                
            if self.ball.xcor() == -330 and ((self.paddles.paddle2.ycor()-50 )<= self.ball.ycor() and self.ball.ycor() <= (self.paddles.paddle2.ycor()+50)):
                self.ball.paddle_bounce(); # bounce when ball hits the second paddle
                
            elif self.ball.xcor() < -340: #if paddle miss the ball begin the game again, increase score of paddle 1
                self.score_paddle1 += 1;
                goto_begin = True;
                winner_ = "paddle1";

                
            self.writer.score_table(self.score_paddle1, self.score_paddle2); # write scores
            self.screen.update();
            
            if goto_begin == True:
                self.begin_again(winner_);
            
              
        self.screen.exitonclick();
        
    def begin_again(self, paddle): # assign a direction to the ball according to the winner 
        self.ball.goto(0,0);
        self.ball.yposition = 5;
        if paddle == "paddle1":
            self.ball.xposition = 5;
           
        else:
            self.ball.xposition = -5;
            
 
Create_Screen();
        
    
    