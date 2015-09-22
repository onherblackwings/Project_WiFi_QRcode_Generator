import os, random, string,io
import pyqrcode
import png
import time
import base64

os.system('cls')

def intro():
    time.sleep(.5)
    SSID_name=raw_input("First, enter your router SSID: ")
    print " "
    return SSID_name


def timer():
    print "."
    time.sleep(.5)
    print".."
    time.sleep(.6)
    print "..."
    time.sleep(.7)

def password_length():
    print "Next, you will decide how many characters your password will have."
    time.sleep(.5)
    print "(Hint: 10 characters seems fine but go ahead and knock yourself out."
    password_length=input("number of characters> ")
    return password_length    


def passwordmaker(password_length):
    c=''
    chars = string.ascii_letters + string.digits + '+/'
    for i in range(password_length):
        c=c+chars[ord(os.urandom(1))%len(chars)]
    return c	

def qrcodemaker(SSID_name,password,qr_filename):
	my_code=pyqrcode.create("SSID: "+SSID_name+" Password: "+password)
	with open(qr_filename+'.jpg','w') as fstream:
		my_code.png(fstream, scale=5)

		my_code.png(qr_filename+'.jpg',scale=5)
		buffer=io.BytesIO()
		my_code.png(buffer)
		print(list(buffer.getvalue()))

def qr_filename(SSID_name,password):
    print "....Your new random generated password for SSID %s is: %s " %(SSID_name,password)
    qr_filename=raw_input("Enter filname to save your qrcode ")
    return qr_filename
		
               

        
SSID_name=intro()
password_length=password_length()
password=passwordmaker(password_length)
timer()
qr_filename=qr_filename(SSID_name,password)
qrcodemaker(SSID_name,password,qr_filename)
timer()
print "....password of SSID "+SSID_name+" has been saved under filename: "+qr_filename.upper()+'.png'.upper()



