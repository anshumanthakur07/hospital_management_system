from sys import exit 
import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='sukhman117',database='anshu')
if conn.is_connected():
  print('successfully connected')
c1=conn.cursor()
print('--------------------------------------------------------------------------------------')
print("***********HOSPITAL MANAGEMENT SYSTEM***********")
print('--------------------------------------------------------------------------------------')
print('"GOD WISHES YOU"')
print("1.*LOGIN*")
print("2.*EXIT*")
choice=int(input("ENTER YOUR CHOICE:"))
if choice==1:
  u1=input("enter user name:")
  pwd1=input("enter the password:")
  while u1=='anshuman singh'and pwd1=='123':
    print('connected')

    print("***WELCOME TO HOSPITAL***")
    print("successfully connected")
    print('1.RegisteringPatient details')
    print('2.RegisteringDoctor details')
    print('3.RegisteringWorker details')
    print("4.total patient details")
    print("5.total doctor details")
    print("6.total worker details")
    print('7.Patient detail')
    print('8.Doctor detail')
    print('9.Worker detail')
    print('10.Exit')
    choice=int(input('ENTER YOUR CHOICE:'))
    if choice==1:
      p_name=input('Enter Patient Name:')
      p_age=int(input('Enter Age of patient:'))
      p_gender=input('Enter gender of patient:')
      p_fathername=input('Enter Patient fathers Name:')
      p_problems=input('Enter the Problem/Disease patient have:')
      p_phono=int(input('Enter Phone number of patient:'))
      p_address=input('Enter address of patient:')
      sql_insert="insert into patient_details values(""'"+p_name+"',"+str(p_age)+",'"+p_gender+"','"+p_fathername+"','"+p_problems+"',"+str(p_phono)+",'"+p_address+"')"
      c1.execute(sql_insert)
      print('***********SUCCESSFULLY REGISTERED***********')
      conn.commit()

    elif choice==2:
      d_name=input('Enter Doctor Name:')
      d_age=int(input('Enter Age:'))
      d_gender=input('Enter gender of doctor:')
      d_department=input('Enter the Department:')
      d_phono=int(input('Enter Phone number:'))
      d_address=input('Enter address of doctor:')
      sql_insert="insert into doctor_details values(""'"+d_name+"',"+str(d_age)+",'"+d_gender+"','"+d_department+"',"+str(d_phono)+",'"+d_address+"')"
      c1.execute(sql_insert)
      print('successfully registered')
      conn.commit()

    elif choice==3:
      w_name=input('Enter Worker Name:')
      w_age=int(input('Enter Age:'))
      w_gender=input('Enter gender of worker:')
      w_workname=input('Enter type of work:')
      w_phono=int(input('Enter Phone number:'))
      w_address=input('Enter address of worker:')
      sql_insert="insert into worker_details values(""'"+w_name+"',"+str(w_age)+",'"+w_gender+"','"+w_workname+"',"+str(w_phono)+",'"+w_address+"')"
      c1.execute(sql_insert)
      print('successfully registered')
      conn.commit()

    elif choice==4:
      sql_w='select*from patient_details '
      c1.execute(sql_w)
      r = c1.fetchall()
      for i in r :
        print(i)

    elif choice==5:
      sql_x="select*from doctor_details"
      c1.execute(sql_x)
      s=c1.fetchall()
      for i in s:
        print(i)

    elif choice==6:
      sql_y="select*from worker_details"
      c1.execute(sql_y)
      t=c1.fetchall()
      for i in t:
        print(i)

    elif choice==7:
      h=input("Enter the name:")
      sql_w='select*from patient_details where p_name=("{}")'.format(h)
      c1.execute(sql_w)
      u = c1.fetchall()
      for i in u:
        print(i)

    elif choice==8:
      d=input("Enter the name:")
      sql_d='select*from doctor_details where d_name=("{}")'.format(d)
      c1.execute(sql_d)
      v=c1.fetchall()
      for i in v:
        print(i)

    elif choice==9:
      f=input("Enter the name:")
      sql_f='select*from worker_details where w_name=("{}")'.format(f)
      c1.execute(sql_f)
      w=c1.fetchall()
      for i in w:
        print(i)

    elif choice==10:
      print("***THANK YOU***")
      exit()
      break
  else:
    print('wrong username&password')
if choice==2:
  print("***THANK YOU***")
  exit()