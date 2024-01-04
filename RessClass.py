# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 12:11:55 2021

@author: ECC
"""
import datetime

class Reservation():
    ressCnt=0
    def __init__(self,idd,duration,room,customer,employee):
        Reservation.ressCnt +=1
        self.idd=idd
        self.date_created=datetime.date.today()
        self.duration=duration
        self.room=room
        self.customer=customer
        self.employee=employee
        
    def __str__(self):
        return ("id:{0} , date created:{1}, duration:{2}, room:{3}, customerID:{4}, employeeID:{5}"
                .format(self.idd,self.date_created,self.duration,self.room,self.customer,self.employee))
