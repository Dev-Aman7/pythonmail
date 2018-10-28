import smtplib
import serial
import time# if you have not already done so
ser = serial.Serial('com16', 9600)

li=["a8285443826@gmail.com","mittalsankalp1810@gmail.com"]
while (True):
    t2=ser.readline().strip().decode("utf-8")
    print(t2)
    if(t2=="mail"):
        for i in range(len(li)):
            s=smtplib.SMTP('smtp.gmail.com',587)
            s.starttls()
            s.login("a8285443826@gmail.com","Rockzo!@77")
            message="Security Breach"
            s.sendmail("sender_email_id",li[i],message)
            s.quit()
            print("done")
    
