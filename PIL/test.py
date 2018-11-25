from PIL import Image
import tesserocr
# img = Image.open('go.jfif')
res = tesserocr.file_to_text('go.jfif')
print(res)