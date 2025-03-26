import random

def generate_otp(length=6):
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])

# Generate 10 OTPs
otp_list = [generate_otp() for _ in range(10)]
print("Generated OTPs:", otp_list)
