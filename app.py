from flask import Flask,render_template,request,session,g,redirect,url_for,flash
import os,pandas as pd
app=Flask(__name__)
app.secret_key="123"
app.config['file']='static/excel'
app.config['image']='static/image'
class User:
    def __init__(self,id,username,password):
        self.id=id
        self.username=username
        self.password=password

users=[]
users.append(User(id=1,username='Dinesh',password='123'))
users.append(User(id=2,username='Surya',password='123')) 
@app.route('/', methods=['GET','POST'])
def login():
    if request.method=='POST':
        uname=request.form.get('username')
        password=request.form.get('pass')
        for data in users:
            if data.username==uname and data.password==password:
                session['user_id']=data.id
                g.user=data.username
                k=1
                flash("Login Successful",'success')
                return render_template('home.html')
            else:
                k=0
        if k!=1:
            flash("Incorrect Username and Password",'danger') 
    return render_template('login.html')
@app.route('/Logout')
def logout():
    if session:
        session.clear
        return redirect(url_for('login'))
@app.route('/upload',methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
        excel=request.files['excel']
        path1=os.path.join(app.config['file'],excel.filename)
        name,ext=os.path.splitext(path1)
        if ext=='.xlsx':
            excel.save(path1)
            flash('File uploaded successfully','success')
            data=pd.read_excel(excel)
            return render_template('login.html',data=data.to_html())
        else:
            flash('Upload file in correct format','danger')
    return render_template('login.html')

@app.route('/image',methods=['GET', 'POST'])
def image():
    if request.method=='POST':
        image=request.files['img']
        path2=os.path.join(app.config['image'],image.filename)
        image.save(path2)
        flash('Image uploaded successfully','success')
    return render_template('home.html',image=path2)


if __name__=='__main__':
    app.run(debug=True)
