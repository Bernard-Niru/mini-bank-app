
#======================== Withdraw Function Through Admin===================
def withdraw_admin():

    updated_lines = []
    
    acc_num = input("enter your account number: ")
    with open('Account.txt', 'r') as acc_file:                                                        
        for line in acc_file:
            if acc_num in line:                
                column = line.split()
                amount = int(input("enter amount to Withdraw : "))
                if amount > 0:
                    new_balance = int(column[2]) - amount
                    column[2]=str(new_balance)
                    updated_line = ' '.join(column) + '\n'
                    updated_lines.append(updated_line)
                    
                    from datetime import datetime
                    now = datetime.now()
                    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open('Transaction.txt', 'a') as tsn_file:
                        tsn_file.write(f"{acc_num}\t")
                        tsn_file.write(f"{timestamp}\t")
                        tsn_file.write(f"Withdraw\t")
                        tsn_file.write(f"{amount}\n")
                    with open('Account.txt', 'w') as acc_file:
                        acc_file.writelines(updated_lines)
                        print("Withdrawal successful.")
                else:
                     print('amount must be greater than zero')       
            else:
                updated_lines.append(line)

    with open('Account.txt', 'w') as acc_file:
        acc_file.writelines(updated_lines)
                
#==============================================================================             

#======================== Deposit Function Through Admin =====================
def deposit_admin():

    updated_lines = []
    
    acc_num = input("enter your account number: ")
    with open('Account.txt', 'r') as acc_file:                                                        
        for line in acc_file:
            if acc_num in line:                
                column = line.split()
                amount = int(input("enter amount to Deposit : "))
                if amount > 0:
                    new_balance = int(column[2]) + amount
                    column[2]=str(new_balance)
                    updated_line = ' '.join(column) + '\n'
                    updated_lines.append(updated_line)                   
                    
                    
                    from datetime import datetime
                    now = datetime.now()
                    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open('Transaction.txt', 'a') as tsn_file:
                        tsn_file.write(f"{acc_num}\t")
                        tsn_file.write(f"{timestamp}\t")
                        tsn_file.write(f"Deposit\t")
                        tsn_file.write(f"{amount}\n")
                    with open('Account.txt', 'w') as acc_file:
                        acc_file.writelines(updated_lines)
                        print("Deposit successful.")
                    
                else:
                     print('amount must be greater than zero')
            else:
                updated_lines.append(line)

    with open('Account.txt', 'w') as acc_file:
        acc_file.writelines(updated_lines)         
#==============================================================================

#=======================Withdraw Function Through Customer ===================
def withdraw_customer(customer_ID):

    updated_lines = []
    
    with open('Account.txt', 'r') as acc_file:                                                        
        for line in acc_file:
            if customer_ID in line:                 
                column = line.split()
                acc_num = column[0]
                amount = int(input("enter amount to Withdraw : "))
                if amount > 0:
                    new_balance = int(column[2]) - amount
                    column[2]=str(new_balance)
                    updated_line = ' '.join(column) + '\n'
                    updated_lines.append(updated_line)
                    
                    from datetime import datetime
                    now = datetime.now()
                    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open('Transaction.txt', 'a') as tsn_file:
                        tsn_file.write(f"{acc_num}\t")
                        tsn_file.write(f"{timestamp}\t")
                        tsn_file.write(f"Withdraw\t")
                        tsn_file.write(f"{amount}\n")
                    with open('Account.txt', 'w') as acc_file:
                        acc_file.writelines(updated_lines)
                        print("Withdrawal successful.")
                else:
                     print('amount must be greater than zero')       
            else:
                updated_lines.append(line)        

    with open('Account.txt', 'w') as acc_file:
        acc_file.writelines(updated_lines)               
#===========================================================================              

#==================== Deposit Function Through Customer ====================
def deposit_customer(customer_ID):

    updated_lines = []
    
    with open('Account.txt', 'r') as acc_file:                                                        
        for line in acc_file:
            if customer_ID in line:                
                column = line.split()
                acc_num = column[0]
                amount = int(input("enter amount to Deposit : "))
                if amount > 0:
                    new_balance = int(column[2]) + amount
                    column[2]=str(new_balance)
                    updated_line = ' '.join(column) + '\n'
                    updated_lines.append(updated_line)                   
                    
                    
                    from datetime import datetime
                    now = datetime.now()
                    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
                    with open('Transaction.txt', 'a') as tsn_file:
                        tsn_file.write(f"{acc_num}\t")
                        tsn_file.write(f"{timestamp}\t")
                        tsn_file.write(f"Deposit\t")
                        tsn_file.write(f"{amount}\n")
                    with open('Account.txt', 'w') as acc_file:
                        acc_file.writelines(updated_lines)
                        print("Deposit successful.")
                    
                else:
                     print('amount must be greater than zero')
            else:
                updated_lines.append(line)

    with open('Account.txt', 'w') as acc_file:
        acc_file.writelines(updated_lines)         
#==============================================================================

#============================ Bank Fuction for Admin ==========================
def admin_bank():                      
    while True:   
            
            print("=========MENU=======")
            print("1.Create Customer")
            print("2..Create Account")
            print("3..Deposit")
            print("4..Withdraw")
            print("5.Check Balance")
            print("6..Transaction History")
            print("7.Exit")
            print("====================")

            choice=input('enter your option from(1-7): ')

            if choice == '1':
                cus_name = input("Enter Customer Name: ")
                cus_pswd = input('enter Customer password: ')
                try:
                    with open('Customer.txt', 'r') as cus_file:
                        line = cus_file.readlines()
                        column = line[-1].split()
                        customer_ID = column[0]
                            
                        suffix = int(customer_ID[-4:])
                        prefix = customer_ID[-5]
                        suffix += 1
                        customer_ID= prefix+str(suffix).zfill(4)
                except FileNotFoundError:
                    line= []
                    customer_ID = 'C0001'
                                    
                                      
                    
                with open('user.txt', 'r') as us_file:
                    line = us_file.readlines() 
                    column = line[-1].split()
                    User_ID= column[0]
                        
                    suffix = int(User_ID[-4:])
                    prefix = User_ID[-5]
                    suffix += 1
                    User_ID= prefix+str(suffix).zfill(4) 

                us_file=open('User.txt','a')
                us_file.write(f'{User_ID}\t')
                us_file.write(f'{cus_pswd}\t')
                us_file.write(f'Customer\t')
                us_file.write('\n')
                us_file.close()

                cus_file=open('Customer.txt','a')
                cus_file.write(f'{customer_ID}\t')
                cus_file.write(f'{cus_name}\t')
                cus_file.write(f'{User_ID}\t')
                cus_file.write('\n')
                cus_file.close()
                             
                print(' Customer created') 
                print(f' Customer ID: {customer_ID}') 

            elif choice == '2':
                found = False
                customer_ID = input("Enter your customer ID: ")
                balance = int(input('enter your intial balance: '))

                with open('Customer.txt', 'r') as cus_file:
                    for line in cus_file:
                        if customer_ID in line:
                            found = True
                                                                                  
                            try:                            
                                with open('Account.txt', 'r') as acc_file:
                                    line = acc_file.readlines()
                                    column = line[-1].split()
                                    acc_num = column[0]
                                        
                                    suffix = int(acc_num[-4:])
                                    prefix = acc_num[-5]
                                    suffix += 1
                                    acc_num= prefix+str(suffix).zfill(4)
                            except FileNotFoundError:
                                line= []        
                                acc_num = 'A0001 '
                        
                                        
                            acc_file=open('Account.txt','a')
                            acc_file.write(f'{acc_num}\t')
                            acc_file.write(f'{customer_ID}\t')
                            acc_file.write(f'{balance}\t')
                            acc_file.write('\n')
                            acc_file.close
                                    
                            print('account created')
                            print(f'Account number : {acc_num}')
                            break
                            
                    if not found:
                        print("Customer not found")
                                       
            elif choice == '3':
                deposit_admin()
                                
            elif choice == '4':
                withdraw_admin()
                    
            elif choice == '5':
                acc_num = input("Enter your account number (eg:- A0001) :")
                with open('Account.txt', 'r') as acc_file:                                                        
                    for line in acc_file:
                        if acc_num in line:                
                            column = line.split() 
                            print(f'Your Balance is {column[2]} LKR')

            elif choice == '6':
                acc_num = input("Enter your account number (eg:- A0001) :")
                with open('Transaction.txt', 'r') as tsn_file:                                                        
                    for line in tsn_file:
                        if acc_num in line:                
                            print (line)
                
            elif choice == '7':
                break

            else:
                print('Invalid Choice,Choose Your option from (1-7)')
#=========================================================================

#==================== Bank Fuction for Customer ==========================
def customer_bank(customer_ID):                      
    while True:   
            
            print("=========MENU=======")
            print("1..Deposit")
            print("2..Withdraw")
            print("3.Check Balance")
            print("4..Transaction History")
            print("5.Exit")
            print("====================")

            choice=input('enter your option from(1-5): ')

            if choice == '1':
                deposit_customer(customer_ID)

            elif choice == '2':
                withdraw_customer(customer_ID)

            elif choice == '3':
                with open('Account.txt', 'r') as acc_file:                                                        
                    for line in acc_file:
                        if customer_ID in line:                
                            column = line.split() 
                            print(f'Your Balance is {column[2]} LKR')

            elif choice == '4':
                with open('Account.txt', 'r') as acc_file:                                                        
                    for line in acc_file:
                        if customer_ID in line:
                            break                
                    column = line.split()
                    acc_num = column[0]
                    with open('Transaction.txt','r') as tsn_file:
                        for line in tsn_file:
                            if acc_num in line:                            
                                print(line) 

            elif choice == '5':
                break

            else:
                print('Invalid Choice,Choose Your option from (1-5)')

#==============================================================================

#========================== Admin Login ======================================
def admin_login():

    admin_id = input("Enter Your ID: ")
    admin_pswd = input("Enter your password: ")

    if admin_id == 'Ad001' and admin_pswd == '123456' :
        try:
            with open('User.txt', 'r') as us_file:
                lines = us_file.readlines()
        except FileNotFoundError:
            lines = []
        found = False
        for line in lines:
            if 'U0001' in line:
                found = True
                break

        if found:
            print("Hello admin")
            admin_bank()
        else:
            with open('User.txt', 'a') as us_file:
                us_file.write(f'U0001\t')
                us_file.write(f'{admin_pswd}\t')
                us_file.write(f'Admin\n')      
            admin_bank()

    else:
        
        print("Incorrect User ID or Password")

#==============================================================================

#========================== Customer Login ====================================
def customer_login():
    
    
    try:
        found = False
        customer_ID = input("Enter your customer ID: ")
        with open('Customer.txt', 'r') as cus_file:                                                        
                    for line in cus_file:
                        if customer_ID in line:
                            
                            column = line.split()
                            print(f'Hello {column[1]}')
                            User_ID = column[0]
                                                      
                            with open('User.txt', 'r') as us_file:
                                for line in us_file:
                                    if User_ID in line:
                                        found = True 
                                column = line.split()
                                user_pswd = column[1]
                                cus_pswd = input('Enter Your password : ')
                                if cus_pswd == user_pswd:
                                    print("Login Successful")
                                    customer_bank(customer_ID)
                                else:
                                    print("Incorrect password")
                                   
                    if not found:
                        print('Customer ID not Found')                                                                  
    except FileNotFoundError:
        print('First Admin have to Login')                     

#============================================================================

#====================== Mini Banking System =================================
while True:
    print("---------Mini Banking System---------")
    print("")
    print('1.Login as Admin')
    print('2.Login as Customer')
    print('3.Exit')
    print("")

    choice = input("Enter your option : ")

    if choice == '1':
        admin_login()
    elif choice == '2':
        customer_login()
    elif choice == '3':
        break
    else:
        print('Choose 1 or 2')

#===============================================================================
       



