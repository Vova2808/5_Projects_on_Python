import pyshorteners
import pyqrcode
from pyqrcode import QRCode
import os

s=pyshorteners.Shortener()
url = str(input("Ссылка которую нужно сократить:"))

print(s.tinyurl.short(url))

url_qr = pyqrcode.create(url)
url_qr.svg("qr_code.svg", scale = 8)
os.system("qr_code.svg")