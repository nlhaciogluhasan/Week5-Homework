""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : ************
###################################################
///

///
"""
#####################################################################
from asyncio.windows_events import NULL


class ItemInfo:
    def __init__(self,item,item_code=0,price=NULL,qty=NULL,discount=NULL,net_price=NULL):
        self.item_code=item_code
        self.item=item
        self.price=price
        self.qty=qty
        self.discount=discount
        self.net_price=net_price
        
    def calculate_discount(self):
        if self.qty<=10:
            self.discount=0
        elif 11<=self.qty<=20:
            self.discount=15
        elif self.qty>=20:
            self.discount=20
            
        self.net_price=self.price*self.qty-(self.price*self.qty*self.discount/100)   
              
        
    def buy(self):
        self.item_code=input("Enter item code : ")
        self.item=input("Enter the item name : ")
        self.price=float(input("Enter the unit price of the item : "))
        self.qty=int(input("How many {}s will you purchase? : ".format(self.item)))   
        
        self.calculate_discount()
        
    
    def show_all(self):
        print("""
            Item Code : {}
            Item Name  : {}
            Item Unit Price   : ${}
            Item Quantity : {}
            Discount : You saved $ {} , ({}%) today!
            Total : ${}
               """.format(self.item_code,self.item,self.price,self.qty,(self.price*self.qty-self.net_price),self.discount,self.net_price)  )
        
person=ItemInfo('','','','','','')
person.buy()
person.show_all()
#####################################################################
    
    
        
        
        
        
        

        