# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 19:16:33 2023

@author: Timot
"""
import pandas as pd

class define_columns_rows:
    
    def __init__(self):
        self
    def prompt_user_input(self):
        column_num = input("How many columns will the table have? ")
        response = []
        for i in range(0,int(column_num)):
            column_name = input("Give the name for column " + str(i + 1) + " " )
            response.append(column_name)
        print(response)
        return response
    def __call__(self):
        self.prompt_user_input()
        
        

I2D = define_columns_rows()
I2D()