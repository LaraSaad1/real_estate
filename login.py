password = input("enter your password")
attempts = 5

while not any(char.isdigit() for char in password) or\
      not any(char.isupper() for char in password) or\
      not any(char.islower() for char in password)or\
      not any(not char.isalnum() for char in password) or\
      len(password) < 8 :

      attempts -= 1

      if attempts > 0:
          print("enter a valid password")
          password = input("enter your password")

      else:
          attempts == 0
          print("Your account have been locked due to too many attempts")
          break

print("Password Saved")

confirm_password = input("enter your password again")
def compare_passwords(password, confirm_password):
    if password == confirm_password:
         print("passwords match")
    else: renter_password = input("Passwords do not match renter your password")


compare_passwords(password, confirm_password)