from collections import defaultdict
from order import Order
o=Order()
global total1
global sid1
import mysql.connector
import datetime
cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
cursor=cnx.cursor()
class manager:
	def insert_seats(self,table_id,no_of_seats):
        	cursor.execute("insert into r101 values(%s,%s);"%(table_id,no_of_seats))
       		cnx.commit()
	def delete_seats(self,no_of_seats):
        	cursor.execute("select max(tableid) from r101 where no_of_seats=%d group by no_of_seats;"%(no_of_seats))
        	value=cursor.fetchall()
        	cursor.execute("delete from r101 where tableid=%s;"%(value[0][0]))
        	cnx.commit()
	def viewdetails(self):
		print("1.View Steward details")
		print("2.View BookedTable details")
		print("3.View Bill details")
		print("4.View Table")
		v=input("Enter your Option : ")
		if v==1:
			cursor.execute("select * from steward")
			no=cursor.fetchall()
			for i in no:
				print(i)
		elif v==2:
			cursor.execute("select * from date1 ")
			no=cursor.fetchall()
			for i in no:
				print(i)
		elif v==3:
			cursor.execute("select * from bill")
			no=cursor.fetchall()
			for i in no:
				print(i)
		else:
        		cursor.execute("select * from r101")
        		list_all=cursor.fetchall()
        		f=open('seat_details.txt','w')
        		f.write('Table Id         |    No. Of Seats \n')
        		for l in list_all:
                		for element in l:
                        		f.write("   ")
                      		  	f.write(str(element)+"                  ")
                		f.write("\n")
        		f.close()
        		fo=open('seat_details.txt','r')
        		variable=fo.read()
        		fo.close()
        		print variable
	        	cnx.commit()
	def assignsteward(self,tableno):
		s=[]
		cursor.execute("select *from steward")
		self.steward=cursor.fetchall()
		for i in self.steward:
			s1=[]
			for j in i:
				s1.append(j)
			s.append(s1)
		for i in s:
			sid1=i[0]	
			if  i[1]==None and i[2]==None:
				i[1]=tableno			
				cursor.execute("update steward set table1='%s' where sid=%s"%(i[1],sid1))
				cnx.commit()
				cursor.execute("update date1 d join tabledate d1 on d.bookedid=d1.bookedid set d.sid=%s where d1.tableid=%s"%(sid1,i[1]))
				cnx.commit()
				print("steward assigned")
				break
			elif i[2]==None:
				i[2]=tableno
				cursor.execute("update steward set table2='%s' where sid=%s"%(i[2],sid1))
				cnx.commit()
				cursor.execute("update date1 d join tabledate d1 on d.bookedid=d1.bookedid set d.sid=%s where d1.tableid=%s"%(sid1,i[2]))
				cnx.commit()
				print("steward assigned")
				break
			else:
				print("no vacant steward")
				pass
	def updatesteward(self,bookedid,billno):
		cursor.execute("select s.sid,t.tableid from steward s,tabledate t,date1 d where t.bookedid=d.bookedid and s.sid=d.sid and d.bookedid=%s"%(bookedid))
		details=cursor.fetchall()
		print(details)
		cursor.execute("select table1,table2 from steward where sid=%s"%(details[0][0]))
		tableid=cursor.fetchall()
		print(tableid)
		if tableid[0][0]==details[0][1]:
			cursor.execute("update steward set table1=NULL where sid=%s"%(details[0][0]))
			cnx.commit()
		elif tableid[0][1]==details[0][1]:
			cursor.execute("update steward set table2=NULL where sid=%s"%(details[0][0]))
			cnx.commit()
		else:
			pass
	def billgeneration(self,orderid,bookid):
		date1=datetime.datetime.now().date()
		time1=datetime.datetime.now().time()
		print(orderid)
		cursor.execute("select o.ItemId,o.Quantity,i.Price,i.Name from OrderedList o,Item i where o.ItemId=i.Id and o.Order_id=%s"%(orderid))
		details=cursor.fetchall()
		print(details)
		total1=0
		for i in details:
			total1=total1+(i[1]*i[2])
		compensation=o.compensation(total1)
		total=total1-compensation
		print("Date: {0},\nTime: {1}".format(str(date1),str(time1)))	
		print "Billno:",orderid
		for i in details:
			print("{0}=={1}*{2}".format(i[3],i[1],i[2]))
		print "Amount={0}".format(total1)
		print "Compensation={0}".format(compensation)
		print "Totalamount={0}".format(total)
		cursor.execute("insert into bill values(%s,%s,%s)"%(orderid,bookid,total))
		cnx.commit()
		self.updatesteward(bookid,orderid)
if  __name__=='__main__':
		m=manager()
		#m.assignsteward(2)
		#m.viewdetails()
		#m.updatesteward(2,49)
		#m.billgeneration(5,6)
