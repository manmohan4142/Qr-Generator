import qrcode
from pyzbar.pyzbar import decode
from PIL import Image


myqr = qrcode.make("https://www.youtube.com/@GateSmashers")
myqr1 = qrcode.make("https://www.youtube.com/@AnujBhaiya")
myqr.save("myqr.png")
myqr1.save("myqr1.png")

b = decode(Image.open("myqr.png"))
print(b[0].data.decode("ascii"))