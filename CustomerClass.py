# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 17:59:28 2021

@author: ECC
"""

from personClass import Person
#from RessClass import Reservation
class Customer(Person):
    numofcss=0
    def __init__(self,idd,name,SSN):
        super().__init__(idd,name,SSN)
        self.ress=[]
        #Reservation.customer=(self.idd,self.name,self.SSN,self.ress)
        Customer.numofcss+=1
        
    def addReservation(self,res):
            self.ress.append(res)
    
    def __str__(self):
        return super().__str__(),("reservations:{}".format(self.ress))


#cust_1 = Customer(1,"ahmed","332")
#cust_2 = Customer(2,"ahmed","332")
#Customer.addReservation(cust_1,1)

#Customer.addReservation(cust_2,3)
#Customer.addReservation(cust_1,2)
#print(Customer.__str__(cust_1))
#print(Customer.__str__(cust_2))
