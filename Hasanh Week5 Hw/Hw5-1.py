""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : Society Class
###################################################

"""
#####################################################################


from mimetypes import init
from tkinter import E


class Society:
    def __init__(self,society_name,house_no_of_mem,flat,income):
        self.society_name=society_name
        self.house_no_of_mem=house_no_of_mem
        self.flat=flat
        self.income=income
    
    
    def input_data(self):
        self.society_name=input("Enter the name of the society : ")
        self.house_no_of_mem=input("Enter the number of members : ")
        self.income=float(input("Enter your income : "))
        
    def allocate_flat(self):
         if self.income>=25000:
             self.flat='A Type'          
         elif 20000<=self.income<25000:
             self.flat='B Type'         
         elif 15000<=self.income<20000:
             self.flat='C Type'           
         elif self.income<15000:
             self.flat='D Type'
        
    
    def show_data(self):
         print("""
                
               Society Name     : {}
               Number of Members: {}
               Income           : {}
               Flat             : {}
               
               """.format(self.society_name,self.house_no_of_mem,self.income,self.flat)  )
    
person=Society('','','','')
person.input_data()
person.allocate_flat()
person.show_data()
#####################################################################



