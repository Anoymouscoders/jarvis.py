import qrcode

qr=qrcode.QRCode(
    version=1,
    box_size =10,
    border=5
)
img_counter= 0
data =input("Enter the data here:")
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("QRCODE//qr{}.png" .format(img_counter))
img_counter+=1
