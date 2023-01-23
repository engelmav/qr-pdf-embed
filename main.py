import fitz
import pdfplumber
input_file = "/home/vengelmann/Downloads/OL996.pdf"
doc = fitz.open(input_file)
page = doc[0]
page.clean_contents()
# define the position (upper-right corner)
top_lefts =     [(1, 1), (150, 150)]
bottom_rights = [(100, 100), (250, 250)]
# for n in range(0,1):
#     image_rectangle = fitz.Rect(top_lefts[n], bottom_rights[n])
xs_and_ys = [(90, 50), (190, 150)]
x0 = 90
y0 = 50
x1 = 190
y1 = 150
row_count = 0
column_count = 0
for n in range(0,10):
    image_rectangle = fitz.Rect(
        # 90,  # x0 translates left side x points from the left
        # 50,  # y0 seems to move bottom. the smaller the number, the further down it goes
        # 190, # x1 translates right side x points from the left
        # 150) # y1 seems to move top. the higher the number, the higher up it goes
        x0, y0, x1, y1)
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
    # if we go across the page, the y stays the same, only the xs change
    # x0 += 100
    # # y0 += 100
    #
    # # if we go down the page, the x stays the same, only the ys change
    # x1 += 100
    # # y1 += 100


doc.save(input_file+"_new.pdf")
print(page)



#
# with pdfplumber.open("/home/vengelmann/Downloads/OL996.pdf") as pdf:
#    first_page = pdf.pages[0]
#    print(first_page.objects)
