import pymysql
import pandas as pd


conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
a=conn.cursor()
print('1.RECEPTIONIST')
print('2.OPTOMETRIST(GENERAL CHECKUP)')
print('3.OPTHALMOLOGIST(DOCTOR)')
ch1=int(input('SELECT YOUR FIELD'))

def receptionist():
    conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
    a=conn.cursor()

   
    print('1.NEW PATIENT')
    print('2.ROUTINE CHECKUP PATIENT DETAILS')
    print('3.VIEW PATIENT DETAILS')
    ch2=int(input('SELECT YOUR FIELD'))
   
    
    '''a.execute('CREATE TABLE PATIENT(PATIENT_ID INT PRIMARY KEY ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')'''
        
   
    if (ch2==1) :
        
        

        user=int(input('Enter PATIENT ID'))
        name=input('Enter PATIENT NAME')
        age=int(input('Enter PATIENT AGE'))
        date=input('Enter DATE')
        doc=input('Enter CONSULTING DOCTOR')
         
         

        a.execute("insert into PATIENT values("+str(user)+",'"+name+"',"+str(age)+",'"+date+"','"+doc+"',NULL,NULL,NULL,NULL,NULL,NULL)")
    elif(ch2==3):
        user=int(input('Enter PATIENT ID'))
        name=input('Enter PATIENT NAME')
        a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user)+" and PATIENT_NAME='"+name+"'" )
        D=a.fetchall()
        data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
        data.set_index('PATIENT_ID ',inplace=True)
        print(data.iloc[:,0:5])
        a.execute("select *from PATIENT")
        D=a.fetchall()
        data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
        
        print(data.iloc[:,0:5])
        

    conn.commit()

if(ch1==1):
    receptionist()
    
elif(ch1==2):
    pass
else:
    pass
conn.commit()

