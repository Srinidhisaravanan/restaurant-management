import sys
import mysql.connector
cnx=mysql.connector.connect(user='user02',passwd='Tata@1234',host='127.0.0.1',database='group6')
cursor=cnx.cursor()
cursor.execute("SELECT Order_Id FROM OrderedList")
r=cursor.fetchall()
for x in r:
        a=x[0]
        a=a+1
        #print a
class Order:
        def __init__(self):
                self.choices={
                                1:self.chicken_biryani,
                                2:self.panner_biryani,
                                3:self.chicken_tikka,
                                4:self.paneer_tikka,
                                5:self.billgeneration,
                                6:self.quit
                             }
		
        def disp(self):
                print("                 *******************************************************************************                 ")
                print("                                         1.CHICKEN BIRYANI			-150")
                print("                                         2.PANNER BIRYANI			-120")
                print("                                         3.CHICKEN TIKKA			-90")
                print("                                         4.PANEER TIKKA				-70")
                print("                                         5.GENERATE BILL                						 ")
                print("                                         6.QUIT                         						 ")
                print("                 *******************************************************************************                 ")
        def run(self):
		global CusId
		CusId=input("ENTER YOUR BOOKING ID TO PLACE ORDER : ")
                while True:
                        self.disp()
                        choice=input("ENTER YOUR CHOICE : ")
                        a1=self.choices.get(choice)
                        if a1:
                       		 a1()
                        else:
                                print("{0} is not a valid choice".format(choice))
 	def chicken_biryani(self):
                num=input("ENTER THE QUANTITY : ")
		if self.update("chicken_biryani")==0:
			pass
		else:
                	#CusId=input("ENTER YOUR CUSTOMER ID TO PLACE ORDER : ")
                	global a
                	cursor.execute("SELECT Id FROM Item WHERE Name='Chicken Biryani'")
                	d=cursor.fetchone()
                	for i in d:
                	         ItemId=i
                	cursor.execute("SELECT Name FROM Item WHERE Id=1")
                	e=cursor.fetchone()
                	for j in e:
                	       Item_Name=j
                	cursor.execute("SELECT Price FROM Item WHERE Id=1")
                	f=cursor.fetchone()
                	for k in f:
                	        Price=k
                	sql=("INSERT INTO OrderedList(Order_Id,Quantity,Item_Name,ItemId) VALUES(%s,%s,%s,%s)")
                	val=(a,num,Item_Name,ItemId)
                	cursor.execute(sql,val)
                	cnx.commit()
                	sql1=("INSERT INTO Orders(Order_Id,Cus_Id,Price)VALUES(%s,%s,%s)")
                	val1=(a,CusId,Price)
                	cursor.execute(sql1,val1)
                	cnx.commit()
                	print(" Order of {} chicken biryani is taken ".format(num))
        def panner_biryani(self):
                num=input("ENTER THE QUANTITY : ")
		if self.update("paneer_biryani")==0:
			pass
		else:	
		
			global CusId
                     	#CusId=input("ENTER YOUR CUSTOMER ID TO PLACE ORDER : ")
                	global a
                	cursor.execute("SELECT Id FROM Item WHERE Name='Paneer Biryani'")
                	d=cursor.fetchone()
                	for i in d:
                        	ItemId=i
                	cursor.execute("SELECT Name FROM Item WHERE Id=2")
                	e=cursor.fetchone()
                	for j in e:
                        	Item_Name=j
                	cursor.execute("SELECT Price FROM Item WHERE Id=2")
                	f=cursor.fetchone()
                	for k in f:
                        	Price=k
                	sql=("INSERT INTO OrderedList(Order_Id,Quantity,Item_Name,ItemId) VALUES(%s,%s,%s,%s)")
                	val=(a,num,Item_Name,ItemId)
 			cursor.execute(sql,val)
                	cnx.commit()
                	sql1=("INSERT INTO Orders(Order_Id,Cus_Id,Price) VALUES(%s,%s,%s)")
                	val1=(a,CusId,Price)
                	cursor.execute(sql1,val1)
                	cnx.commit()
                	print(" Order of {} panner biryani is taken ".format(num))
        def chicken_tikka(self):
                num=input("ENTER THE QUANTITY : ")
		if self.update("chicken_tikka")== 0:
			pass
		else:	
			#CusId=input("ENTER YOUR CUSTOMER ID TO PLACE ORDER : ")
                	global a
                	cursor.execute("SELECT Id FROM Item WHERE Name='Chicken Tikka'")
                	d=cursor.fetchone()
                	for i in d:
                        	ItemId=i
                	cursor.execute("SELECT Name FROM Item WHERE Id=3")
                	e=cursor.fetchone()
                	for j in e:
                        	Item_Name=j
                	cursor.execute("SELECT Price FROM Item WHERE Id=3")
                	f=cursor.fetchone()
                	for k in f:
                        	Price=k
                	sql=("INSERT INTO OrderedList(Order_Id,Quantity,Item_Name,ItemId) VALUES(%s,%s,%s,%s)")
                	val=(a,num,Item_Name,ItemId)
                	cursor.execute(sql,val)
                	cnx.commit()
                	sql1=("INSERT INTO Orders(Order_Id,Cus_Id,Price) VALUES(%s,%s,%s)")
                	val1=(a,CusId,Price)
                	cursor.execute(sql1,val1)
                	cnx.commit()
                	print(" Order of {} chicken tikka is taken ".format(num))
        def paneer_tikka(self):
                num=input("ENTER THE QUANTITY : ")
		if self.update("paneer_tikka")== 0:
                	pass
		else:
                	#CusId=input("ENTER YOUR CUSTOMER ID TO PLACE ORDER :")
                	global a
                	cursor.execute("SELECT Id FROM Item WHERE Name='Paneer Tikka'")
                	d=cursor.fetchone()
                	for i in d:
                        	ItemId=i
                	cursor.execute("SELECT Name FROM Item WHERE Id=4")
                	e=cursor.fetchone()
                	for j in e:
				Item_Name=j
                	cursor.execute("SELECT Price FROM Item WHERE Id=4")
                	f=cursor.fetchone()
                	for k in f:
                        	Price=k
                	sql=("INSERT INTO OrderedList(Order_Id,Quantity,Item_Name,ItemId) VALUES(%s,%s,%s,%s)")
                	val=(a,num,Item_Name,ItemId)
                	cursor.execute(sql,val)
                	cnx.commit()	
                	sql1=("INSERT INTO Orders(Order_Id,Cus_Id,Price) VALUES(%s,%s,%s)")
                	val1=(a,CusId,Price)
                	cursor.execute(sql1,val1)
                	cnx.commit()
                	print(" Order of {} panner tikka is taken ".format(num))
	def billgeneration(self):
		from steward import manager
		manager=manager()
		manager.billgeneration(a,CusId)
	def compensation(self,total):
		from steward import manager
		manager=manager()
		print(" \n 3 - Excellent \n 2 - Average \n 1 - Poor	")
		b=input(" \n ENTER YOUR FEEDBACK :  ")
		if b == 1:
			compensation = 0.02*total
			print("DUE TO POOR FEEDBACK WE WOULD LIKE TO PROVIDE YOU A COMPENSATION OF 2PERCENT OF THE BILL AMOUNT")
			return compensation
		else:
			return 0
	def update(self,var):
		sql=("SELECT availability FROM Menu where itemname='%s'"%(var))
		cursor.execute(sql)
		d=cursor.fetchall()
		if d[0][0]=='un available':
			print("SORRY! AT PRESENT IT IS NOT AVAILABLE ")
			return 0
		else:
			return 1			
	def quit(self):
                global a
                a=a+1
                print("                                         THANK YOU                                               ")
		from main import User
		user1=User()
                user1.customer(CusId)

if __name__=='__main__':
        o=Order()
        o.run()
