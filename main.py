import fitz
from qrcode import QRCode

from concat import concat

QR_IMAGE_PATH = "/home/vengelmann/Documents/_CodingInEnglish/flyer_labels/pineberry_qr.png"
CONCAT_IMAGE = "/home/vengelmann/Documents/_CodingInEnglish/flyer_labels/full_label.png"

qr = QRCode(version=1)
qr.add_data("https://www.codinginenglish.com/?a=33da1598")

qr_image = qr.make_image()
# qr_image.show()
qr_image_lg = qr_image.resize((1250, 1250))
qr_image_lg.save(QR_IMAGE_PATH)

LABEL_TEXT_IMAGE_PATH = "/home/vengelmann/Documents/_CodingInEnglish/flyer_labels/label_text.png"

concatenated_image = concat(QR_IMAGE_PATH, LABEL_TEXT_IMAGE_PATH)
concatenated_image.save(CONCAT_IMAGE)

input_file = "/home/vengelmann/Documents/_CodingInEnglish/flyer_labels/OL996.pdf"
doc = fitz.open(input_file)
page = doc[0]
page.clean_contents()
x0 = 90
y0 = -20
x1 = 190
y1 = 140
row_count = 0
column_count = 0
for n in range(0,10):
    image_rectangle = fitz.Rect(x0, y0, x1+100, y1+70)
    page.insert_image(image_rectangle, filename=CONCAT_IMAGE)
    column_count += 1
    if column_count <= 1:
        x0 += 230
        x1 += 230
    if column_count > 1:
        x0 -= 230
        x1 -= 230
        y0 += 150
        y1 += 150
        column_count = 0


doc.save(input_file+"_new.pdf")
