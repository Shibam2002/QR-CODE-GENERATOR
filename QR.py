import qrcode as qr
print("THIS IS A QR CODE GENERATOR")
link=input("Enter the link to generate QR CODE : ")
CODE=qr.make(link)
create=input("GIVE THE FILE NAME :")
CODE.save(create)