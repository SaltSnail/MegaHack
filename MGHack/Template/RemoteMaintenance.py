from Template.Field import Field
from Template.CheckBox import CheckBox
from InputIO.PdfToImage import convert_pdf_to_image
from json import dumps
from os import path


class RemoteMaintenance:
    img = ""
    field = {}
    checkbox = {}

    def __init__(self, _dir):
        self.img = convert_pdf_to_image(path.abspath(_dir))
        self.field = {"personal_account1": Field(self.img, [996, 1635, 2800, 1700]),
                      "personal_account2": Field(self.img, [140, 1720, 2670, 1779]),
                      "codeword": Field(self.img, [140, 1870, 1575, 1935]),
                      "EMail1": Field(self.img, [140, 2180, 1200, 2243], "eng"),
                      "EMail2": Field(self.img, [140, 2250, 1200, 2334], "eng"),
                      "EMail3": Field(self.img, [140, 2360, 1200, 2425], "eng"),
                      "EMail4": Field(self.img, [140, 2450, 1200, 2517], "eng"),
                      "EMail5": Field(self.img, [140, 2540, 1200, 2608], "eng")}

        self.checkbox = {"codeWordBool": CheckBox(self.img, [2239, 1890, 2275, 1920]),
                         "EMail1Bool": CheckBox(self.img, [1875, 2190, 1912, 2228]),
                         "EMail2Bool": CheckBox(self.img, [1875, 2280, 1912, 2319]),
                         "EMail3Bool": CheckBox(self.img, [1875, 2372, 1912, 2410]),
                         "EMail4Bool": CheckBox(self.img, [1875, 2463, 1912, 2502]),
                         "EMail5Bool": CheckBox(self.img, [1875, 2554, 1912, 2593])}

    def scan(self):
        if self.checkbox["codeWordBool"].scan():
            for i in self.checkbox:
                self.checkbox[i].scan()

            for i in self.field:
                self.field[i].scan()

            return None

        self.field["personal_account1"].scan()
        self.field["personal_account2"].scan()


    def out(self):
        personal_account = (self.field["personal_account1"].value + self.field["personal_account2"].value).replace(";", ",")
        outDict = {"personal_account": (personal_account.split(","))}
        outDict.update({"codeword": self.field["codeword"].value, "codeWordBool": self.checkbox["codeWordBool"].value})
        if self.checkbox["codeWordBool"].value:
            outDict.update({"Email": []})
            if self.field["EMail1"].value != '':
                outDict["Email"].append([self.field["EMail1"].value, self.checkbox["EMail1Bool"].value])
            if self.field["EMail2"].value != '':
                outDict["Email"].append([self.field["EMail2"].value, self.checkbox["EMail2Bool"].value])
            if self.field["EMail3"].value != '':
                outDict["Email"].append([self.field["EMail3"].value, self.checkbox["EMail3Bool"].value])
            if self.field["EMail4"].value != '':
                outDict["Email"].append([self.field["EMail4"].value, self.checkbox["EMail4Bool"].value])
            if self.field["EMail5"].value != '':
                outDict["Email"].append([self.field["EMail5"].value, self.checkbox["EMail5Bool"].value])
        return dumps(outDict)
