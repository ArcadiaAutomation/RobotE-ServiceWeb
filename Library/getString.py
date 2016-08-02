def getOTPinSMS(FullString):
    Index = FullString.find("OTP")
    OTP = FullString[Index+6:Index+10]
    return OTP
