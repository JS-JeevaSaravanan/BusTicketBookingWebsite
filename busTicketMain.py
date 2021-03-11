from flask import *
import sqlite3


app=Flask(__name__)

qa=[]

qw=''

@app.route('/',methods=['GET','POST'])

def log():
    global qw,qa
    if request.method== 'GET':
        return render_template("log.html")

    else:

        # check username and jpass
        
        ve=request.form.get("email")
        vp= request.form.get("pass")

        q3 = "select * from t where e='{}' and p='{}'";
        kr = sqlite3.connect("E:\\jeeva\\HOD project\\update\\jeeva\\newww\\db1.db")
        s = kr.execute(q3.format(ve, vp))
        kr.commit()

        p=''
        for i in s:
            p=p+str(i)
        if(len(p)>1):
            qw=qw+ve
            #print(qw)
            return render_template("res.html")

        else:
            return render_template("log.html")


@app.route('/reg',methods=['GET','POST'])

def reg():
    if request.method== 'GET':
        return render_template("reg.html")
    else:
        # store username and func

        v1=request.form.get("name")
        v2 = request.form.get("email")
        v3 = request.form.get("pass")
        v4 =""

        q3 = "insert into t values ('{}','{}','{}','{}')";
        kr = sqlite3.connect("E:\\jeeva\\HOD project\\update\\jeeva\\newww\\db1.db")
        s = kr.execute(q3.format(v1,v2,v3,v4))
        kr.commit()

        return render_template("log.html")


@app.route('/res',methods=['GET','POST'])

def res():
    if request.method== 'GET':
        return render_template("res.html")
    else:
        return "lo"



@app.route('/plane',methods=['GET','POST'])

def plane():
    if request.method== 'GET':

        q3 = "select s from t";
        kr = sqlite3.connect("E:\\jeeva\\HOD project\\update\\jeeva\\newww\\db1.db")
        s = kr.execute(q3.format(qw))
        kr.commit()
        ts=''
        for t in s:
            p=str(t)

            for h in range(2,len(p)-3):
                #print(p[h],end="")
                ts=ts+p[h]

        #print(ts)

        mo=ts.split('#')
        mo.pop()

        print(mo)

        we=[]
        for u in mo:
            we.append(int(u))
        print(we)

        de=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']


        for bb in range(len(de)):
            if bb in we:
                de[bb-1]="disabled"

        print(de)


        return render_template("plane.html",bc=de)

    else:
        # store username and func

        selected = request.form.getlist('seat')
        #qa=[]

        qa.extend(selected)


        return render_template("book.html")


@app.route('/track',methods=['GET','POST'])

def track():
    if request.method== 'GET':
        q3 = "select s from t where e='{}'";
        kr = sqlite3.connect("E:\\jeeva\\HOD project\\update\\jeeva\\newww\\db1.db")
        s = kr.execute(q3.format(qw))
        kr.commit()
        mb=''
        for t in s:
            mb=str(t)
            break
        print(mb)
        nm=str(mb)
        gg=''
        for y in range(2,len(nm)-3):
            gg=gg+str(nm[y])

        bk=gg.split('#')
        vv=[]
        for mv in range(len(bk)-1):
            vv.append(bk[mv])

        return render_template("track.html",bl=vv)
    else:
        return "lo"



@app.route('/book',methods=['GET','POST'])

def book():
    if request.method== 'GET':
        return render_template("book.html")
    else:
        #print(qa)
        x=''
        for mb in qa:
            x=x+mb+"#"

        #print(x)
        #print(qw)

        q3 = """update t 
                set s='{}'
                where e='{}';"""


        kr = sqlite3.connect("E:\\jeeva\\HOD project\\update\\jeeva\\newww\\db1.db")
        s = kr.execute(q3.format(x,qw))
        kr.commit()
        return render_template("tku.html")


'''
##########
global k;
k=[]

j=['','','','']

q3 = "select sst from t1";
kr = sqlite3.connect("db1.db")
s = kr.execute(q3)
kr.commit()

for k in s:
    print(s)

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def g():
    if request.method== 'GET':
        return render_template("s1.html",a=j)
    else:
        selected = request.form.getlist('seat')
        k.extend(selected)
        return render_template("x1.html")


@app.route('/bk',methods=['GET','POST'])

def h():
    if request.method== 'GET':
        return render_template("x1.html")
    else:
        m=''
        print("hii")
        for i in k:
            m=m+i+"#"

        print(m)

        o=m.split("#")

        print(o)

        return "booked"



'''


if __name__=="__main__":
   app.debug=True
   app.run()





