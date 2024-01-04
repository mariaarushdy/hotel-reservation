# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 13:38:56 2021

@author: ECC
"""
import pickle
def save(oject):
    try:
        file = open("fileforpro","Wb+")
        pickle.dump(oject,file)
        file.close()
        print("file saved")
    except:
        print("save faild")
        
def load():
    try:
        file = open("fileforpro","rb")
        oject = pickle.laod(file)
        file.close()
        print("file loaded")
        return oject
    except:
        print("load faild")
        return []
    
        