import os
import openpyxl
from openpyxl.drawing.image import Image


images_dir_path = "./emblem_images"
image_files = os.listdir(images_dir_path)

wb = openpyxl.Workbook()
ws = wb["Sheet"]

columns = ["A", "E", "I"]
c = 0
r = 3

for filename in image_files:
  img = Image(f"{images_dir_path}/{filename}")
  img.width = 250
  img.height = 200

  ws.add_image(img, columns[c]+str(r))
  ws[columns[c]+str(r-2)].value = filename[:filename.index(".")]

  if c == 2:
    c = 0
    r += 14
  else:
    c += 1


wb.save("car-emblem-book.xlsx")
wb.close()

