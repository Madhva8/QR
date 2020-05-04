#Generate QR code and save the image file in .png extension 
import qrcode #importing modules
qr = qrcode.QRCode( 
    version = 1,
    box_size= 90,
    border=4
)
data = '' #enter website or web links in '' for eg. 'https://google.com'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill='black',back_color='white')
img.save('') #enter the name of file with .png extension for eg 'sample.png'