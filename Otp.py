import random
import math
def otpGenerate():
    digit="0123456789" #digit variable
  
    otp="" # variable to store otp

    for i in range(4):
        otp=otp+digit[math.floor(random.random()*10)]
    return otp

def strOTP():
    string="abcdefghij"
    OTP=""
    for i in range(5):
        OTP=OTP+string[math.floor(random.random()*len(string))]
    return OTP
if __name__=="__main__":
    print("OTP",otpGenerate())
    print(strOTP())

