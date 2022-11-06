import qrcode
from time import sleep

qr = qrcode.QRCode(
    version=1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)

print("\033[33m****** Gerador QRcode ******\033[m")
URL = input("Insira a URL: ")
print("\nAguarde...")
sleep(2)

qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')

print("\nQRcode gerado com sucesso!")
