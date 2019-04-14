from wand.image import Image
from wand.image import Color
from pytesseract.pytesseract import image_to_string
import PIL.Image
from numpy import asarray
from io import BytesIO


def convert_pdf_to_image(pdf):
    with Image(filename=pdf, resolution=350) as img:
        with Image(width=img.width, height=img.height, background=Color("white")) as bg:
            bg.composite(img, 0, 0)                      # Из пдфки пихаем в картинку
            img_buffer = asarray(bytearray(bg.make_blob(format='jpeg')), dtype='uint8')
            bytesio = BytesIO(img_buffer)
            return PIL.Image.open(bytesio)


def cut_image(image, coord=[0, 0, None, None]):
    image = image.crop(tuple(coord))
    image.save("1.jpeg")
    return image


def img_to_str(image, lang="rus"):
    return image_to_string(image, lang)                  #С помощью обученной рекуррентное нейронной
                                                         # сети с долгой краткосрочной памятью парсим картинку


def img2str(image, coord=[0, 0, None, None], lang="rus"):           #PDF в картинку
    return img_to_str(cut_image(image, coord), lang)     #Возвращаем текст из картинки
