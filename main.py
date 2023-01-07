from flask import Flask, render_template, redirect,request,flash,session
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,login_manager,login_required,login_user,logout_user,LoginManager,current_user



local_server=True

app = Flask(__name__)
app.secret_key="suhilkhan"

#app.config['SQL_ALCHEMY_DATABASE_URI']='mysql://username:password@localhost/databasename'
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:suhilkhan@localhost/ngobase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)
#connection of app with the database
#<=====Login Manager====>


login_manager=LoginManager(app)         

#this is for getting unique useraccess

login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))


class Test(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100))

class Admin(UserMixin,db.Model):
    adminid=db.Column(db.Integer,primary_key=True)
    adminname=db.Column(db.String(100))
    adminpw=db.Column(db.String(100))

class Orphan(UserMixin,db.Model):
    orphid=db.Column(db.String(100),primary_key=True)
    orphname=db.Column(db.String(100))
    orphage=db.Column(db.String(100))
    orphgender=db.Column(db.String(100))
    grdname=db.Column(db.String(100))
    grdphno=db.Column(db.String(100))
    grdaddr=db.Column(db.String(100))

class Donor(UserMixin,db.Model):
    donid=db.Column(db.String(100),primary_key=True)
    donname=db.Column(db.String(100))
    donaddr=db.Column(db.String(100))
    donphn=db.Column(db.String(100))
    donmail=db.Column(db.String(100))
    donoccu=db.Column(db.String(100))
    doninc=db.Column(db.String(100))


class Employee(UserMixin,db.Model):
    empid=db.Column(db.String(100),primary_key=True)
    empname=db.Column(db.String(100))
    empdesg=db.Column(db.String(100))
    empphn=db.Column(db.String(100))
    empsal=db.Column(db.String(100))

class Adoption(UserMixin,db.Model):
    orphid=db.Column(db.String(100),primary_key=True)
    orphname=db.Column(db.String(100))
    orphage=db.Column(db.String(100))
    orphaddr=db.Column(db.String(100))
    adopname=db.Column(db.String(100))
    adopnum=db.Column(db.String(100))
    adopaddr=db.Column(db.String(100))

class Medical(UserMixin,db.Model):
    orphid=db.Column(db.String(100),primary_key=True)
    orphname=db.Column(db.String(100))
    hosname=db.Column(db.String(100))
    disease=db.Column(db.String(100))
    billexp=db.Column(db.String(100))
    mediexp=db.Column(db.String(100))

class Inventory(UserMixin,db.Model):
    itemid=db.Column(db.String(100),primary_key=True)
    itemname=db.Column(db.String(100))
    dntname=db.Column(db.String(100))
    dntphn=db.Column(db.String(100))
















    




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/adminlogin', methods=['POST','GET'])
def adminlogin():
    if request.method=='POST':
        adminid=request.form.get('adminid')
        adminpw=request.form.get('adminpw')

        admins=Admin.query.filter_by(adminid=adminid).first()

        if admins and (admins.adminpw==adminpw):
            flash("Logged Id ","success")

            return redirect('/adminindex')
        else:
            flash("Incorrect Id or Password ","warning")
            return redirect('/adminlogin')

    return render_template('adminlogin.html')

@app.route('/adminsignup', methods=['POST','GET'])
def adminsingup():
    if request.method=='POST':
        adminid=request.form.get('adminid')
        adminname=request.form.get('adminname')
        adminpw=request.form.get('adminpw')

        idadmin=Admin.query.filter_by(adminid=adminid).first()

        if idadmin:
            flash("Admin ID already Exists","warning")
            return render_template("adminsignup.html")

        new_user=db.engine.execute(f"INSERT INTO `admin` (`adminid`,`adminname`,`adminpw`) VALUES ('{adminid}','{adminname}','{adminpw}') ")
        flash("Admin is Added Successfully","success")

    return render_template('adminsignup.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/adminindex')
def adminindex():
    return render_template('adminindex.html')

@app.route('/orphan', methods=['POST','GET'])
def orphan():
    if request.method=='POST':
        orphid=request.form.get('orphid')
        orphname=request.form.get('orphname')
        orphage=request.form.get('orphage')
        orphgender=request.form.get('orphgender')
        grdname=request.form.get('grdname')
        grdphno=request.form.get('grdphno')
        grdaddr=request.form.get('grdaddr')

        idorphan=Orphan.query.filter_by(orphid=orphid).first()

        if idorphan:
            flash("Orphan ID already Exists","warning")
            return render_template("orphan.html")

        new_user=db.engine.execute(f"INSERT INTO `orphan` (`orphid`,`orphname`,`orphage`,`orphgender`,`grdname`,`grdphno`,`grdaddr`) VALUES ('{orphid}','{orphname}','{orphage}','{orphgender}','{grdname}','{grdphno}','{grdaddr}') ")
        flash("Orphan is Added Successfully","success")
    
    allorphans=Orphan.query.all()


    return render_template('orphan.html',allorphans=allorphans)


@app.route('/donor', methods=['POST','GET'])
def donor():
    if request.method=='POST':
        donid=request.form.get('donid')
        donname=request.form.get('donname')
        donaddr=request.form.get('donaddr')
        donphn=request.form.get('donphn')
        donmail=request.form.get('donmail')
        donoccu=request.form.get('donoccu')
        doninc=request.form.get('doninc')

        iddonor=Donor.query.filter_by(donid=donid).first()

        if iddonor:
            flash("Orphan ID already Exists","warning")
            return render_template("donor.html")

        new_user=db.engine.execute(f"INSERT INTO `donor` (`donid`,`donname`,`donaddr`,`donphn`,`donmail`,`donoccu`,`doninc`) VALUES ('{donid}','{donname}','{donaddr}','{donphn}','{donmail}','{donoccu}','{doninc}') ")
        flash("Donor is Added Successfully","success")

    alldonor=Donor.query.all()


    return render_template('donor.html',alldonor=alldonor)



@app.route('/employee', methods=['POST','GET'])
def employee():
    if request.method=='POST':
        empid=request.form.get('empid')
        empname=request.form.get('empname')
        empdesg=request.form.get('empdesg')
        empphn=request.form.get('empphn')
        empsal=request.form.get('empsal')

        idemp=Employee.query.filter_by(empid=empid).first()

        if idemp:
            flash("Employee ID already Exists","warning")
            return render_template("employee.html")

        new_user=db.engine.execute(f"INSERT INTO `employee` (`empid`,`empname`,`empdesg`,`empphn`,`empsal`) VALUES ('{empid}','{empname}','{empdesg}','{empphn}','{empsal}') ")
        flash("Employee is Added Successfully","success")
        
    allemployee=Employee.query.all()

    return render_template('employee.html',allemployee=allemployee)


@app.route('/adoption', methods=['POST','GET'])
def adoption():
    if request.method=='POST':
        orphid=request.form.get('orphid')
        orphname=request.form.get('orphname')
        orphage=request.form.get('orphage')
        orphaddr=request.form.get('orphaddr')
        adopname=request.form.get('adopname')
        adopnum=request.form.get('adopnum')
        adopaddr=request.form.get('adopaddr')

        nameorph=Adoption.query.filter_by(orphname=orphname).first()

        if nameorph:
            flash("Orphan Is Already Adopted","warning")
            return render_template("adoption.html")

        new_user=db.engine.execute(f"INSERT INTO `adoption` (`orphid`,`orphname`,`orphage`,`orphaddr`,`adopname`,`adopnum`,`adopaddr`) VALUES ('{orphid}','{orphname}','{orphage}','{orphaddr}','{adopname}','{adopnum}','{adopaddr}') ")
        flash("Adoptor is Added Successfully","success")

    alladop=Adoption.query.all()


    return render_template('adoption.html',alladop=alladop)

@app.route('/medical', methods=['POST','GET'])
def medical():
    allmedi=Medical.query.all()
    if request.method=='POST':
        orphid=request.form.get('orphid')
        orphname=request.form.get('orphname')
        hosname=request.form.get('hosname')
        disease=request.form.get('disease')
        billexp=request.form.get('billexp')
        mediexp=request.form.get('mediexp')

        idorph=Medical.query.filter_by(orphid=orphid).first()

        new_user=db.engine.execute(f"INSERT INTO `medical` (`orphid`,`orphname`,`hosname`,`disease`,`billexp`,`mediexp`) VALUES ('{orphid}','{orphname}','{hosname}','{disease}','{billexp}','{mediexp}') ")
        flash("Medical Data is Added Successfully","success")

    return render_template('medical.html',allmedi=allmedi)

@app.route('/inventory', methods=['POST','GET'])
def inventory():
    allinv=Inventory.query.all()
    if request.method=='POST':
        itemid=request.form.get('itemid')
        itemname=request.form.get('itemname')
        dntname=request.form.get('dntname')
        dntphn=request.form.get('dntphn')

        iditem=Inventory.query.filter_by(itemid=itemid).first()

        if iditem:
            flash("Item Is Already Present","warning")
            return render_template("Inventory.html")

        new_user=db.engine.execute(f"INSERT INTO `inventory` (`itemid`,`itemname`,`dntname`,`dntphn`) VALUES ('{itemid}','{itemname}','{dntname}','{dntphn}') ")
        flash("Item Data is Added Successfully","success")


    return render_template('inventory.html',allinv=allinv)


@app.route('/eedit/<string:empid>',methods=['POST','GET'])
def eedit(empid):
    employee=Employee.query.filter_by(empid=empid).first()

    if request.method=='POST':
        empid=request.form.get('empid')
        empname=request.form.get('empname')
        empdesg=request.form.get('empdesg')
        empphn=request.form.get('empphn')
        empsal=request.form.get('empsal')
        db.engine.execute(f"UPDATE `employee` SET `empid` ='{empid}',`empname`='{empname}',`empdesg`='{empdesg}',`empphn`='{empphn}',`empsal`='{empsal}' WHERE `empid`='{empid}'")
        flash("Emplpyee Updated","info")
        return redirect("/employee")

    return render_template('eedit.html',employee=employee)


@app.route('/edelete/<string:empid>',methods=['POST','GET'])
def edelete(empid):

    db.engine.execute(f"DELETE FROM `employee` WHERE `empid`='{empid}'")
    flash("Data Deleted","danger")
    return redirect("/employee")



@app.route('/oedit/<string:orphid>',methods=['POST','GET'])
def oedit(orphid):
    orphans=Orphan.query.filter_by(orphid=orphid).first()

    if request.method=='POST':
        orphid=request.form.get('orphid')
        orphname=request.form.get('orphname')
        orphage=request.form.get('orphage')
        orphgender=request.form.get('orphgender')
        grdname=request.form.get('grdname')
        grdphno=request.form.get('grdphno')
        grdaddr=request.form.get('grdaddr')
        db.engine.execute(f"UPDATE `orphan` SET `orphid` ='{orphid}',`orphname`='{orphname}',`orphage`='{orphage}',`orphgender`='{orphgender}',`grdname`='{grdname}',`grdphno`='{grdphno}',`grdaddr`='{grdaddr}' WHERE `orphid`='{orphid}'")
        flash("Orphan Details Updated","info")
        return redirect("/orphan")

    return render_template('oedit.html',orphans=orphans)


@app.route('/odelete/<string:orphid>',methods=['POST','GET'])
def odelete(orphid):

    db.engine.execute(f"DELETE FROM `orphan` WHERE `orphid`='{orphid}'")
    flash("Data Deleted","danger")
    return redirect("/orphan")

@app.route('/test')
def test():
    try:
        a = Test.query.all()
        print(a)
        return f'database is connected'

    except Exception as e:
        print(e)
        return f'My database is not connected {e}'



if __name__=="__main__":
    app.run(debug=True)     