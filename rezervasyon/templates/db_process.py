import sqlite3

con = sqlite3.connect(r"C:\Users\arifseyda\Desktop\rezervasyon_sistemi\ESXi.db")
cursor = con.cursor()

def create_table():
    cursor.execute("Create Table IF NOT EXISTS ESXi(ESXi Name TEXT, ESXi_Number INTEGER,is_checked INTEGER)")
    con.commit()

def create_value():
    for i in range(20,31):
        cursor.execute("Insert into ESXi values('ESXi{}', {}, 0)".format(i,i))
        con.commit()

def read_value():
    cursor.execute("Select * from ESXi")
    liste = cursor.fetchall()
    return liste

if __name__ == '__main__':
    #create_table()
    #create_value()
    esxi_array = read_value()
con.close()