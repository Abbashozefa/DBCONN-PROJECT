try:
    import pymysql
    import pandas as pd
    import matplotlib.pyplot as plt
    import datetime


    pd.set_option("display.max_columns", 12)

    conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
    a=conn.cursor()
    while(True):
        print('1.RECEPTIONIST')
        print('2.OPTOMETRIST(GENERAL CHECKUP)')
        print('3.OPTHALMOLOGIST(DOCTOR)')
        print('4.SHOW STATISTICS ')
        
        ch1=int(input('SELECT YOUR FIELD:::'))
        if(ch1==4):
            a.execute('SELECT AGE FROM PATIENT')
            D=a.fetchall()
            S=()        
            for j in D:           
                S=S+j
            plt.hist(S,bins=[0,20,40,60,80,100,120],facecolor='green',edgecolor='red')
            plt.title('PATIENT AGE DISTRIBUTION')
            plt.xlabel('AGES')
            plt.ylabel('FREQUENCY')
            plt.grid(True)
            plt.show()
            
        def receptionist():
            while(True):
            
                conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
                a=conn.cursor()
                a.execute("show tables")
                D=a.fetchone()
                if(D==None):
                    a.execute('CREATE TABLE PATIENT(PATIENT_ID INT ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')
                    
                print('----------------------------------------------------------------------------------------------------------')
                print('1.NEW PATIENT')
                print('2.ROUTINE CHECKUP PATIENT DETAILS')
                print('3.VIEW PATIENT DETAILS')
                print('4.GO BACK')
                print('----------------------------------------------------------------------------------------------------------')
                ch2=int(input('SELECT YOUR FIELD:::'))
                print('----------------------------------------------------------------------------------------------------------')                
                
                '''a.execute('CREATE TABLE PATIENT(PATIENT_ID INT ,PATIENT_NAME VARCHAR(20),AGE INT,DATE_OF_LAST_VISIT DATE,CONSULTING_DOCTOR VARCHAR(20),RIGHT_SPH DECIMAL(2,1),RIGHT_CYL DECIMAL(2,1),RIGHT_AXIS INT,LEFT_SPH DECIMAL(2,1),LEFT_CYL DECIMAL(2,1),LEFT_AXIS INT)')'''
                    
               
                if (ch2==1) :
                    
                    

                    user=int(input('Enter PATIENT ID:'))
                    name=input('Enter PATIENT NAME:')
                    age=int(input('Enter PATIENT AGE:'))
                    G= str(datetime.date.today())
                    
                    
                    doc=input('Enter CONSULTING DOCTOR:')
                    print('PATIENT ENTRY DONE')
                     
                     

                    a.execute("insert into PATIENT values("+str(user)+",'"+name+"',"+str(age)+",'"+G+"','"+doc+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                elif(ch2==3):
                    user=int(input('Enter PATIENT ID'))
                    
                    a.execute("select PATIENT_ID  ,PATIENT_NAME,AGE,DATE_OF_LAST_VISIT,CONSULTING_DOCTOR from PATIENT where PATIENT_ID="+str(user))
                    D=a.fetchall()
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print('----------------------------------------------------------------------------------------------------------')
                    print(data.iloc[:,0:5])
                    print('----------------------------------------------------------------------------------------------------------')
                    
                    
                elif(ch2==2):
                    user=int(input('Enter PATIENT ID:'))
                    date=input('ENTER DATE :')
                    age=int(input('Enter PATIENT AGE'))
                    a.execute("select distinct* from PATIENT where PATIENT_ID="+str(user) )
                    D=a.fetchall()               
                    
                    a.execute("insert into PATIENT values("+str(user)+",'"+D[0][1]+"',"+str(age)+",'"+date+"','"+D[0][4]+"',NULL,NULL,NULL,NULL,NULL,NULL)")
                else:
                    break
                

                    
                    
                conn.commit()
        def general():
            while(True):
                conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
                a=conn.cursor()

                print('----------------------------------------------------------------------------------------------------------')
                print('1.UPDATE PATIENTS EYE POWER')
                print('2.MAKE EYE POWER')
                print('3.')
                print('4.GO BACK')
                print('----------------------------------------------------------------------------------------------------------')
                ch2=int(input('SELECT YOUR FIELD:::'))
                print('----------------------------------------------------------------------------------------------------------')
               
                
                
                    
               
                if (ch2==1) :                 
                    
                    user=input('Enter PATIENT ID:')
                    rsph=input('Enter RIGHT EYE AXIS:')
                    rcyl=input('Enter RIGHT EYE CYLINDRICAL:')
                    raxis=input('Enter RIGHT EYE AXIS:')
                    date=input('ENTER DATE :')
                    lsph=input('Enter LEFT EYE AXIS:')
                    lcyl=input('Enter LEFT EYE CYLINDRICAL:')
                    laxis=input('Enter LEFT EYE AXIS:')                      

                    a.execute("update PATIENT set RIGHT_SPH ="+rsph+",RIGHT_CYL ="+rcyl+",RIGHT_AXIS ="+raxis+",LEFT_SPH ="+lsph+",LEFT_CYL ="+lcyl+",LEFT_AXIS="+laxis+"where PATIENT_ID="+user+" and DATE_OF_LAST_VISIT='"+date+"'")
                elif(ch2==3):
                    pass
                    
                elif(ch2==2):
                    
                    user=input('Enter PATIENT ID:')
                    rsph=input('Enter RIGHT EYE AXIS:')
                    rcyl=input('Enter RIGHT EYE CYLINDRICAL:')
                    raxis=input('Enter RIGHT EYE AXIS')
                    date=input('ENTER DATE :')
                    lsph=input('Enter LEFT EYE AXIS:')
                    lcyl=input('Enter LEFT EYE CYLINDRICAL:')
                    laxis=input('Enter LEFT EYE AXIS:')                   
                    
                    a.execute("update PATIENT set RIGHT_SPH ="+rsph+",RIGHT_CYL ="+rcyl+",RIGHT_AXIS ="+raxis+",LEFT_SPH ="+lsph+",LEFT_CYL ="+lcyl+",LEFT_AXIS="+laxis+"where PATIENT_ID="+user+" and DATE_OF_LAST_VISIT='"+date+"'")
                    print('ENTRY DONE')
                else:
                    break    
                    
                conn.commit()
        def doctor():
            while(True):
                conn=pymysql.connect(host='localhost',user='root',password='yellowyellow',database='EYEHOSPITAL')
                a=conn.cursor()

                print('----------------------------------------------------------------------------------------------------------')
                print('1.CHECK COMPLETE RECORD')
                print('2.')
                print('3.GIVE PRESCRIPTION')
                print('4.GO BACK')
                print('----------------------------------------------------------------------------------------------------------')
                ch2=int(input('SELECT YOUR FIELD:::'))
                print('----------------------------------------------------------------------------------------------------------')
                
                
                
                    
               
                if (ch2==1) :
                    
                    

                    user=int(input('Enter PATIENT ID:'))
                    a.execute("select *from PATIENT WHERE PATIENT_ID="+str(user))
                    D=a.fetchall()
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print('----------------------------------------------------------------------------------------------------------')
                    print(data)
                    print('----------------------------------------------------------------------------------------------------------')                                     
                     

                   
                elif(ch2==3):
                    print('==============================================================================================================')
                    print('=================================================PRESCRIPTION=================================================')
                    
                    user=int(input('                PATIENT ID:: '))
                    print('----------------------------------------------------------------------------------------------------------')
                    date=input('                    DATE::')
                    print('----------------------------------------------------------------------------------------------------------')
                    med=input('                     MEDICATIONS::')
                    print('----------------------------------------------------------------------------------------------------------')
                    a.execute("select *from PATIENT WHERE PATIENT_ID="+str(user)+" and DATE_OF_LAST_VISIT='"+date+"'")
                    D=a.fetchall()
                    print('                         AGE :: '+str(D[0][2]))
                    print('----------------------------------------------------------------------------------------------------------')
                    
                    print('                         CONSULTING DOCTOR'+D[0][4])
                    print('----------------------------------------------------------------------------------------------------------')
                    data=pd.DataFrame(D,columns=['PATIENT_ID ' ,'PATIENT_NAME','AGE','DATE_OF_LAST_VISIT','CONSULTING_DOCTOR','RIGHT_SPH','RIGHT_CYL','RIGHT_AXIS','LEFT_SPH','LEFT_CYL','LEFT_AXIS'])
                    data.set_index('PATIENT_ID ',inplace=True)
                    print(data.iloc[:,5:])
                    print('================================================================================================================')
                    print('================================================================================================================')
                elif(ch2==2):
                   pass
                else:
                    break  
                conn.commit()    
        if(ch1==1):
            receptionist()
            
        elif(ch1==2):
            general()
        elif(ch1==3):
            doctor()
        else:
            break
    conn.commit()
except:
    print('|-----------------------------------------------------------------------|')
    print('                     OPPS!  SOMETHING JUST WENT WRONG')
    print('|-----------------------------------------------------------------------|')


    
        
    
