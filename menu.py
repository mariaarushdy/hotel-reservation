# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 15:01:47 2021

@author: ECC
"""
#from datafile
from RoomClass import Room
from EmployeeClass import Employee
from CustomerClass import Customer
from RessClass import Reservation
import filepickling
import exceptions
import sys
emplist=[Employee(0,"mesha",123456,"ma_1")]
roomlist=[Room(0,1,False),
          Room(1,2,False),
          Room(2,2,False),
          Room(3,3,False),
          Room(4,3,False),
          Room(5,3,False),
          Room(6,4,False),
          Room(7,4,False),
          Room(8,4,False),
          Room(9,4,False)]
custlist=[]
resslist=[] 
samble_list=[emplist,roomlist,custlist,resslist]
ressid=0
filepickling.save(samble_list)

def logIn():
    empidd = int(input("id: "))
    password = input("password: ")
    flagid= 0
    flagpas= 0
    for x in emplist:
        if empidd == x.idd:
            flagid=1
            if password == Employee.get_password(x):
                flagpas= 1
                print("login succeeded")
                menu(empidd,ressid)
                break
    if flagid == 0 :
         print("invalid id")
    try :
        if flagpas == 0 :
            raise exceptions.AccessDeniedError(" ")
    except exceptions.AccessDeniedError as e:
        print("AccessDeniedError", e.mess)

def checkauthorityToaccess():
    try:
        ps=input("password: ")
        if ps == "blabla":
            return True
        else: raise exceptions.AccessDeniedError(" ")
    except exceptions.AccessDeniedError as e:
        print("AccessDeniedError", e.mess)     

def menu(empidd,ressid):
    while(True):
        
        print("1. View all Rooms")
        print("2. Add new employee")
        print("3. View all employees")
        print("4. Delete employee by id")
        print("5. Make new reservation")
        print("6. View all reservations")
        print("7. Delete a reservation")
        print("8. Add new customer")
        print("9. View all customer")
        print("10. Delete customer by id")
        print("11. Sign Out")
        print("12. Exit and Save")
        samble_list = filepickling.load()
        flag=True
        while(flag):
            try:
                op = int(input("plz enter ur option: "))
                if op>12 :
                    raise exceptions.OptionNotExist("")
            except exceptions.OptionNotExist as e:
                print("OptionNotExist", e.mess)
            except Exception as e:
                print(e)
            else : flag = False
        #----------------------------------
        if op == 1 :
           for i,x in enumerate(roomlist):
               if x.curr_res == True:
                   continue
               else: print(Room.__str__(x))
               print("---------------------------")
        if op == 2 :
            if checkauthorityToaccess() == True:
                    print("please enter the employee info")
                    flag = True
                    while(flag):
                        try:
                            empid=int(input("Id: "))
                        except Exception as e:
                            print(e)
                        else:
                            for x in emplist:
                                if empid == x.idd:
                                    print ("id already exist")
                                    break
                                else : flag = False
                #----------------------------------
                    flag =True
                    while(flag):
                        empname=input("Name: ")
                        for x in emplist:
                            if empname == x.name:
                                flag = True
                                break
                            else : flag = False
                        try:
                            if flag == True:
                                raise exceptions.NameDuplicateError(" ")
                        except exceptions.NameDuplicateError as e:
                            print("NameDuplicateError", e.mess)
                #----------------------------------
                    empssn=int(input("SSN: "))
                    empass=input("Password: ")
                    emplist.append(Employee(empid,empname,empssn,empass))
                    print("employee add succeefully")
                    print(Employee.__str__(emplist[-1]))
                    print("")
            else : pass
         #---------------------------------
        if op == 3: 
            if checkauthorityToaccess() == True:
                for i in emplist:
                   print(Employee.__str__(i))
                   print("--------------------------")
            else : pass
        if op ==4:
            if checkauthorityToaccess() == True:
                print("please enter the id of the employee you want to delete")
                flag = False
                try:
                    delemp=int(input("Id: "))
                except Exception as e:
                        print(e)
                else:
                    if empidd == delemp :
                        print("u can't delete uself")
    
                    else:
                        for i,o in enumerate(emplist):
                            if delemp == o.idd:
                                del emplist[i]
                                flag=False
                                print("employee deleted successfully")
                                break
                            else : flag = True
                        try:
                            if flag == True:
                                raise exceptions.EmployeeNotFoundError(" ")
                        except exceptions.EmployeeNotFoundError as e:
                            print("EmployeeNotFoundError", e.mess)
            else : pass
         #--------------------------------------
        if op == 5: 
            flag = True
            try:
                custid=int(input("Custommer Id: "))
            except Exception as e:
                print(e)
            else:
                for i,x in enumerate(custlist):
                    if custid == x.idd:
                        flag=False
                        x.ress.append(ressid)
                        break
                    else : flag = True
                try:
                    if flag==True:
                        raise exceptions.CustomerNotFoundError(" ")
                except exceptions.CustomerNotFoundError as e:
                    print("CustomerNotFoundError", e.mess)
            if flag == False: 
                flagres= True
                while(flagres):
                    roomnum=int(input("room numper: "))
                    for x in roomlist:
                        if roomnum == x.number:
                            found=True
                            try: 
                                if x.curr_res == True:
                                 raise exceptions.RoomNotAvailableError(" ")
                            except exceptions.RoomNotAvailableError as e:
                                flagres = True
                                print("RoomNotAvailableError", e.mess)
                            else :
                                x.curr_res=True
                                flagres = False
                                break
                        else : flagres = True
                    try:
                        if found==False:
                            raise exceptions.RoomNotFoundError(" ")
                    except exceptions.RoomNotFoundError as e:
                        print("RoomNotFoundError", e.mess)
                duration=int(input("duration: "))
                ressid += 1
                resslist.append(Reservation(ressid,duration,roomnum,custid,empidd))    
            
                        
        #-------------------------------------
        if op == 6:
            for i in resslist:
                #x=Reservation(ressid,duration,roomnum,custid,empidd)
                print(Reservation.__str__(i))
        #-------------------------------------
        if op == 7:
            if checkauthorityToaccess() == True:
                x = True
                while(x):
                    print("please enter the id of the reservation you want to delete")
                    prs=input("to delete last reservation type last else type anything then enter the id u want to delete: ")
                    if prs == "last":
                        print("this [{0}] is the last reservation Id u can deleted now  u can enter [{0}] to delete it "
                              .format(resslist[-1].idd))
                    else :
                        flag = False
                        try:
                            delres=int(input("Id: "))
                        except Exception as e:
                                print(e)
                        else:
                            for i,o in enumerate(resslist):
                                if delres == o.idd :
                                    for x in roomlist:
                                        if o.room == x.number:
                                            x.curr_res = False
                                            x = False
                                            print("Room {0} now free".format(o.room))
                                            break
                                    del resslist[i]
                                    flag=False 
                                    x= False
                                    print("reservation deleted successfully")
                                    break
                                else : 
                                    flag = True
                                    x=False
                            try:
                                if flag == True:
                                    raise exceptions.ReservationNotFoundError(" ")
                            except exceptions.ReservationNotFoundError as e:
                                print("ReservationNotFoundError", e.mess)
            else: pass
        #-------------------------------------
        if op == 8:
            print("please enter the customer info")
            flag = True
            while(flag):
                try:
                    custid=int(input("Id: "))
                except Exception as e:
                    print(e)
                else:
                    for x in custlist:
                        if custid == x.idd:
                            print ("id already exist")
                            break
                    else : flag = False
        #----------------------------------
            flag =True
            while(flag):
                custname=input("Name: ")
                for x in custlist:
                    if custname == x.name:
                        flag = True
                        break
                else : flag = False
                try:
                    if flag == True:
                        raise exceptions.NameDuplicateError(" ")
                except exceptions.NameDuplicateError as e:
                    print("NameDuplicateError", e.mess)
        #----------------------------------
            custssn=int(input("SSN: "))
            custlist.append(Customer(custid,custname,custssn))
            print("customer add succeefully")
            print(Customer.__str__(custlist[-1]))
            print("")
        #---------------------------------- 
        if op == 9:
            for i in custlist:
               print(Customer.__str__(i))
               print("--------------------------")
        #---------------------------------- 
        if op == 11:
            logIn()
        #----------------------------------
        if op == 12:
            filepickling.save(samble_list)
            print("data saved")
            sys.exit()
        #----------------------------------
            
    
while(True):    
    logIn()    
        
     
     
     
     
     
     
     
     

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
        