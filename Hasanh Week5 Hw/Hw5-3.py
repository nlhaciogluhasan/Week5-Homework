""""
Date : 22.02.2022
Prepared by the Program : Hasan
Name Of The Program : ************
###################################################


///
"""
#####################################################################

class Product :
    def __init__(self,product_id='',product_name='',product_purchase_price=int,product_sale_price=int):
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price
    
    
    
    def set_remarks(self,margin):
        self.margin=margin
        if (self.product_sale_price-self.product_purchase_price)>0:
            self.margin='Profit'
        else:
            self.margin='Loss'
        
    
    
    def set_details(self):
        self.product_id=input("Enter Product Id : ")
        self.product_name=input("Enter Product Name : ")
        self.product_purchase_price=float(input("Enter Product Purchase Price : "))
        self.product_sale_price=float(input("Enter Product Sale Price : "))
        
        self.set_remarks('')
    
    def get_details(self):
        print("""
            Product Id : {}
            Product Name  : {}
            Product Purchase Price   : ${}
            Product Sale Price  : ${}
            Product Profit Margin : {} - You {}ed ${} per unit from this product!
               """.format(self.product_id,self.product_name,self.product_purchase_price,self.product_sale_price,self.margin,self.margin,abs(self.product_sale_price-self.product_purchase_price)  ))
    
    
person=Product("",'','',"")
person.set_details()
person.get_details()
#####################################################################