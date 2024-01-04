# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 16:11:37 2021

@author: ECC
"""
from personClass import Person
#from RessClass import Reservation
class Employee(Person):
    numofemp =0
    emplist =[]
        
    def __init__(self,idd,name,SSN,password):
        super().__init__(idd,name,SSN)
        self.__password=password
        Employee.numofemp+=1
        #Employee.emplist.append([self.idd,self.name,self.SSN,self.__password])
        #Reservation.employee=(self.idd,self.name,self.SSN,self.__password)
        
    def get_password(self):
        return self.__password
    def set_password(self,new_password):
        self.__password=new_password
    
    def signIn(self,passwordEnterd):
        self.set_password(passwordEnterd)
        if passwordEnterd == self.password:
            return True
    
    def __str__(self):
        return super().__str__(),("password:{}".format(self.get_password()))
        
#emp1=Employee(1,"ahmed","123","apwe")   
#emp1=Employee(2,"adam","1q3","apede") 
#print(Employee.__str__(emp1))
