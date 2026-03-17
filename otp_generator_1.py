import random
import smtplib
from email.message import EmailMessage
def generate_otp(length=6):
    digits = "0123456789"
    otp = "".join(random.choice(digits) for _ in range(length))
    return otp
# print(generate_otp())
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login('pruthvishkulkarni14@gmail.com', 'etqq qkyy mlhq voxu')
otp = generate_otp()
# message = f"Your OTP is: {otp}"
recipient_email = input("Enter the recipient's email address: ")
msg = EmailMessage()
msg.set_content(message)
msg['Subject'] = 'Your OTP Code'
msg['From'] = 'pruthvishkulkarni14@gmail.com'
msg['To'] = recipient_email
server.send_message(msg)
print(f"OTP sent to {recipient_email}")
entered_otp = input(f"Enter the OTP you received: ")
if entered_otp == otp:
    print("OTP verified successfully!")
else:
    print("Invalid OTP.")
server.quit()

