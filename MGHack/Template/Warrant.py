from Template.Field import Field
from Template.CheckBox import CheckBox
from InputIO.PdfToImage import convert_pdf_to_image
from json import dumps
from os import path


class Warrant:
    img = ""
    checkbox = {}
    field = {}
    image = ""

    def __init__(self, _dir):
        self.img = convert_pdf_to_image(path.abspath(_dir))
        self.field = {"personal_account": Field(self.img, [1927, 321, 2756, 401]),  # Поле лицевого счета
                      "representative": Field(self.img, [1311, 1022, 2515, 1078]),  # Поле представителя
                      "signature": "",  # Поле подписи
                      "date": Field(self.img, [1790, 3725, 2280, 3788])}  # Поле даты

        self.checkbox = {"communicationContract": CheckBox(self.img, [283, 1923, 316, 1955]),
                         "blockOrRecover": CheckBox(self.img, [283, 2050, 316, 2082]),
                         "failureToUse": CheckBox(self.img, [283, 2136, 316, 2167]),
                         "replacementSim": CheckBox(self.img, [283, 2207, 316, 2238]),
                         "ChangePlans": CheckBox(self.img, [283, 2276, 316, 2307]),
                         "connectionExtraServices": CheckBox(self.img, [283, 2344, 316, 2376]),
                         "receiptOfAccountingDocs": CheckBox(self.img, [283, 2447, 316, 2479]),
                         "billDetail": CheckBox(self.img, [283, 2584, 316, 2617]),
                         "CredentialChange": CheckBox(self.img, [283, 2688, 316, 2720]),
                         "renewalContract": CheckBox(self.img, [283, 2757, 316, 2790]),
                         "terminationAgreement": CheckBox(self.img, [283, 2829, 316, 2860]),
                         "cashTransfer": CheckBox(self.img, [283, 2898, 316, 2930]),
                         "gettingValues": CheckBox(self.img, [283, 2966, 316, 2998]),
                         "equipmentContract": CheckBox(self.img, [283, 3034, 316, 3066]),
                         }

    def scan(self):
        for i in self.checkbox:
            self.checkbox[i].scan()
        field = self.field
        del field["signature"]
        for i in self.field:
            self.field[i].scan()

    def out(self):
        outDict = {}
        outDict.update({"personal_account": self.field["personal_account"].value})
        outDict.update({"representative": self.field["representative"].value})
        outBoolDict = {"bool": {}}
        for i in self.checkbox:
            outBoolDict["bool"].update({i: self.checkbox[i].value})
        outDict.update(outBoolDict)
        return dumps(outDict)
