# SYNC Interns - Task 2 - OTP Verification Using Python 

import random

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp(otp):
    print(f"OTP: {otp}")

def verify_otp(otp, user_input):
    return otp == user_input

def main():
    print("OTP Verification Example")

    otp = generate_otp()
    send_otp(otp)
    
    user_input = input("Enter the OTP you received: ")

    if verify_otp(otp, user_input):
        print("OTP verification successful! Access granted.")
    else:
        print("OTP verification failed! Access denied.")

if __name__ == "__main__":
    main()



