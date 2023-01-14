import getpass
import pickle
import os

def Employee_1():
         print()
         print()
         print()
         print()
         print()
         print()
         print('\t\t\t\t\t 1 : Branch Manager ')
         print('\t\t\t\t\t 2  : Employee ')
         print('\t\t\t\t\t 3  : Return to main menu')
         print()
         print()
         chh=input('\t\t\t\tEnter your choice : ')
         if chh=='1':
                  Branch_Manager()
         elif chh=='2':
                  Employee_2()
         elif chh=='3':
                os.system('cls')
                Front_page()
         else:
                  print('\t\t\t\tWrong input given !')
                  input()
                  os.system('cls')
                  Front_page()

def Employee_2():
        A='1'
        x=input('Enter the username : ')
        y=getpass.getpass('Enter the password : ')
        print()
        print()
        while A=='1':
                r=open('bank_karmi.dat','rb')
                while True:
                        try:
                                z=pickle.load(r)
                                if z[1]==x and z[2]==y:
                                        print('1: check customer list')
                                        print('2: opening new account')
                                        print('3: deleting an account')
                                        print('4:  Returning to Previous Menu ')
                                        pro=input('Enter urr choice  : ')
                                        os.system('cls')
                                        if pro=='1':
                                                Check_customer()
                                        elif pro=='2':
                                                new_account_by_Employee()
                                        elif pro=='3':
                                                delete_customer_by_employee()
                                        elif pro=='4':
                                                Employee_1()
                                        else:
                                                print('Wrong Input Given')
                                                Front_page()
                                                
                                            
                        except EOFError:
                                r.close()
                                break

                print()
                print()
                print()
                print('For going to previous menu  : Press 8')
                print('For going to Main menu  : Press 9')
                print()
                print()
                L=input('Enter you choice  :  ')
                os.system('cls')
                if L=='8':
                        Employee_2()
                elif L=='9':
                        Employee_1()
                else:
                        Front_page()
                        
                        
                        
def Check_customer():
        print()
        print()
        p=open('SIRF.dat','rb')
        while True:
                try:
                        a=pickle.load(p)
                        print(a)
                except EOFError:
                        p.close()
                        break

def new_account_by_Employee():
        p=open('SIRF.dat','ab')
        while True:
                acc=input('Enter account no : ')
                username=input('Enter name of account holder : ')
                pin=input("enter security pin=")
                balance=input('Entre the initial amount   : Rs ')
                l=[acc,username,pin,balance]
                pickle.dump(l,p)
                print('for more press 1 otherwise anything : ')
                choice=int(input('Enter urr choice : '))
                print()
                print()
                print("Your account has been created susscessfully .")
                print('Thank You for being part of our PSP family !')
                if choice==1:
                        continue
                else:
                        p.close()
                        break

        

def update_employee():                                                          # INCOMPLETE
         p=open('SIRF.dat','rb+')
         r=input("Enter user id : ")
         while True:
                  try:
                           loc=p.tell()
                           k=pickle.load(p)
                           flag=0
                           if k[0]==r:
                                    k[1]=input('Enter new name : ')
                                    k[3]=input('Enter new amount  : ')
                                    p.seek(loc,0)
                                    pickle.dump(k,p)
                                    flag=1
                                    p.close()
                                    break
                  except EOFError:
                           p.close()
                           break
         if flag==0:
                  print('account not found !')
         else:
                  print('account updated succesfully...')

def THANOS():
         p=open('SIRF.dat','rb+')
         r=input("Enter user id : ")
         while True:
                  try:
                           loc=p.tell()
                           k=pickle.load(p)
                           flag=0
                           if k[0]==r:
                                    k[3]=input('Enter new amount  : ')
                                    p.seek(loc,0)
                                    pickle.dump(k,p)
                                    flag=1
                                    p.close()
                                    break
                  except EOFError:
                           p.close()
                           break
         if flag==0:
                  print('account not found !')
         else:
                  print('account updated succesfully...')

def delete_customer_by_employee():
        p=open('SIRF.dat','rb')
        n=open('new.dat','wb')
        r=input("User-ID wanna del.")
        flag=0
        while True:
                try:
                        a=pickle.load(p)
                        if a[0]==r:
                                print('Record deleted succesfully !')
                                flag=1
                                continue
                        else:
                                pickle.dump(a,n)
                except EOFError:
                        p.close()
                        n.close()
                        break
        os.remove('SIRF.dat')
        os.rename('new.dat','SIRF.dat')
        if flag==0:
                print('Record not found !')



def Branch_Manager():
        l='1'
        while l=='1':
                 code=123
                 pass1='111'
                 x=int(input('Enter the Branch Code : '))
                 y=getpass.getpass('Enter the password :  ')
                 if x==code and y==pass1:
                          os.system('cls')
                          print()
                          print()
                          print()
                          print()
                          print('\t\t\t\t\t\tVERIFIED SUCCESFULLY !!!')
                          print()
                          print()
                          print()
                          print()
                          print('''#  Check Employee List : Press A
#  Recruite a new employee : Press B
#  Check customer list : Press C
#  Remove an employee : Press D
#  Return to previous Menu : Press Z''')
                          print()
                          print()
                          print()
                          print()
                          op=input('Enter your choice : ')
                          os.system('cls')
                          print()
                          print()
                          print()
                          if op=='A':
                                   u=open('bank_karmi.dat','rb')
                                   print('\t\t\t\t\tEm_id\t\tusername\tPassword  \tSalery')
                                   while True:
                                            try:
                                                     a=pickle.load(u)
                                                     print('\t\t\t\t\t',a[0],'\t\t',a[1],'\t\t',a[2],'\t\t',a[3])
                                            except EOFError:
                                                     u.close()
                                                     print()
                                                     print()
                                                     break

                          elif op=='Z':
                                  Employee_1()
                                  
                          elif op=='B':
                                  p=open('bank_karmi.dat','ab')
                                  while True:
                                          Acc_no=input('User id_no. : ')
                                          name=input('Enter Name of Employee : ')
                                          pass1=input('Enter Password : ')
                                          Balance=input('Enter Salary of employee : ')
                                          lst=[Acc_no,name,pass1,Balance]
                                          pickle.dump(lst,p)
                                          print('Record inserted !!!')
                                          print('want to enter more records press 1 otherwise anything :')
                                          choice=input('Enter urr choice : ')
                                          if choice=='1':
                                                   continue
                                          else:
                                                   p.close()
                                                   break
                                  print()  
                                  print('all records inserted...')
   
                          elif op=='C':
                                   p=open('SIRF.dat','rb')
                                   print('Account no.\tAcc. Holder Name\tCurrent Balance')
                                   while True:
                                            try:
                                                     a=pickle.load(p)
                                                     print(a[0],'\t\t',a[1],'\t\t\t',a[3])
                                            except EOFError:
                                                     p.close()
                                                     print()
                                                     print()
                                                     break

                                           


                          elif op=='D':
                                   p=open('bank_karmi.dat','rb')
                                   n=open('new.dat','wb')
                                   r=int(input("user_id wanna del."))
                                   flag=0
                                   while True:
                                            try:
                                                     a=pickle.load(p)
                                                     if a[0]==r:
                                                             print(' !')
                                                             flag=1
                                                             continue
                                                     else:
                                                              pickle.dump(a,n)
                                            except EOFError:
                                                     p.close()
                                                     n.close()
                                                     break
                                   os.remove('bank_karmi.dat')
                                   os.rename('new.dat','bank_karmi.dat')
                                   if flag==0:
                                            print('Employee Record deleted succesfully !')
                          else:
                                  print('WRONG INPUT GIVEN !')
                                  Front_page()
                                  
                 else:
                          print()
                          print()
                          print()
                          print('WRONG CRUDENTIALS GIVEN !!!')
                          print()
                          print()
                 l=input('For Returning to Previous Menu : Press 5      ')
                 if l!='5':
                         os.system('cls')
                         Front_page()
                 else:
                          os.system('cls')
                          Branch_Manager()
                           


def withdraw_money():
         p=open('SIRF.dat','rb+')
         r=input("Enter user id : ")
         sss=float(input('Enter amt. to be withdrawn  :  '))
         while True:
                  try:
                           loc=p.tell()
                           k=pickle.load(p)
                           flag=0
                           if k[0]==r:
                                    a=int(k[3])
                                    if sss<a:
                                        a-=sss
                                        o=str(a)
                                        k[3]=o
                                        print('DONE !')
                                        print()
                                    else:
                                        print('INSUFFICIENT BALANCE !!!')
                                    p.seek(loc,0)
                                    pickle.dump(k,p)
                                    flag=1
                                    p.close()
                                    break
                  except EOFError:
                           p.close()
                           break
         if flag==0:
                  print('account not found !')

def deposit_money():
         p=open('SIRF.dat','rb+')
         r=input("Enter user id : ")
         sss=float(input('Enter amt. to be deposited  :  '))
         while True:
                  try:
                           loc=p.tell()
                           k=pickle.load(p)
                           flag=0
                           if k[0]==r:
                                   a=int(k[3])
                                   a+=sss
                                   o=str(a)
                                   k[3]=o
                                   print('DONE !')
                                   print()
                                   p.seek(loc,0)
                                   pickle.dump(k,p)
                                   flag=1
                                   p.close()
                                   break
                  except EOFError:
                           p.close()
                           break
         if flag==0:
                  print('account not found !')

    








def customer_frontpage():
        print()
        print('\t\t\t WELCOME TO PSP BANK ')
        print('''

''')
        print('\t\t\tFor Banking related Enquiry : Press 1')
        print('\t\t\tFor Bank servives : Press 2')
        print('\t\t\tFor Returning to main menu Press 3')
        print()
        ans=input('\t\t\tYour Input  :')
        if ans=='1':
                BankSchemes()
        elif ans=='3':
                Front_page()
        elif ans=='2':
                aaa='2'
                while aaa=='2':
                        print('\t\t\tFor creating new account : Press 3')
                        print('\t\t\tFor deleting your current account : Press 5')
                        print('\t\t\tFor depositing money : Press 6')
                        print('\t\t\tFor withdrawing money : Press 7')
                        print('\t\t\tFor returning to Previous Menu : Press 9')
                        Thanos=input('Enter your choice : ')
                        if Thanos=='3':
                                new_acc_By_customer()
                        elif Thanos=='5':
                                delete_customer_by_employee()
                        elif Thanos=='7':
                                 a=input('Enter account number : ')
                                 b=input('Enter your pin : ')
                                 print('VERIFIED SUCCESSFULLY !')
                                 print()
                                 c=input('Amount you want to withdraw : ')
                                 print()
                                 print('Amount deducted !.')
                                 input()
                        elif Thanos=='6':
                                 a=input('Enter account number : ')
                                 b=input('Enter your pin : ')
                                 print('VERIFIED SUCCESSFULLY !')
                                 print()
                                 c=input('Amount you want to deposit : ')
                                 print()
                                 print('Amount deposited !')
                                 input()
                        elif Thanos=='9':
                                customer_frontpage()
                        else:
                                print('Wrong Input Given !')
                                Front_page()
                                
                                
                                

                        aaa=input('For Going to previous MENU  :  2')
                        if aaa!='2':
                                Front_page()
        else:
                print('WRONG INPUT GIVEN')
                        

                

def new_acc_By_customer():
        print('NOTE :A single person cannot open more than 2 account in this bank.')
        print('Would you like to continue (y/n)')
        print()
        print('''Upon clicking Yes ! You agree to our terms and condition and assure that you does not
have more than 1 account in this Bank. ''')
        x=input('\t(y/n)')
        if x=='y':
                new_account_by_Employee()
        else:
                customer_frontpage()







        
def BankSchemes():
        print('For knowing about Interest rates  : Press a')
        print('For Knowing about Credit card  : Press b')
        print('For accessing Loan details : Press c')
        print('For accesing FD details : Press d')
        opp=input('Entre your choice : ')
        if opp=='a':
                print("Bank name Welcomes You to the world's finest and most trusted Bank.")
                print('We give our customer highest possible returns and best interest rates!!!')
                print()
                print('Interest on one month =                                         4.5%')
                print('Interest rate on quaterly basis =                               5.3%')
                print('Interest rate on semi-annual time Period =                      6%')
                print('Interest on yearly basis =                                      6.7%.')
                print('Interest on 5 years =                                           7.5%')
                print('Interest on 10 years or more =                                  8.1%')
                print('')
                print('NOTE  :  The interest will be compounded on Quaterly basis.')
                print()
                print('1:  Previous menu ')
                print('2:Main menu ')
                kl=input('Where you want to go  : ')
                if kl=='1':
                        BankSchemes()
                elif kl=='2':
                        customer_frontpage()
                else:
                        Front_page()

                        
                        
                        

        elif opp=='b':
                print('We Welcome you to the world\'s most Trusted PSP Bank. ')
                print()
                print('''Exclusive Benefits on Shopping, Lifestyle & More Plus Easy Rewards Redemption!
Use Anywhere in the World. 24/7 Support & Service. Fraud & Purchase Security.
Types: Travel Cards, Rewards Cards, Shopping Cards.''')
                print()
                print('''#  Platinum Card  :  1,00,000 Bonus Membership Rewards Points or stay vouchers worth INR 45,000 from Taj,
                      SeleQtions and Vivanta Hotels''')
                print('\tAnnual Fee: Rs. 60,000 plus applicable taxes.')
                print()
                print('''#  SmartEarn™ Credit Card  :  Rs. 500 cashback as Welcome Gift on eligible spends of
\tRs. 10,000 in the first 90 days of Cardmembership''')
                print('\tFirst Year Fee: Rs. 495 plus applicable taxes (Second Year onwards: Rs.495 plus applicable taxes)')
                print()
                print('#  Rewards® Credit Card : Welcome Gift of 4,000 Bonus Membership Rewards® Points')
                print('\tFirst Year Fee: Rs. 1,000 plus applicable taxes (Second Year onwards: Rs. 4,500 plus applicable taxes)')
                print()
                print()
                print('1:  Previous menu ')
                print('2:Main menu ')
                kl=input('Where you want to go  : ')
                if kl=='1':
                        BankSchemes()
                elif kl=='2':
                        customer_frontpage()
                else:
                        Front_page()


        elif opp=='c':
                print()
                print('We Welcome you to the world\'s most Trusted PSP Bank. ')
                print('We provide to our customer the best interest and easy loan facilities.')
                print('''
Business Loan  :
Business Loans with 25% discount on processing fees.

Working Capital Loan  :
Working Capital Loans with flat 50% off on processing fees (secured).

Doctor Loan  : 
Doctor Loan with processing fees starting from Rs.5,000.

Collateral-free Business Loans for Doctors.
Interest rates starting from 11.50% p.a.

Funds for business or personal use.
Longer tenure of up to 20 years (for salaried customers).
Balance transfer with additional loan facility.
Initial processing fee of Rs.2,500+GST and balance at the time of disbursement.*
Commercial Vehicle & Construction Equipment Loans with up to 85% funding.

Special scheme for first time users and single vehicle owners''')
                print()
                print('1:  Previous menu ')
                print('2:Main menu ')
                kl=input('Where you want to go  : ')
                if kl=='1':
                        BankSchemes()
                elif kl=='2':
                        customer_frontpage()
                else:
                        Front_page()


        elif opp=='d':
                print('''FD stands for fixed deposit. It is a amount given to bank for a fixed amount of time
and which can be taken only upon maturity of the time period. It is beneficial since it provides
higher rate of interest.''')
                print()
                print('\tTime period                    Rate of Interest(per month)')
                print('\tFor 1 year        \t   :  5%' )
                print('\tFor 3 year        \t   :  6.5%')
                print('\tFor 5 year       \t   :  8.5%')
                print('\tFor 10 year\t   :  10%')
                print('\tFor 10 years or more  :  Contact to Branch Manager ')
                print()
                print('NOTE  :  A FD has to be done for a minimum of 1 year.')
                print()
                print()
                print('1:  Previous menu ')
                print('2:Main menu ')
                kl=input('Where you want to go  : ')
                if kl=='1':
                        BankSchemes()
                elif kl=='2':
                        customer_frontpage()
                else:
                        Front_page()

                
        



def Front_page():
        print()
        print()
        print('                                                  1: As Staff member  ')
        print('                                                  2: As Customer ')
        print('                                                  3: To exit   ')
        print()
        ch=input('\t\t            Enter your Choice  :    ')
        os.system('cls')

        if ch=='1':
                 Employee_1()
        elif ch=='2':
                 customer_frontpage()
        elif ch=='3':
                print()
                print()
                print()
                print('THANK YOU FOR VISITING US  !!!')
                print('''HAVE A NICE DAY AHEAH  !  VISIT AGAIN...''')
                input()
                
        else:
                Front_page()
                print('Wrong input given !')
print('''

                `7MM"""Mq.  .M"""bgd `7MM"""Mq.     `7MM"""Yp,      db     `7MN.   `7MF`7MMF' `YMM' 
                  MM   `MM.,MI    "Y   MM   `MM.      MM    Yb     ;MM:      MMN.    M   MM   .M'   
                  MM   ,M9 `MMb.       MM   ,M9       MM    dP    ,V^MM.     M YMb   M   MM .d"     
                  MMmmdM9    `YMMNq.   MMmmdM9        MM"""bg.   ,M  `MM     M  `MN. M   MMMMM.     
                  MM       .     `MM   MM             MM    `Y   AbmmmqMA    M   `MM.M   MM  VMA    
                  MM       Mb     dM   MM             MM    ,9  A'     VML   M     YMM   MM   `MM.  
                .JMML.     P"Ybmmd"  .JMML.         .JMMmmmd9 .AMA.   .AMMA.JML.    YM .JMML.   MMb.
                                                                                                                                                                        
''')

print(''' __       __ ________ __       ______   ______  __       __ ________  ______         __      __  ______  __    __ 
|  \  _  |  |        |  \     /      \ /      \|  \     /  |        \/      \       |  \    /  \/      \|  \  |  \
| $$ / \ | $| $$$$$$$| $$    |  $$$$$$|  $$$$$$| $$\   /  $| $$$$$$$|  $$$$$$\       \$$\  /  $|  $$$$$$| $$  | $$
| $$/  $\| $| $$__   | $$    | $$   \$| $$  | $| $$$\ /  $$| $$__   | $$___\$$        \$$\/  $$| $$  | $| $$  | $$
| $$  $$$\ $| $$  \  | $$    | $$     | $$  | $| $$$$\  $$$| $$  \   \$$    \          \$$  $$ | $$  | $| $$  | $$
| $$ $$\$$\$| $$$$$  | $$    | $$   __| $$  | $| $$\$$ $$ $| $$$$$   _\$$$$$$\          \$$$$  | $$  | $| $$  | $$
| $$$$  \$$$| $$_____| $$____| $$__/  | $$__/ $| $$ \$$$| $| $$_____|  \__| $$          | $$   | $$__/ $| $$__/ $$
| $$$    \$$| $$     | $$     \$$    $$\$$    $| $$  \$ | $| $$     \\$$    $$          | $$    \$$    $$\$$    $$
 \$$      \$$\$$$$$$$$\$$$$$$$$\$$$$$$  \$$$$$$ \$$      \$$\$$$$$$$$ \$$$$$$            \$$     \$$$$$$  \$$$$$$ ''')
print()

Front_page()

