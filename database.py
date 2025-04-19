#Database operations(CRUD)
import pymysql
class crud:
    def __init__(self):
        self.con=pymysql.connect(host='localhost',user='root',password='*****',db='my_db')
        print("Connect to db succesfull!")
    def add(self,id,name,age):
        q="insert into student values({0},'{1}',{2})".format(id,name,age)
        cur=self.con.cursor()
        c=cur.execute(q)
        self.con.commit()
        cur.close()
        print("Data saved!" if c!=0 else 'Failed')
    def edit(self,id,age):
        q="update student set age={0} where id={1}".format(age,id)
        cur=self.con.cursor()
        c=cur.execute(q)
        self.con.commit()
        cur.close()
        print("Data saved!" if c!=0 else 'Failed')
    def delete(self,id):
        q="delete from student where id={0}".format(id)
        cur=self.con.cursor()
        c=cur.execute(q)
        self.con.commit()
        cur.close()
        print("Data deleted!"if c!=0 else 'Failed')
    def view(self):
        q="select * from student"
        cur=self.con.cursor()
        cur.execute(q)
        r=cur.fetchall()
        for i in r:
            for j in i:
                print(j,end="\t")
            print("\n")
    def cancel(self):
        print("App closed!")
        self.con.close()