import sqlite3
class population:

    def __init__(self,rt='',s=0,p=0,r=0,t=0,a=1800,name='',age='',gender='',mobile='',email='',tribe='',origin='',address=''):

        print("\n\n__________________________________________________")
        print ("        WELCOME TO National Population Commission   ")
        print("_____________________________________________________\n")

        
        self.rt=rt

        self.r=r

        self.t=t

        self.p=p

        self.s=s
        self.a=a
        self.name=name
        self.address=address
        self.age=age
        self.gender=gender
        self.mobile=mobile
        self.email=email
        self.tribe=tribe
        self.origin=origin


    def inputdata(self):
        self.name=input("\nEnter your full name: ")
        self.age=input("\nEnter your age: ")
        self.gender=input("\nEnter your gender: ")
        self.mobile=input("\nEnter your mobile number: ")
        self.email=input("\nEnter your Email Address: ")
        self.address=input("\nEnter your resident address: ")
        self.tribe=input("\nEnter your tribe: ")
        self.origin=input("\nEnter your state of origin: ")
                
 
    def display(self):
        print ("******National Population Commission******")
        print ("Customer details: ")
        print ("Customer name: ",self.name)
        print ("Customer age: ",self.age)
        print ("Customer mobile number: ",self.mobile)
        print ("Customer email address: ",self.email)
        print ("Customer address: ",self.address)
        print ("Customer tribe: ",self.tribe)
        print ("Customer state of origin: ",self.origin)


def Database():
        conn = sqlite3.connect("population.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `popul` (mem_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT, age TEXT, gender TEXT, tribe TEXT, origin TEXT address TEXT, mobile TEXT)")
        cursor.execute("SELECT * FROM `popul` ORDER BY `name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()



   
            

        

        

def main():

    a=population()
    

    while (1):
        print("***********************")
        print("       Main Menu ")
        print("***********************\n")
        
        print("1. Enter Customer Data")
        
        print("2. Update Customer Data")

        print("3. Search Customer Dat")

        print("4. Delete Customer Data")

        print("5. Show total")

        print("6. EXIT")

        b=int(input("\nEnter your choice: "))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.updatedata()
        
        if (b==3):
            a.searchdata()

        if (b==4):
            a.deletdata()

        if (b==5):

            a.display()

        if (b==6):

            quit()


main()

