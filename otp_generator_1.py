import random
def generate_otp(length=6):
    otp = random.randint(10**(length-1), 10**length - 1)
    return otp

