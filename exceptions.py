# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 16:43:45 2021

@author: ECC
"""
class NameDuplicateError(RuntimeError):
    def __init__(self, mess):
        self.mess = mess
class OptionNotExist(RuntimeError):
    def __init__(self, mess):
        self.mess = mess
class EmployeeNotFoundError(RuntimeError):
     def __init__(self, mess):
        self.mess = mess
class ReservationNotFoundError(RuntimeError):
     def __init__(self, mess):
        self.mess = mess
class RoomNotFoundError(RuntimeError):
     def __init__(self, mess):
        self.mess = mess
class RoomNotAvailableError(RuntimeError):
     def __init__(self, mess):
        self.mess = mess
class CustomerNotFoundError(RuntimeError):
     def __init__(self, mess):
        self.mess = mess
class AccessDeniedError(RuntimeError):
     def __init__(self, mess):
        self.mess = mess

