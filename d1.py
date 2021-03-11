import sqlite3


'''
q3="select *  from t1 where u1='{}' and p1='{}'"
kr=sqlite3.connect("db1.db")
s=kr.execute(q3.format("u1","p1"))
kr.commit()

for i in s:
        break
'''
con=sqlite3.connect("E:\jeeva\HOD project\JEEVA\jeeva\newww\demodb.db")
s=con.execute("""create table t (
        n text,
        e text,
        p text,
        s text
)""")

con.close()
'''
for i in s:
        print("printing")
        print(i)

'''       