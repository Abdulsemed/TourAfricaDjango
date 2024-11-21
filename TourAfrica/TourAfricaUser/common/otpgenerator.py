from random import randint

def createOTP():
    otpvalue = ""
    for _ in range(0,6):
        otpvalue += str(randint(0,9))
        
    return otpvalue
        
def verify_OTP_Template(otpvalue):
    html_content = f"""
            <html>
                <body>
                <img src= ""https://res.cloudinary.com/dwmujpiu9/image/upload/v1723810519/im4xa2jwkq3myfh77ygi.jpg"" width=100>
                <h1 style='color:#2A75EC'>Verify Your Account</h1>
                <p>To finish activating your TourAfrica account password, we just need to make sure this email address is yours.</p>
                <p>To verify your email address use this security code</p>
                <P style='font-size:20px; margin:0'><b>{otpvalue}</b></P>
                <p>If you didn't request this code, you can safely ignore this email. Someone else might have typed your email address by mistake.
                <p>Thanks,</p>
                <p>The TourAfrica Team</p>
                </body>
            </html>
            
            """
    return html_content