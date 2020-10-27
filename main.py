from customer import Customer 
c2=Customer()
from login6 import loginpage
c4=loginpage()
class User:
        def user(self,list1):
        	#l1=loginpage()
        	#list1=l1.customer()
        	if list1[1]==1:
                        cid=list1[0]
                        self.customer(cid)
                elif list1[1]==2:
                        self.manager()
                elif list1[1]==3:
                        self.chef()
                else:
                        from login6 import loginpage
                        signup=loginpage()
                        signup.customer()	

	def customer(self,cid):
                from order import Order
                c3=Order()
                print("1.reserve tables")
                print("2.order food")
		print("3.back to login")
                r=input("enter your choice")
                if r==1:
                        c2.selectrest(cid)
                elif r==2:
                        c3.run()
                else:
                        c4.customer()	
	def manager(self):
		from steward import manager
		m1=manager()
		r=0
		while(r<=3):
			print("1.View Details")
			print("2.Add Tables")
			print("3.Delete Tables")
			r=input("enter your choice")
			if r==1:
                m1.viewdetails()
			elif r==2:
                no_of_seats=input("ENTER THE NUMBER OF SEATS")
                tableid=input("ENTER THE TABLE ID")
                m1.insert_seats(tableid,no_of_seats)
            elif r==3:
                no_of_seats=input("ENTER NUMBER OF SEATS TO DELETE")
                m1.delete_seats(no_of_seats)
            else:
                c4.customer()
    def chef(self):
        from chef import Chef
        chef=Chef()
		chef.viewtables()
		c4.customer()
			
if __name__=="__main__":
	u=User()
	u.user()

