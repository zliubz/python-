import os
import schedule
import time
pathdownload = r' C:\Users\Administrator\Desktop\autodownloadnews.py'
pathsend = r' C:\Users\Administrator\Desktop\send_email.py'
def send():
    global pathdownload,pathsend
    os.system('python'+ pathdownload)
    time.sleep(120)
    os.system('python'+ pathsend)


schedule.every().day.at("08:00").do(send)

while True:
    schedule.run_pending()
    time.sleep(20)