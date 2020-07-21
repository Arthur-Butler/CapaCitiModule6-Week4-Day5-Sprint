#Importing bar graph utils from pandas
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt
import numpy as np
#Importing pandas for dataframe
import pandas as pd
#Importing DataFrame from pandas import
from pandas import DataFrame
#Importing mysql.connector to connect to database
import mysql.connector
#Establishin database connection
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1738art",
    database="sprintdb"
)
#Creatin cursor to navigate database
mycursor=mydb.cursor()
#Fetchin columns from database using SQL
mycursor.execute("SELECT `stock`.`ItemAmount` FROM stock")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y=[]
for row in ItemAmount:
    y.extend(row)
print(y)
mycursor.execute("SELECT `stock`.`Items` FROM stock")
Items=mycursor.fetchall()
x=[]
for row in Items:
    x.extend(row)
print(x)    
y_pos=np.arange(7)
#Diplaying data viually using a bar graph
plt.bar(y_pos, y, align='center', alpha=1)
plt.xticks(y_pos, x)
plt.ylabel('Stock Amount')
plt.xlabel('Item Category')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT `chips`.`Stock Amount` FROM chips")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y1=[]
for row in ItemAmount:
    y1.extend(row)
print(y1)
mycursor.execute("SELECT `chips`.`Brand_Name` FROM chips")
Items=mycursor.fetchall()
x1=[]
for row in Items:
    x1.extend(row)
print(x1)    
y_pos=np.arange(len(x1))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y1, align='center', alpha=1)
plt.xticks(y_pos, x1)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT cooldrinks.Stock_Amount FROM cooldrinks")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y2=[]
for row in ItemAmount:
    y2.extend(row)
print(y2)
mycursor.execute("SELECT Brand_Name FROM cooldrinks")
Items=mycursor.fetchall()
x2=[]
for row in Items:
    x2.extend(row)
print(x2)    
y_pos=np.arange(len(x2))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y2, align='center', alpha=1)
plt.xticks(y_pos, x2)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT chocolates.Stock_Amount FROM chocolates")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y3=[]
for row in ItemAmount:
    y3.extend(row)
print(y3)
mycursor.execute("SELECT Brand_Name FROM chocolates")
Items=mycursor.fetchall()
x3=[]
for row in Items:
    x3.extend(row)
print(x3)    
y_pos=np.arange(len(x3))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y3, align='center', alpha=1)
plt.xticks(y_pos, x3)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT cupcakes.Stock_Amount FROM cupcakes")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y4=[]
for row in ItemAmount:
    y4.extend(row)
print(y4)
mycursor.execute("SELECT Brand_Name FROM cupcakes")
Items=mycursor.fetchall()
x4=[]
for row in Items:
    x4.extend(row)
print(x4)    
y_pos=np.arange(len(x4))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y4, align='center', alpha=1)
plt.xticks(y_pos, x4)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT fruit.Stock_Amount FROM fruit")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y5=[]
for row in ItemAmount:
    y5.extend(row)
print(y5)
mycursor.execute("SELECT Brand_Name FROM fruit")
Items=mycursor.fetchall()
x5=[]
for row in Items:
    x5.extend(row)
print(x5)    
y_pos=np.arange(len(x5))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y5, align='center', alpha=1)
plt.xticks(y_pos, x5)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT pies.Stock_Amount FROM pies")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y6=[]
for row in ItemAmount:
    y6.extend(row)
print(y6)
mycursor.execute("SELECT Brand_Name FROM pies")
Items=mycursor.fetchall()
x6=[]
for row in Items:
    x6.extend(row)
print(x6)    
y_pos=np.arange(len(x6))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y6, align='center', alpha=1)
plt.xticks(y_pos, x6)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()

mycursor.execute("SELECT veggies.Stock_Amount FROM veggies")
ItemAmount=mycursor.fetchall()
#Placing data in lists
y7=[]
for row in ItemAmount:
    y7.extend(row)
print(y7)
mycursor.execute("SELECT Brand_Name FROM veggies")
Items=mycursor.fetchall()
x7=[]
for row in Items:
    x7.extend(row)
print(x7)    
y_pos=np.arange(len(x7))
#Diplaying data viually using a bar graph
plt.bar(y_pos, y7, align='center', alpha=1)
plt.xticks(y_pos, x7)
plt.ylabel('Stock Amount')
plt.xlabel('Brand')
plt.title('Amount of stock for each item in a category')
plt.show()
