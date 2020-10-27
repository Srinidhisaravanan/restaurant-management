import mysqlconnect1
from steward import manager
manager=manager()
cursor1=mysqlconnect1.cnx.cursor()
def getbookedid(a,c):
        cursor=mysqlconnect1.cnx.cursor()
        cursor.execute("select bookedid from date1 where user_date='%s' and hour=%s"%(a,c))
        d=cursor.fetchall()
	
        return d

def gettablespecific(b):
        cursor=mysqlconnect1.cnx.cursor()
        cursor.execute("select tableid from r101 where no_of_seats=%s"%(b))
        tables=cursor.fetchall()
        return tables

def tableallotment(d,a,c,tableid):
        cursor=mysqlconnect1.cnx.cursor()
        cursor.execute("insert into date1(cid,user_date,hour) values(%s,'%s',%s)"%(d,a,c))
        mysqlconnect1.cnx.commit()
        cursor.execute("select max(bookedid) from date1")
        bookedlist=cursor.fetchone()
        print("list of max value of bookid",bookedlist)
        bookidvalue=bookedlist[0]
        cursor.execute("insert into tabledate values('%s',%s)"%(tableid,bookidvalue))
        mysqlconnect1.cnx.commit()
	manager.assignsteward(tableid)
	from main import User
	obj2=User()
	obj2.customer(d)

def getcidfortables(j):
	cursor1.execute("select tableid from tabledate where bookedid=%s"%(j))
        booked=cursor1.fetchone()
        return booked 
       

