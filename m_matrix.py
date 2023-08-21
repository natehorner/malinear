# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 18:25:44 2023

@author: Nate
"""

from abc import ( ABC, abstractmethod )


"""
SOme kind of general matrix/vector object - abstract parent class to have
identity, empty, etc as types

only supporting 2d because some things aren't well defined in higher dimensions

"""

class m_matrix(ABC):

    #set in superclass __init__()    
    rows = 0
    cols = 0
    is_identity = False
    is_empty = False

    #keep transposed as a flag to easily transpose
    transposed = False
    

    #descriptor values to calculate later, but save for convenience
    metr_need_updates = True
    rank = -1
    det = -1
    
    def __init__(self, numrows,numcols):
        print("Calling superclass init")
        return
    
    def numcols(self) :
        if self.transposed == True :
            return self.rows
        return self.cols
    
    def numrows(self) :
        if self.transposed == True :
            return self.cols
        return self.rows
    
    #abstract because some instances will be read only (like identity)
    @abstractmethod 
    def setval(self,r,c,val):
        return
    
    @abstractmethod
    def getval(self,r,c):
        return -1
    
"""
identity matrix
"""
class id_matrix(m_matrix):
    
    def __init__(self,numrows,numcols):
        
        self.is_identity = True
        self.is_empty = False

        if numrows <= 0 or numcols <= 0 :
            print("Matrix creation error: row and col must be positive ints ("
                  + str(numrows) + "," + str(numcols) +")")

        #dimensions
        self.rows = numrows
        self.cols = numcols
        
        #Defaults
        self.metr_need_updates = True
        self.rank = -1
        self.det = -1
        self.transposed = False
        return
    
    def setval(self,r,c,val):
        print("setval() error Cannot set value of identity matrix!")
        return "ERROR"
    
    def getval(self,r,c):
        
        #check dimensions
        if r >= self.rows or r < 0 or c >= self.cols or c < 0 :
            print("getval() error row or col is invalid val: (" + str(r) + 
                  "," + str(c) + ") max = "+str(self.rows)+"," +str(self.cols))
        
        if r==c:
            return 1
        else:
            return 0
    
"""
empty matrix
"""
class empty_matrix(m_matrix):
    
    def __init__(self,numrows,numcols):
        
        self.is_identity = False
        self.is_empty = True

        if numrows <= 0 or numcols <= 0 :
            print("Matrix creation error: row and col must be positive ints ("
                  + str(numrows) + "," + str(numcols) +")")

        #dimensions
        self.rows = numrows
        self.cols = numcols
        
        #Defaults
        self.metr_need_updates = True
        self.rank = -1
        self.det = -1
        self.transposed = False
        return
    
    def setval(self,r,c,val):
        print("setval() error Cannot set value of empty matrix!")
        return "ERROR"
    
    def getval(self,r,c):
        
        #check dimensions
        if r >= self.rows or r < 0 or c >= self.cols or c < 0 :
            print("getval() error row or col is invalid val: (" + str(r) + 
                  "," + str(c) + ") max = "+str(self.rows)+"," +str(self.cols))
        
        return 0



    