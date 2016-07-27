import requests
from wtforms import Form
from wtforms import SubmitField,PasswordField,TextField,validators
cookies=None
html=''
htmlLength=0

class NameForm(Form):
    userName = TextField('student ID', [validators.DataRequired()])
    passWord = PasswordField('password', [validators.DataRequired()])
    captcha = TextField('verification code', [validators.DataRequired()])
    submit = SubmitField('Submit')


def virtualLogin(stuId,passWord,captchaCode,cook):
    prameters={"groupId":"","j_username":stuId,"j_password":passWord,"j_captcha":captchaCode,"login":"登陆"}
    r=requests.post('http://202.204.105.22/academic/j_acegi_security_check',data=prameters,cookies=cook)
    html=str(r.text)

    print(r.text)
    print(prameters)
    print(html)
    htmlLength=len(r.text)
    print(html)
    return htmlLength

def isSucceed():
    if htmlLength<2000:
        return True
    else: 
        return False

def getCaptcha():
    r = requests.get('http://202.204.105.22/academic/getCaptcha.do')
    f = open('besearch\static\c.jpg',mode='wb')
    f.write(r.content)
    print('############345435745764467474744354############')
    f.close()
    return r.cookies.get_dict()