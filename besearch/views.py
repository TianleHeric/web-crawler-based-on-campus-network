"""
Routes and views for the flask application.
"""

from besearch import app
from datetime import datetime
from flask import render_template
from flask import request
from besearch import htmlpaser
from besearch import login

@app.route('/',methods=['GET','POST'])
@app.route('/home',methods=['GET','POST'])
def home():
    """Renders the home page."""
    if request.method == "GET":
        login.cookies=login.getCaptcha()
    form = login.NameForm(request.form)
    print('###########################################')
    print(login.cookies)
    if form.validate():
        userId = form.userName.data
        passWord = form.passWord.data
        verificationCode = form.captcha.data
        login.htmlLength=login.virtualLogin(userId,passWord,verificationCode,login.cookies)
        if login.isSucceed():
            return render_template('layout.html',title='login successfully')
        print('******************************************')
    return render_template(
        'index.html',
        title='My Blog Home Page',
        year=datetime.now().year,
        message='your home page.',
        form=form       
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""

    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about',methods=['GET','POST'])
def about():
    """Renders the about page."""
    print(type(request.form))
    sForm=htmlpaser.serarchForm(request.form)
    if request.method=="GET":
        print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
        pass
    if request.method=="POST":
        buildInfor=sForm.building.data
        weekInfor=sForm.weekTime.data
        dayInfor=sForm.dayTime.data
        print(buildInfor,weekInfor,dayInfor)
        htmlForSchedule=htmlpaser.getHtml(buildInfor,weekInfor,dayInfor,login.cookies)

        if buildInfor=="80":
            table= htmlpaser.getTableZonghelou(htmlForSchedule)
            return render_template(
            'zonghelou.html',
            building='综合楼',
            title='about',
            year=datetime.now().year,
            message='Your application description page.',
            tb=table,
            weekInfor=weekInfor,
            dayInfor=dayInfor
        )

        if buildInfor=="1021":           #tecbuilding
            table=htmlpaser.getTableKeyanlou(htmlForSchedule)
            return render_template(
            'zonghelou.html',
            building='科研楼',
            title='about',
            year=datetime.now().year,
            message='Your application description page.',
            tb=table,
            weekInfor=weekInfor,
            dayInfor=dayInfor
        )

        if buildInfor=="164":#jiaoyilou
            table=htmlpaser.getTableJiaoyilou(htmlForSchedule)
            return render_template(
            'zonghelou.html',
            building='教一楼',
            title='about',
            year=datetime.now().year,
            message='Your application description page.',
            tb=table,
            weekInfor=weekInfor,
            dayInfor=dayInfor
        )

        if buildInfor=="10":
            table=htmlpaser.getTableShijiulou(htmlForSchedule)
            return render_template(
            'zonghelou.html',
            building='十九楼',
            title='about',
            year=datetime.now().year,
            message='Your application description page.',
            tb=table,
            weekInfor=weekInfor,
            dayInfor=dayInfor
        )


        if buildInfor=='126':
            table= htmlpaser.getTableJiaowulou(htmlForSchedule)
            return render_template(
            'zonghelou.html',
            building='教五楼',
            title='about',
            year=datetime.now().year,
            message='Your application description page.',
            tb=table,
            weekInfor=weekInfor,
            dayInfor=dayInfor
        )


    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        form=sForm,
        message='Your application description page.'
    )

