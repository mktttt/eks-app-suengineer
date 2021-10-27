#-*- coding:utf-8 -*-
from flask import render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import os 
from dotenv import load_dotenv


import secrets
import member_cal
from flask import Flask

app = Flask(__name__)

load_dotenv()



secret_key= secrets.token_hex(16)
app.secret_key = secret_key

app.config['MYSQL_HOST'] = os.environ.get("MYSQL_HOST")
app.config['MYSQL_USER'] = os.environ.get("MYSQL_USER")
app.config['MYSQL_PASSWORD'] = os.environ.get("MYSQL_PASSWORD")
app.config['MYSQL_DB'] = os.environ.get("MYSQL_DB")
app.config['MYSQL_PORT'] = int(os.environ.get("MYSQL_PORT"))

# Intialize MySQL
mysql = MySQL(app)

location_type=''
@app.route('/')
def index():
    return render_template('index.html')





@app.route('/corona_moim')
def corona_moim():
  

    coronaWarninglevel=request.args.get('사회적거리두기단계')
    moimN=request.args.get('모임인원')
    vaccineN=request.args.get('백신2차접종2주경과인원')
    
    
    result_app=member_cal.cal_moim(coronaWarninglevel,moimN,vaccineN)

    return render_template('corona_moim.html',result=result_app)



@app.route('/location_search')
def location_search():
    

   
    location_type = request.args.get('location_type')
    # MySQL DB에 해당 계정 정보가 있는지 확인
    
   
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT 비고 FROM location WHERE 구분 = %s',(location_type,))
    location_type_notice = cursor.fetchall()
    if len(location_type_notice)!=0:
        print(location_type_notice)
        print(type(location_type_notice))
        location_type_notice=location_type_notice[0]
        location_type_notice=location_type_notice['비고']
    # 값이 유무 확인 결과값 변수로 넣기
    
    
        notice_app = location_type_notice
    else:
        notice_app = '종류를 골라주십시오 '

    return render_template('location_search.html', notice=notice_app, location=location_type)
if __name__ == '__main__':
    app.run('0.0.0.0', port=80, debug=True)
