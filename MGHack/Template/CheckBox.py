from InputIO.PdfToImage import cut_image


class CheckBox:
    img = ""
    value = False
    coord = [0, 0, None, None]

    def __init__(self, _img, _coord=[0, 0, None, None], _value=False):
        self.img = _img
        self.coord = _coord
        self.value = _value

    def scan(self):
        self.img = cut_image(self.img, self.coord)
        for i in range(0, 10):
            for j in range(0, 10):
                if self.img.getpixel((10+i, 10+j)) < 200:
                    self.value = True
                    return True
        return False
