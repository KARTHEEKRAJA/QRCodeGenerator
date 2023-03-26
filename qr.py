import pyqrcode

def qrcode():
    q = pyqrcode.create(input("Please Provide Information In Text Format : "))
    q.png("qrcode.png",scale=6)
    print("QR Code is generated Successfully")


if __name__ == "__main__":
    qrcode()

