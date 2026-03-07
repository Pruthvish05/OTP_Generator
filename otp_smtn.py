import random
otp = random.randint(10000, 99999)
print("Your OTP is:", otp)
while True:
    user_input = input("Enter the OTP: ")
    if user_input == str(otp):
        print("OTP verified successfully!")
        break
    else:
        print("Incorrect OTP. Please try again.")