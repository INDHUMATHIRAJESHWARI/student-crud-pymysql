#Console intreface
import database
try:
    db=database.crud()
    while True:
        print("\n\n DashBoard")
        print("1. Insert\n2. View\n3. Edit\n4. Delete\n0. Close")
        ch=int(input("Enter choice : "))
        if ch==1:
            print("\n Student Registration Form")
            i=int(input("Enter id : "))
            n=input("Enter name : ")
            a=int(input("Enter age : "))
            db.add(i,n,a)
        elif ch==2:
            print("\n Registered Student Data")
            db.view()
        elif ch==3:
            print("\n Student Updation Form")
            i=int(input("Enter id : "))
            a=int(input("Enter age : "))
            db.edit(i,a)
        elif ch==4:
            print("\nStudent Removal Form")
            i=int(input("Enter id : "))
            db.delete(i)
        elif ch==0:
            db.cancel()
            break
        else:
            print("\n Invalid Choice")
except Exception as e:
    print("\n Error ~ ",e)
