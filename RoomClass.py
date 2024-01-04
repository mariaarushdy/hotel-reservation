# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 05:18:57 2021

@author: ECC
"""
from CustomerClass import Customer
#from RessClass import Reservation
class Room:
    room_count=0
    def __init__(self,number,typee,curr_res=False):
        self.number=number
        self.typee=typee
        self.curr_res=False
        Room.room_count+=1
        #Room.roominfo=self.number,self.typee,self.curr_res
        
    def room_type(self,typee):
        if   typee==1 : return "Royal"
        elif typee==2 : return "Presidential"
        elif typee==3 : return "Suite"
        elif typee==4 : return "Bed and Breakfast"
        
    def isReserved(self):
        if self.curr_ress == True:
            return True 
        else : return False
        
    def __str__(self):
        return ("id:{0}, type:{1}, reserved:{2} "
              .format(self.number,self.room_type(self.typee),self.curr_res))
        
    def free_room(self,R):
        for x in Customer.ress(self):
            if R == Customer.ress[x]:
                Customer.ress[x].clear(x)
                self.curr_res = False 
            break
        else : print("Room Not Found")
#x=[Room(1,2),Room(2,3)]
#for i in x:
#    print(Room.__str__(i))
    
    
    
    
    
    
    
    
    
    
    