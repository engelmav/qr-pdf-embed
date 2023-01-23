import fitz
import pdfplumber
input_file = "/home/vengelmann/Downloads/OL996.pdf"
doc = fitz.open(input_file)
page = doc[0]
page.clean_contents()
x0 = 90
y0 = 40
x1 = 190
y1 = 140
row_count = 0
column_count = 0
for n in range(0,10):
    image_rectangle = fitz.Rect(x0, y0, x1, y1)
    page.insert_image(image_rectangle, filename="/home/vengelmann/test.png")
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
