import qrcode
print('QR CODE GENERATOR'.center(175,"-"))

link= input("Enter link: ")
qr = qrcode.QRCode()
qr.add_data(link)
qr.make(fit=True)
img = qr.make_image()
img.save('qrcode.png')
print('Image saved!')
print('QR CODE GENERATion is done'.center(175,"-"))