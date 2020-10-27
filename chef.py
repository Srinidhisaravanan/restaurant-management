import mysql.connector
cx=mysql.connector.connect(host='127.0.0.1',user='user02',password='Tata@1234',database='group6')
xx=cx.cursor()
xx.execute("select max(Order_Id) from OrderedList")
sds=xx.fetchall()
sw=sds[0][0]
class Chef:
        def orders(self):
                xx.execute("select Quantity,Item_Name from OrderedList where Order_Id=%s"%sw)
                i=xx.fetchall()
                v1,v2=zip(*i)
                return (v2)
        def __init__(self):
                self.switcher ={
                         "Chicken Biryani":self.chicken_biryani,
                         "Chicken Tikka":self.chicken_tikka,
                         "Paneer Biryani":self.panner_biryani,
                         "Paneer Tikka":self.panner_tikka
                         }
        def run(self,v2):
                for j in v2:
                        action=self.switcher.get(j)
                        if action:
                                action()
                        else:
                                break
        def chicken_biryani(self):
                xx.execute("select material,quantity from Raw where material in ('chicken','oil','rice','spices')")
                i=xx.fetchall()
                xx.execute("select Quantity from OrderedList where Item_Name ='Chicken Biryani'and Order_Id=%s"%sw)
                r=xx.fetchall()
                ii=int(r[0][0])
                if (i[0][1]>=ii and i[1][1]>=ii and i[2][1]>=ii and i[3][1]>=ii):
                        xx.execute("update Menu set availability='avilable' where itemname='chicken_biryani'")
                        xx.execute("update Raw set quantity=(quantity - %s) where material in ('chicken','oil','rice','spices')" %ii)
                        cx.commit()
                else:
                        xx.execute("update Menu set availability='un avilable' where itemname='chicken_biryani'")
                        self.purchase()
                        cx.commit()
	def chicken_tikka(self):
                xx.execute("select material,quantity from Raw where material in ('chicken','oil','spices')")
                i=xx.fetchall()
                xx.execute("select Quantity from OrderedList where Item_Name ='Chicken Tikka'and Order_Id=%s"%sw)
                r=xx.fetchone()
                for x in r:
                        z=x
                if (i[0][1]>=z and i[1][1]>=z and i[2][1]>=z):
                        xx.execute("update Menu set availability='avilable' where itemname='chicken_tikka'")
                        xx.execute("update Raw set quantity=(quantity - %s) where material in ('chicken','oil','spices')" %z)
                        cx.commit()
                else:
                        xx.execute("update Menu set availability='un available' where itemname='chicken_tikka'")
                        self.purchase()
                        cx.commit()
        def panner_biryani(self):
                xx.execute("select material,quantity from Raw where material in ('paneer','oil','rice','spices')")
                i=xx.fetchall()
                xx.execute("select Quantity from OrderedList where Item_Name ='Paneer Biryani'and Order_Id=%s"%sw)
                rr=xx.fetchall()
                iii=int(rr[0][0])
                if (i[0][1]>=iii and i[1][1]>=iii and i[2][1]>=iii and i[3][1]>=iii):
                        xx.execute("update Menu set availability='avilable' where itemname='paneer_biryani'")
                        xx.execute("update Raw set quantity=(quantity - %s) where material in ('paneer','oil','rice','spices')" %iii)
                        cx.commit()
                else:
                        xx.execute("update Menu set availability='un available' where itemname='paneer_biryani'")
                        self.purchase()
                        cx.commit()
        def panner_tikka(self):
                xx.execute("select material,quantity from Raw where material in ('paneer','oil','spices')")
                i=xx.fetchall()
                xx.execute("select Quantity from OrderedList where Item_Name ='Paneer Tikka'and Order_Id=%s"%sw)
                r=xx.fetchall()
                i4=int(r[0][0])
                if (i[0][1]>=i4 and i[1][1]>=i4 and i[2][1]>=i4):
                        xx.execute("update Menu set availability='avilable' where itemname='paneer_tikka'")
                        xx.execute("update Raw set quantity=(quantity - %s) where material in ('paneer','oil','spices')" %i4)
                        cx.commit()
		else:
                        xx.execute("update Menu set availability='un available' where itemname='paneer_tikka'")
                        self.purchase()
                        cx.commit()
        def purchase(self):
                xx.execute("update Raw set quantity=100 where material in ('chicken','oil','spices','paneer','rice') and  quantity<=0")
        def viewtables(self):
		se=0
		while se<=2:
               		print(" *************************************************************** \n 1 - To view Raw table \n 2 - To view Menu table")
                	se=input("enter your choice")
            	    	if(se==1):
                	        xx.execute("select * from Raw ")
                        	jj=xx.fetchall()
                        	for i in jj:
                        	        print(i)
                	elif(se==2):
                        	xx.execute("select * from Menu")
                        	jj=xx.fetchall()
                        	for i in jj:
                                	print(i)
                	else:
                        	print("invalid entry")
		return 0
		
if __name__=="__main__":
        abc=Chef()
        sd=abc.orders()
        abc.run(sd)
	abc.viewtables()

