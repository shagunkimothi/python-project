import qrcode
img=qrcode.make("https://www.example.com")
img.save("qrcode.png")
from PIL import Image

qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code, 1 is the smallest
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # about 7% or less error correction
    box_size=10,  # size of each box in pixels
    border=15,  # thickness of the border
)

# Add data to the QR code
qr.add_data("https://www.example.com")
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# Save the image file
img.save("custom_qrcode.png")

# Display the image
img.show()



