import mysqlconnect1
import datetime
import time
import random
import mysqlfunctions1
from steward import manager
import mysql.connector
manager=manager()
class Customer:
	def selectrest(self,cid):
                cursor=mysqlconnect1.cnx.cursor()
                cursor.execute("select rlocation from restaurant")
                loc=cursor.fetchall()
                for i in loc:
                        print(i)
                location1=raw_input('enter the location')
                str(location1)
                cursor.execute("select * from restaurant where rlocation='%s'"%(location1))
                t=cursor.fetchall()
                #print(t)
                restdetails=[]
                for i in t:
                        for j in i:
                                restdetails.append(str(j))
                print restdetails
                riddetails=[]
                #print('select a restaurant id ')
                restaurantid=raw_input('enter the restaurant id')
                str(restaurantid)
                print('restaurantid',restaurantid)
                cursor.execute("select rid from restaurant where rid='%s'"%(restaurantid))
                d=cursor.fetchall()
                riddetails=d[0][0]
                print(riddetails)
                if riddetails:
                        cursor.execute("select distinct  no_of_seats from %s"%(riddetails))
                        b=cursor.fetchall()
                print('available seat number details',b)
                print('select one seat number from above')
                self.action(cid)
	def action(self,d):
		from main import User
		user=User()
        	a=raw_input('enter the date in YYYY-MM-DD')
        	b=input('enter the number of seats required')
	        c=input('enter the hour at which table is required')

        	year,month,day=map(int,a.split('-'))
        	user_date=datetime.date(year,month,day)
        	print("printing user date",user_date)
        	today=datetime.date.today()
        	margin=datetime.timedelta(days=7)
        	print("printing margin",today+margin)
        	if today<=user_date<=today+margin:
        	    tablesval=[]
       		    print("booking")
       		    d1=mysqlfunctions1.getbookedid(a,c)
            	    print("printing d",d1)
           	    #cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
          	    #cursor=cnx.cursor()
		    #cursor=mysqlconnect1.cnx.cursor()
         	    #cursor.execute("select bookid from date1 where user_date='%s' and hour=%s"%(a,c))
         	    #cid1=cursor.fetchall()
		    #print(cid1)
        	    if not d1:
                	print('hi')
                	tables=mysqlfunctions1.gettablespecific(b)
                	print("list of all tables",tables)
                	for i in tables:
                	    for j in i:
                	        tablesval.append(j)
                	print("printing tables val",tablesval)
                	tableid=random.choice(tablesval)
                	print("table id of 1st vacancy table",tableid)
                	mysqlfunctions1.tableallotment(d,a,c,tableid)	
 		    else:
                	tablesbooked=[]
                	tablesforseats=[]
			booked=[]
               		print("printing d",d)
                	for i in d1:
                    		for j in i:
                        		booked.append(mysqlfunctions1.getcidfortables(j))
                       	print("booked",booked)
			for i in booked:
				for j in i:
					tablesbooked.append(j)
                	print("printing tables booked",tablesbooked)
                	alltables=mysqlfunctions1.gettablespecific(b)
                	for i in alltables:
                    		for j in i:
                       			tablesforseats.append(j)
                	print("printing all tables for noofseats",tablesforseats)
                	tablesavailable=list(set(tablesforseats)-set(tablesbooked))
                	print("tables available",tablesavailable)
                	if not tablesavailable:
                    		print("no vacancy")
				user.customer(d)
				
                	else:
                    		tablesval=random.choice(tablesavailable)
                    		print("table id of 1st vacany table",tablesval)
                    		mysqlfunctions1.tableallotment(d,a,c,tablesval)	
       		else:
           		print("can not book greater than 7")
			user.customer(d)
if __name__=="__main__":
	obj1=Customer()
	obj1.selectrest()
