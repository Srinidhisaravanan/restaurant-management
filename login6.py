from termcolor1 import *
import re
import sys
import mysql.connector
from random import *
from getpass import getpass
cid=0
class loginpage:
        def customer(self):
		from main import User
		obj3=User()
                cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
                cursor=cnx.cursor()
		print blue 
		print("       WELCOME TO DEVINE DINING       ")
		print red
                print"***************************************"
		print blue
                print("         1.Login")
                print("         2.Sign Up")
                print("         3.Manager Login")
                print("         4.Chef Login")
		print("	 5.Quit")
		print red
		print("**************************************")
		print reset		
                a=input("enter your choice:")
                if a==1:
                        c=self.cust_login()
			obj3.user(c)
                elif a==2:
                        self.signup()
                elif a==3:
                        m=self.managerlogin()
			obj3.user(m)
                elif a==4:
                        ch= self.chef_login()
			obj3.user(ch)
		elif a==5:
			sys.exit(0)
                else:
                        print("invalid choice!")
			print("please enter a valid choice!")
			self.customer()

        def managerlogin(self):
                cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
                cursor=cnx.cursor()
                managerid=[]
                t=[]
		print("****************************************")
                a=raw_input("enter the manager id of manager6:")
                q=("select * from manager6 where mid=%s"%a)
                cursor.execute(q)
                t=cursor.fetchall()
                for i in t:
                        for j in i:
                                managerid.append(str(j))
                if a not in managerid:
                        print("the managerid doesnot exist")
                        self.customer()
		else:

                        password=getpass("enter your password:")
                        abc=("select password from manager6 where mid=%s"%a)
                        cursor.execute(abc)
                        t=cursor.fetchall()
                        for i in t:
                                if i in t:
                                        print("login sucessfull")
					return [1,2]
                                else :
                                        print ("wrong password")
                        self.customer()
        def chef_login(self):
                cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
                cursor=cnx.cursor()
                chefid=[]
                t=[]
		print("**************************************")
                a=raw_input("enter the chef id:")
                q=("select * from chef6 where chefid=%s"%a)
                cursor.execute(q)
                t=cursor.fetchall()
                for i in t:
                        for j in i:
                                chefid.append(str(j))
                if a not in chefid:
                        print("the chefid doesnot exist")
                        self.customer()
                else:
                        password=getpass("enter your password:")
                        abc=("select password from chef6 where chefid=%s"%a)
                        cursor.execute(abc)
                        t=cursor.fetchall()
                        for i in t:
                                if i in t:
                                        print("login sucessfull")
					return [001,3]
                                else :
                                        print ("wrong password")
                        self.customer()

	def cust_login(self):
                cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
                cursor=cnx.cursor()
                count=0
                c=[]
		print("****************************************")
                loginid=raw_input("enter user id:")
                q=("select userid from customer6")
                cursor.execute(q)
                t=cursor.fetchall()
                for i in t:
                        for j in i:
                                c.append(str(j))
                if loginid not in c:
                                print ("user does not exist")
                                ans1=raw_input("Do you want to signup? y/n")
                                if(ans1.lower()=='y'):
					print("SIGN UP")
                                        self.signup()
                                elif(ans1.lower()=='n'):
                                        exit()
                                else:
                                        print("invalid input")
                                        exit()
              	else:
                                while count<3:
                                        p1=getpass("enter password")
                                        count=count+1

                                        abc=("select password from customer6 where userid='%s'"%(loginid))
                                        cursor.execute(abc)
                                        t=cursor.fetchone()
                                        if p1==t[0]:
                                                print "successful login"
                                                cursor.execute("select cid from customer6 where userid='%s'"%(loginid))
                                                global cid
                                                cid=int(cursor.fetchall()[0][0])
                                                return [cid,1]
                                                break
 					else:
                                                print"wrong password"
		

        def signup(self):
                cnx=mysql.connector.connect(user='user02',password='Tata@1234',host='127.0.0.1',database='group6')
                cursor=cnx.cursor()
                print("welcome to devine dining!!")
		print("***************************************")
                name=raw_input("enter name:")
                contact=raw_input("enter contact:")
                address=raw_input("enter your address:")
                gender=raw_input("gender:")
                mailid=raw_input("enter mailid:")
                userid=raw_input("enter user id of characters and atleast 1 special character:")
                while(1):
                        password=getpass("enter password containing atleast one special character with minimum length of 8 characters:")
                        if len(password)<8:
                                 print "password is less than 8 characters"

                        elif re.search('[!@#$%&*?]',password)is None:
                                print "there is no special character"
                        else:	
				count=0
                                while(count<3): 
					pd=getpass("confirm password")
                                	if pd==password:
                                        	print "password created"
                                        	query=("insert into customer6(name,contact,address,gender,mailid,userid,password) values('%s','%s','%s','%s','%s','%s','%s')"%(name,contact,address,gender,mailid,userid,password))
                                        	cursor.execute(query)
                                        	cnx.commit()
						ans=raw_input("login? y/n ")
			                	if ans.lower()=='y':
							print("LOGIN")
                        				self.cust_login()
                				elif ans.lower()=='n':
                       					 print"THANK YOU"
							 break
						else:
							 print("please select another option:")
							 self.customer()
                               		else:
                                        	print "password does not match,retype the password"
              					count=count+1
	#	print("please select another option")
	 # ans=raw_input("login? y/n")
                #if ans=='y':
                 #       self.cust_login()
	#	elif ans=='n':
         #               print"thank you"
	#	self.customer()
if __name__=='__main__':
        l=loginpage()
        l.customer()    
