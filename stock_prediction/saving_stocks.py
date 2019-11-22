##Code for storing the stocks into the database (model) 

from django.db import models
import array 

class stock():
    def __init__(self,name,price):
        self.name = name
        self.price = float(price)


class user(models.Model):
    user_name = models.CharField(max_length = 100)


    
class saved_stocks(models.Model):
    ##Do we need an auto updating array of stocks since we can only pull 5 stocks from the API at a time? Like this:
    STOCK_ARRAY = (
        ('1', "Stock 1"),
        ('2', "Stock 2"),
        ('3', 'Stock 3'),
        ('4', 'Stock 4'),
        ('5', 'Stock 5'),
    )
    
    stock_name = models.CharField(max_length = 50)
    stock_price = models.IntegerField()

    user_who_saved_stock = models.ForeignKey(user, on_delete = models.CASCADE)


    def add_stock(add_stock):
        STOCK_ARRAY.append(add_stock)
    def remove_stock(remove_stock):
        ##need to add array parsing to make sure the remove_stock object is actually in the saved_stock_array
        STOCK_ARRAY.remove(remove_stock)
        
    

    

    
    
    



    
    
    

