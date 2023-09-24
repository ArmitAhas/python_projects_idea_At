import pyqrcode
import png

url="https://www.wikipedia.org/"
myqrcode = pyqrcode.create(url)


myqrcode.show(scale=8)
myqrcode.png("myqr.png",scale=8)
