from InputIO.PdfToImage import img2str


class Field:
    pdf = ""
    value = ""
    coord = [0, 0, None, None]
    lang = "rus"

    def __init__(self, _img, _coord=[0, 0, None, None], _lang="rus", _value=""):
        self.img = _img
        self.coord = _coord
        self.lang = _lang
        self.value = _value

    def scan(self):
        self.value = img2str(self.img, self.coord, self.lang)
        return self.value
