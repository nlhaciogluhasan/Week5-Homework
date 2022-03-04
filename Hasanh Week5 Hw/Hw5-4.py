""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : ************
###################################################
///
///
"""
#####################################################################
class Customer():
    
    def __init__(self,customer_gender,customer_name,customer_surname,customer_adress,n,customers,i):
        self.customer_gender=customer_gender
        self.customer_name=customer_name
        self.customer_surname=customer_surname
        self.customer_adress=customer_adress
        self.n=n
        self.customers=customers
        self.i=i
        self.customers=[] 
    def cust_numbers(self):
        self.n=int(input("How many customers : "))
        return self.n  
         
       
    def get_cust_info(self):
        
        
        self.customer_gender=input("MR MRS ?: ")
        self.customer_name=input("Enter Your Name : ")
        self.customer_surname=input("Enter Surname : ")
        self.customer_adress=input("Enter Adress : ")
        self.customers.append([self.customer_gender,self.customer_name,self.customer_surname,self.customer_adress])
           

        
    def __str__(self):
        print()
        print(self.customer_gender,self.customer_name,self.customer_surname)
        print(self.customer_adress)
        

class Items(Customer):
    def __init__(self,item_name,total_price,item_price,item_qty,discount,price_tobe_paid,shop_list,items,x,sub_total,count):
        self.item_name=item_name
        self.total_price=total_price
        self.item_price=item_price
        self.item_qty=item_qty
        self.discount=discount
        self.price_tobe_paid=price_tobe_paid
        self.shop_list=shop_list
        self.items=items
        self.items=[]
        self.x=x
        self.sub_total=sub_total
        self.count=count
    def get_item_info(self):
        self.count=0
        self.items=[]
        while True:         
            
            self.item_name=input("\nEnter item name: ")
            self.item_price=float(input("Enter item price : "))
            self.item_qty=float(input("How many you want?? : "))
            self.items.append([self.item_name,self.item_price,self.item_qty])
            self.count+=1
            self.x=input("Item eklemek için y degilse n bas ")
            
            if self.x=='n':
                break
        
        
    def __str__ (self):
        print("""\n                YOUR SHOPPING CARD
                ------------------------------------------------------
                                                        Total Per Item
                                                        --------------
                """)
        self.sub_total=0
        for self.i in range (self.count):
            print("""                                        
                {}           x        {}            =    $ {}                                     
                """.format(self.items[self.i][0],self.items[self.i][2],(self.items[self.i][1]*self.items[self.i][2])))
            self.sub_total=self.sub_total+self.items[self.i][1]*self.items[self.i][2]

        self.calculate_discount()
        print("""
              SUB TOTAL                                =   $ {}
              DISCOUNT                                 =   $ {}  (%{})
              ----------------------------------------------------
              TOTAL                                    =   $ {}
              """.format(self.sub_total,self.sub_total*self.discount/100,self.discount,self.sub_total-self.sub_total*self.discount/100))
        
    def calculate_discount(self):
        if self.sub_total>=4000:
            self.discount=25
        elif self.sub_total>=2000:
            self.discount=15
        elif self.sub_total<2000:
            self.discount=10
         
        
    # def shopping_cart(self):
    
            
    #def get_total_amount(self):
    #    self.price_tobe_paid=self.total_price-(self.total_price*self.discount/100)
    
person1=Items("","","","","","","","","","","")    
person0=Customer("","","","","","","")
person0.cust_numbers()



    
for i in range(person0.n):
    person0.get_cust_info()
    person1.get_item_info()
    person0.__str__()
    person1.__str__()

    
#####################################################################

