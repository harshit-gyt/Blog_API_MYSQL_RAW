from flask import *
import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='gytworkZ@71', database='DB1')
cur=mydb.cursor()
#cur.execute('CREATE TABLE blog(name  varchar(10), email varchar(20), blog varchar(50) )')
mydb.cursor()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('adduser.html')

@app.route("/GET", methods=['GET'])
def get():
    l1=[]
    s = 'select * from blog'
    cur.execute(s)
    result = cur.fetchall()
    for e in result:
        data= {"name": e[0],"email" : e[1], "blog" : e[2]}
        l1.append(data)
    return {"userinfo":l1}


@app.route("/POST", methods=['POST'])
def post_user():
    cur = mydb.cursor()
    uname = request.form['uname']
    email = request.form['email']
    blog = request.form['blog']

    s = "insert into blog(name, email, blog) values (%s, %s, %s)"
    v=(uname,email,blog)
    cur.execute(s,v)
    mydb.commit()

    return redirect("/GET")


@app.route("/DELETE/<string:name>")
def delete_user(name):
    cur = mydb.cursor()
    uname = name
    s="DELETE FROM blog WHERE name= (%s)"
    v=uname
    cur.execute(s,(v,))
    mydb.commit()

    return {"Status": 200 }


if __name__=="__main__":
    app.run(debug=True)





