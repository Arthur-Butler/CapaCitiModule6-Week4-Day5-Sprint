#!/usr/bin/env python
# coding: utf-8

# In[17]:


#importing pymongo
import pymongo
#connecting to database
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
#Inputing sprint 3 data
mydb = myclient["DataTracker"]
mycol = mydb["stock"]
mylist = [
  { "Items": "Chips", "ItemAmount": 120},             
  { "Items": "Cooldrink", "ItemAmount": 81}, 
  { "Items": "Chocolates", "ItemAmount": 150}, 
  { "Items": "Pies", "ItemAmount": 90}, 
  { "Items": "Fruit", "ItemAmount": 160}, 
  { "Items": "Cupcakes", "ItemAmount": 50}, 
  { "Items": "Veggies", "ItemAmount": 80}
]
x = mycol.insert_many(mylist)

mycol = mydb["veggies"]
mylist_veggies = [
  { "Brand_Name": "Carrot", "Stock_Amount": 10},             
  { "Brand_Name": "Potato", "Stock_Amount": 20},  
  { "Brand_Name": "Squash", "Stock_Amount": 15},   
  { "Brand_Name": "Pumpkin", "Stock_Amount": 15},  
  { "Brand_Name": "Cabbage", "Stock_Amount": 20}  
]
x = mycol.insert_many(mylist_veggies)

mycol = mydb["pies"]
mylist_pies = [
  { "Brand_Name": "Steak and Kidney", "Stock_Amount": 10},             
  { "Brand_Name": "Pepper Steak", "Stock_Amount": 15},  
  { "Brand_Name": "Roast Chicken", "Stock_Amount": 15},   
  { "Brand_Name": "Chicken and Mushroom", "Stock_Amount": 10},  
  { "Brand_Name": "Apple", "Stock_Amount": 10},  
  { "Brand_Name": "Pepper Steak", "Stock_Amount": 20},  
  { "Brand_Name": "Steak", "Stock_Amount": 10}  
]
x = mycol.insert_many(mylist_pies)

mycol = mydb["fruit"]
mylist_fruit = [
  { "Brand_Name": "Apple", "Stock_Amount": 20},             
  { "Brand_Name": "Pear", "Stock_Amount": 20},  
  { "Brand_Name": "Oranges", "Stock_Amount": 15},   
  { "Brand_Name": "Lemon", "Stock_Amount": 15},  
  { "Brand_Name": "Tangerine", "Stock_Amount": 40},  
  { "Brand_Name": "Tomato", "Stock_Amount": 20},  
  { "Brand_Name": "Pineapple", "Stock_Amount": 20}, 
  { "Brand_Name": "Strawberries", "Stock_Amount": 10}
]
x = mycol.insert_many(mylist_fruit)

mycol = mydb["cupcakes"]
mylist_cupcakes = [
  { "Brand_Name": "Chocolate", "Stock_Amount": 20},             
  { "Brand_Name": "Vanilla", "Stock_Amount": 10},  
  { "Brand_Name": "Sprinkles", "Stock_Amount": 10},   
  { "Brand_Name": "Caramel", "Stock_Amount": 10}  
]
x = mycol.insert_many(mylist_cupcakes)

mycol = mydb["cooldrinks"]
mylist_cooldrinks = [
  { "Brand_Name": "Fanta", "Stock_Amount": 20},             
  { "Brand_Name": "Sprite", "Stock_Amount": 10},  
  { "Brand_Name": "Coke", "Stock_Amount": 10},   
  { "Brand_Name": "Pepsi", "Stock_Amount": 10},  
  { "Brand_Name": "Stoney", "Stock_Amount": 10},  
  { "Brand_Name": "Ginger Ale", "Stock_Amount": 10},  
  { "Brand_Name": "Appletiser", "Stock_Amount": 11} 
]
x = mycol.insert_many(mylist_cooldrinks)

mycol = mydb["chocolates"]
mylist_chocolates = [
  { "Brand_Name": "Tex", "Stock_Amount": 20},             
  { "Brand_Name": "Kit Kat", "Stock_Amount": 20},  
  { "Brand_Name": "Crunchie", "Stock_Amount": 20},   
  { "Brand_Name": "Astros", "Stock_Amount": 20},  
  { "Brand_Name": "Flakes", "Stock_Amount": 20},  
  { "Brand_Name": "Lindt", "Stock_Amount": 20},  
  { "Brand_Name": "Whispers", "Stock_Amount": 20}, 
  { "Brand_Name": "Beacon Marshmellow Eggs", "Stock_Amount": 10}
] 
x = mycol.insert_many(mylist_chocolates)

mycol = mydb["chips"]
mylist_chips = [
  { "Brand_Name": "Lays", "Stock_Amount": 20},             
  { "Brand_Name": "Fritos", "Stock_Amount": 30},  
  { "Brand_Name": "Doritos", "Stock_Amount": 20},   
  { "Brand_Name": "Cheese Curls", "Stock_Amount": 10},   
  { "Brand_Name": "Flings", "Stock_Amount": 10},  
  { "Brand_Name": "Simba Chips", "Stock_Amount": 20}, 
  { "Brand_Name": "Pringles", "Stock_Amount": 10}
] 
x = mycol.insert_many(mylist_chips)


# In[20]:


#Creating top product collection
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")

mycol = mydb["TopProducts"]
mylist_topprod = [
  { "Brand_Name": "Tangerine", "Stock_Amount": 30},             
  { "Brand_Name": "Fritos", "Stock_Amount": 30},  
  { "Brand_Name": "Cabbage", "Stock_Amount": 20}]
x = mycol.insert_many(mylist_topprod)

    


# In[21]:


#Sorting documents in descending order by stock or item amount
myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
mycol=mydb["stock"]
mydoc=mycol.find().sort("ItemAmount",-1)
for x in mydoc:
    print(x)


# In[23]:


#deleting documents
myclient=pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
mycol=mydb["pies"]
myquery={"Brand_Name": "Apple"}
mycol.delete_one(myquery)
for x in mycol.find():
    print(x)
    
mycol=mydb["chocolates"]
myquery={"Brand_Name": "Beacon Marshmellow Eggs"}
mycol.delete_one(myquery)
for x in mycol.find():
    print(x)


# In[24]:


#updating top products
myclient=pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")
mycol=mydb["TopProducts"]

myquery = { "Brand_Name": "Tangerine", "Stock_Amount": 30 }
newvalues = { "$set": {"Stock_Amount": 40} }

mycol.update_one(myquery, newvalues)


# In[27]:


import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/?readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false")

mycol = mydb["stock"]

myresult = mycol.find().sort("ItemAmount",-1).limit(5)
for x in myresult:
  print(x)


# In[ ]:




