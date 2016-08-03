import re
def getOTPinSMS(FullString):    
    OTP = re.search( r"\d\d\d\d", FullString)
<<<<<<< HEAD
    return OTP.group()
=======
    return OTP.group()
>>>>>>> origin/master
