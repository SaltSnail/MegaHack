from Template.Field import Field
from Template.CheckBox import CheckBox
from InputIO.PdfToImage import convert_pdf_to_image
from json import dumps
from os import path


class PersonalArea:
    img = ""
    field = {}
    checkbox = {}

    def __init__(self, _dir):
        self.img = convert_pdf_to_image(path.abspath(_dir))
        self.field = {"Number1": Field(self.img, [220, 1287, 1020, 1375]),
                      "Number2": Field(self.img, [220, 1390, 1020, 1465]),
                      "Number3": Field(self.img, [220, 1483, 1020, 1559]),
                      "initials": Field(self.img, [1035, 2605, 2280, 2675]),
                      "date": Field(self.img, [1795, 2823, 2505, 2877])}

        self.checkbox = {"personal_account": CheckBox(self.img, [170, 923, 201, 960]),
                         "Number1Bool": CheckBox(self.img, [1565, 1315, 1603, 1350]),
                         "Number2Bool": CheckBox(self.img, [1565, 1407, 1603, 1443]),
                         "Number3Bool": CheckBox(self.img, [1565, 1497, 1603, 1535])}

    def scan(self):
        for i in self.checkbox:
            self.checkbox[i].scan()

        if self.checkbox["personal_account"].value:
            self.field["Number1"].scan()
            self.field["Number2"].scan()
            self.field["Number3"].scan()

        self.field["initials"].scan()

    def out(self):
        outDict = {"initials": [self.field["initials"].value, not self.checkbox["personal_account"].value]}
        if self.checkbox["personal_account"].value:
            outDict.update({"Numbers": []})
            if self.field["Number1"].value != '':
                outDict["Numbers"].append([self.field["Number1"].value, self.checkbox["Number1Bool"].value])
            if self.field["Number2"].value != '':
                outDict["Numbers"].append([self.field["Number2"].value, self.checkbox["Number2Bool"].value])
            if self.field["Number3"].value != '':
                outDict["Numbers"].append([self.field["Number3"].value, self.checkbox["Number3Bool"].value])
        return dumps(outDict)
