# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:11:02 2017

@author: casari
"""

def OpenValve(valve):
    print("Open: " + str(valve))
    
def CloseValve(valve):
    print("Close: " + str(valve))
    
    
    
    
    
if __name__ == '__main__':              # if we're running file directly and not importing it
    OpenValve(1)
    CloseValve(2)