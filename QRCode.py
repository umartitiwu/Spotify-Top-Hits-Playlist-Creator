import qrcode
import os

# Replace this with your playlist URL
playlist_url = '*'

# Create a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(playlist_url)
qr.make(fit=True)

# Create an image from the QR Code instance
img = qr.make_image(fill='black', back_color='white')

# Ensure the output directory exists
output_dir = r'path'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Save the image to the specified directory
img_path = os.path.join(output_dir, 'spotify_playlist_qr.png')
img.save(img_path)

print(f"QR code generated and saved as {img_path}")
