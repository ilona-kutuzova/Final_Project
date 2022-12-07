import os
import random
import numpy as np

print ("--------------------------------------------------------",
"\n                     GEO Investments", 
"\n--------------------------------------------------------",
"\n1) Create a profile",
"\n2) Log in",
"\n--------------------------------------------------------")

user_option_choice = input("\nEnter a number option and press ENTER or type 'q' to quit: ")

account_types = ["Small Business Class", "Medium Business Class", "Large Business Class", "Enterprise Business"]

username = input("Enter username: ")
password = input("Enter password: ")
PIN = input("Enter four-digit PIN: ")
user_login_info = username + "login_info"

#Function to calculate sum of elements in array
def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return(sum)

#Function to calculate number of transactions in array
def calc_monthly_transactions_number(arr):
  monthly_transactions_number = len(arr)
  return monthly_transactions_number

#Function to print months
def print_months():
  print("\n1) January",
        "\n2) February", "\n3) March", "\n4) April", "\n5) May", "\n6) June", "\n7) July", "\n8) August", "\n9) September", "\n10) October", "\n11) November", "\n12) December", "\n")

#Creating user class
class User:
  def __init__(self, username, password, PIN):
    self.username = username
    self.password = password
    self.pin = PIN

  #Function to create deposits for a year
  def create_yearly_deposits(self):
  
    user_deposits = []
    for i in range(12):
      random_deposits = np.random.randint(1,999,random.randint(1,20))
      user_deposits.append(random_deposits)
       
    return user_deposits  

  #Function to create withdrawals for a year
  def create_yearly_withdrawals(self):
  
    user_withdrawals = []
    for i in range(12):
      
      monthly_fee = np.array([10])  
      random_withdrawals = np.random.randint(1,999,random.randint(1,20))
      #Adding monthly $10 fee
      random_withdrawals_with_fee = np.append(monthly_fee, random_withdrawals)
      
      user_withdrawals.append(random_withdrawals_with_fee)
      
    return user_withdrawals
  
#Sign up function
def signup():
  name = input("Enter full name: ")
  address = input("Enter address: ")
  date_of_birth = input("Enter your date of birth: ")
  business_name = input("Enter your business name: ")
  incorporation_date = input("Enter date of incorporation: ")
  stakeholders_equity_list = input("Enter the list of stakeholders and equity: ")
  print("\nChoose from the list: ", account_types)
  account_type = input("Please enter your account type: ")

  #Generating account number
  random_numbers = random.randint(00000000,99999999)
  split_business_name = [*business_name]
  account_number = str(random_numbers) + "-" + split_business_name[0] + split_business_name[1]   
  
  user_file_name = username
  user_login_info = username + "login_info"
    
  with open(user_file_name, "w") as f:
    f.write(name + "\n")
    f.write(address + "\n")
    f.write(date_of_birth + "\n")
    f.write(business_name + "\n")
    f.write(incorporation_date + "\n")
    f.write(stakeholders_equity_list + "\n")
    f.write(account_type + "\n")
    f.write(account_number)
    f.close()
  with open(user_login_info, "w") as f:
    f.write(username + "\n")
    f.write(password + "\n")
    f.write(PIN)
    f.close()
  print("You have registered successfully!")
  
#View profile function
def view_profile():
   print("\nACCOUNT INFORMATION" + "\n")
   user_file_name = username
   text_file = open(user_file_name)
   contents = text_file.read()
   print(contents)
   text_file.close()

#Change username function
def change_username():
   with open(user_login_info, "r") as f:
    stored_username, stored_password, stored_pin = f.read().split("\n")
    f.close()
   new_username = input("Enter your new username: ")
   new_login_user_info = new_username + "login_info"

   with open(user_login_info, 'w') as file:
    file.write(new_username + "\n")
    file.write(stored_password + "\n")
    file.write(stored_pin)
    file.close()
     
   os.rename(user_login_info, new_login_user_info)
   os.rename(stored_username, new_username)

   print("\n" + "Username Changed Successfully!" + "\n")

#Change password function
def change_password():
  with open(user_login_info, "r") as f:
    stored_username, stored_password, stored_pin = f.read().split("\n")
  f.close()
  new_password = input("Enter your new password: ")

  with open(user_login_info, 'w') as file:
    file.write(stored_username + "\n")
    file.write(new_password + "\n")
    file.write(stored_pin)
    file.close()

    print("\n" + "Password Changed Successfully!" + "\n")

#Change PIN function
def change_pin():
   with open(user_login_info, "r") as f:
    stored_username, stored_password, stored_pin = f.read().split("\n")
    f.close()
    new_pin = input("Enter your new PIN: ")

    with open(user_login_info, 'w') as file:
      file.write(stored_username + "\n")
      file.write(stored_password + "\n")
      file.write(new_pin)
      file.close()

    print("\n" + "PIN Changed Successfully!" + "\n")

#Log in function
def login(): 
  with open(user_login_info, "r") as f:
    stored_username, stored_password, stored_pin = f.read().split("\n")
    f.close()
    if username == stored_username and password == stored_password and PIN == stored_pin:
      user = User(username, password, PIN)
      yearly_deposits = user.create_yearly_deposits()
      yearly_withdrawals = user.create_yearly_withdrawals()
      total_deposits_number = 0
      total_withdrawals_number = 0
      total_deposits = 0
      total_withdrawals = 0
      print("\n" + "Logged in Successfully!" + "\n", 
           "\n1) View profile",
           "\n2) Change username",
           "\n3) Change password",
           "\n4) Change PIN",
           "\n5) Deactivate account",
           "\n6) View all statements",
           "\n7) View monthly statements",
           "\n8) View insights",
           "\n9) Quit")
      user_option_choice = input("\nEnter a number option and press ENTER: ")

      if(user_option_choice == "1"):
        view_profile()
       
      elif(user_option_choice == "2"):
        change_username()
       
      elif(user_option_choice == "3"):
         change_password()

      elif(user_option_choice == "4"):
          change_pin()

      elif(user_option_choice == "5"):
        os.remove(user_login_info)
        print("\n" + "Account Deactivated Successfully!" + "\n")

      elif(user_option_choice == "6"):
        
        print("All Deposits: ", yearly_deposits, "\n")
        print("All Withdrawals: ", yearly_withdrawals)
        
        for x in range(12):
          total_deposits_number = total_deposits_number + len(yearly_deposits[x])

        for x in range(12):
          total_withdrawals_number = total_withdrawals_number + len(yearly_withdrawals[x])

        #Calculating total number of transactions made
        total_transactions_number = total_deposits_number + total_withdrawals_number

        print("Total Number of Transactions Made: ", total_transactions_number)

        for x in range(12):
          total_deposits = total_deposits + _sum(yearly_deposits[x])

          total_withdrawals = total_withdrawals + _sum(yearly_withdrawals[x])

        #Calculating total gain or loss in account (negative gain = loss)
        total_gain = total_deposits - total_withdrawals
        
        print("Total Gain/Loss: ", total_gain)

      elif(user_option_choice == "7"):
        print_months()
        
        month = input("Choose a month: ")

        month_number = int(month)-1
        deposits_number = calc_monthly_transactions_number(yearly_deposits[month_number])
        withdrawals_number = calc_monthly_transactions_number(yearly_withdrawals[month_number])
        total_deposits = _sum(yearly_deposits[month_number])
        total_withdrawals = _sum(yearly_withdrawals[month_number])
        
        #Calculating total gain/loss for the chosen month
        total_gain = total_deposits - total_withdrawals
        print("\nDeposits: ", yearly_deposits[month_number],
              "\nWithdrawals: ", yearly_withdrawals[month_number],
              "\nTotal number of transactions made: ", deposits_number + withdrawals_number,
               "\nTotal Gain: ", total_gain)
          
      elif(user_option_choice == "8"):

        print("\n1) Compare monthly spending against other months",
              "\n2) Get quarterly income report")
        user_option_choice = input("\nEnter a number option and press ENTER: ")

        if(user_option_choice == "1"):
          print_months()
          month_one = int(input("Enter first month number: "))
          month_two = int(input("Enter second month number: "))
          month_one_total_withdrawals = sum(yearly_withdrawals[month_one])
          print("First month withdrawals: ", month_one_total_withdrawals)
          month_two_total_withdrawals = sum(yearly_withdrawals[month_two])
          print("Second month withdrawals: ", month_two_total_withdrawals)

        if(user_option_choice == "2"):
          print("\n1) Quarter 1: January, February, March", 
               "\n2) Quarter 2: April, May, June", 
               "\n3) Quarter 3: July, August, September", 
               "\n4) Quarter 4: October, November, December", "\n")

          quarter = input("Enter quarter number: ")

          if(quarter == "1"):

            total_deposits = _sum(yearly_deposits[0]) + _sum(yearly_deposits[1]) + _sum(yearly_deposits[2])
            total_withdrawals = _sum(yearly_withdrawals[0]) + _sum(yearly_withdrawals[1]) + _sum(yearly_withdrawals[2])
            total_gain = total_deposits - total_withdrawals
            print("\nQuater 1 Gain: ", total_gain)

          if(quarter == "2"):
            total_deposits = _sum(yearly_deposits[3]) + _sum(yearly_deposits[4]) + _sum(yearly_deposits[5])
            total_withdrawals = _sum(yearly_withdrawals[3]) + _sum(yearly_withdrawals[4]) + _sum(yearly_withdrawals[5])
            total_gain = total_deposits - total_withdrawals
            print("\nQuater 2 Gain: ", total_gain)

          if(quarter == "3"):
            total_deposits = _sum(yearly_deposits[6]) + _sum(yearly_deposits[7]) + _sum(yearly_deposits[8])
            total_withdrawals = _sum(yearly_withdrawals[6]) + _sum(yearly_withdrawals[7]) + _sum(yearly_withdrawals[8])
            total_gain = total_deposits - total_withdrawals
            print("\nQuater 3 Gain: ", total_gain)

          if(quarter == "4"):
            total_deposits = _sum(yearly_deposits[9]) + _sum(yearly_deposits[10]) + _sum(yearly_deposits[11])
            total_withdrawals = _sum(yearly_withdrawals[9]) + _sum(yearly_withdrawals[10]) + _sum(yearly_withdrawals[11])
            total_gain = total_deposits - total_withdrawals
            print("\nQuater 4 Gain: ", total_gain)

      elif(user_option_choice == "9"):
        print("\nEnd.")

      else:
        print("Please enter a valid choice")
   
    else:
      print("Login failed! \n")
   
if(user_option_choice == "1"):
  signup()
elif(user_option_choice == "2"):
  login()
elif(user_option_choice == "q"):
  print("\nEnd")
else:
  print("\nPlease enter a valid choice")