# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:03:05 2021

@author: ECC
"""

class Person:
    def __init__(self,idd,name,SSN):
        self.idd=idd
        self.name=name
        self.SSN=SSN
        
    def __str__(self):
        return ("id:{0}, name:{1}, SSN:{2} "
              .format(self.idd,self.name,self.SSN))