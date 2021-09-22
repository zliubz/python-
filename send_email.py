import smtplib
from email.mime.text import MIMEText
from email.header import Header
import pymysql

content = ""
conn = pymysql.connect(
    host='localhost',
    user='root',password='990108',
    database='百度新闻',
    charset='utf8')
cursor = conn.cursor()
sql = 'select * from 每日百度新闻;'
cursor.execute(sql)
result =cursor.fetchall()
sql = 'drop table 每日百度新闻;' 
cursor.execute(sql)
conn.commit()
cursor.close()
conn.close()

for item in result:
    title = '<a href="'+item[1]+'">'+item[0]+'</a><br></br>'
    content+=title



mail_host = "smtp.163.com"
mail_user = ""
mail_pass = ""

sender = ""
#receivers = []
receivers = []
#receivers=[]

title = '百度每日热搜新闻'

message = MIMEText(content, _subtype='html', _charset='utf-8')
message['From'] = "{}".format(sender)
message['To'] = ",".join(receivers)
message['Subject'] = title

smtpObj = smtplib.SMTP_SSL(mail_host,465)
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender,receivers,message.as_string())

