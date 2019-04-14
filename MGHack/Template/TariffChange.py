from Template.Field import Field
from Template.CheckBox import CheckBox
from InputIO.PdfToImage import convert_pdf_to_image
from json import dumps
from os import path


class TrafficChanger:
    img = ""
    field = {}
    checkbox = {}

    def __init__(self, _dir):
        self.img = convert_pdf_to_image(path.abspath(_dir))
        self.field = {"personal_account": Field(self.img, [1920, 670, 2705, 725], 'rus'),
                      "initials": Field(self.img, [910, 2780, 2442, 2845]),
                      "date": Field(self.img, [1700, 2990, 2170, 3050]),

                      # поля из таблицы:

                      "personal_account1": Field(self.img, [215, 965, 660, 1021]),
                      "newTariff1": Field(self.img, [1450, 900, 2325, 947]),
                      "tariffDateSince1": Field(self.img, [2505, 900, 2745, 945]),
                      "Numbers11": Field(self.img, [142, 1108, 770, 1167]),
                      "connectService11": Field(self.img, [860, 1035, 2240, 1093]),
                      "connectServiceDateSince1": Field(self.img, [2505, 976, 2745, 1014]),
                      "Numbers12": Field(self.img, [142, 1180, 770, 1235]),
                      "connectService12": Field(self.img, [860, 1110, 2240, 1165]),
                      "connectServiceDateUntil1": Field(self.img, [2505, 1042, 2745, 1092]),
                      "Numbers13": Field(self.img, [142, 1250, 770, 1308]),
                      "disableService11": Field(self.img, [860, 1260, 2240, 1310]),
                      "disableServiceDateSince1": Field(self.img, [2505, 1196, 2745, 1232]),
                      "Numbers14": Field(self.img, [142, 1320, 770, 1375]),
                      "disableService12": Field(self.img, [860, 1349, 2240, 1388]),

                      "personal_account2": Field(self.img, [215, 1475, 660, 1527]),
                      "newTariff2": Field(self.img, [1450, 1400, 2325, 1455]),
                      "tariffDateSince2": Field(self.img, [2505, 1412, 2745, 1452]),
                      "Numbers21": Field(self.img, [142, 1620, 770, 1675]),
                      "connectService21": Field(self.img, [860, 1550, 2240, 1600]),
                      "connectServiceDateSince2": Field(self.img, [2505, 1484, 2745, 1524]),
                      "Numbers22": Field(self.img, [142, 1687, 770, 1745]),
                      "connectService22": Field(self.img, [860, 1620, 2240, 1670]),
                      "connectServiceDateUntil2": Field(self.img, [2505, 1540, 2745, 1596]),
                      "Numbers23": Field(self.img, [142, 1755, 770, 1816]),
                      "disableService21": Field(self.img, [860, 1771, 2240, 1822]),
                      "disableServiceDateSince2": Field(self.img, [2505, 1694, 2745, 1738]),
                      "Numbers24": Field(self.img, [142, 1825, 770, 1885]),
                      "disableService22": Field(self.img, [860, 1849, 2240, 1888]),

                      "personal_account3": Field(self.img, [215, 1985, 660, 2034]),
                      "newTariff3": Field(self.img, [1450, 1919, 2325, 1966]),
                      "tariffDateSince3": Field(self.img, [2505, 1913, 2745, 1961]),
                      "Numbers31": Field(self.img, [142, 2120, 770, 2180]),
                      "connectService31": Field(self.img, [860, 2055, 2240, 2105]),
                      "connectServiceDateSince3": Field(self.img, [2505, 1991, 2745, 2029]),
                      "Numbers32": Field(self.img, [142, 2190, 770, 2250]),
                      "connectService32": Field(self.img, [860, 2130, 2240, 2185]),
                      "connectServiceDateUntil3": Field(self.img, [2505, 2055, 2745, 2103]),
                      "Numbers33": Field(self.img, [142, 2260, 770, 2322]),
                      "disableService31": Field(self.img, [860, 2262, 2240, 2322]),
                      "disableServiceDateSince3": Field(self.img, [2505, 2211, 2745, 2245]),
                      "Numbers34": Field(self.img, [142, 2330, 770, 2392]),
                      "disableService32": Field(self.img, [860, 2340, 2240, 2393]),
                      }

        self.checkbox = {"personal_account1Bool": CheckBox(self.img, [175, 900, 209, 931]),
                         "newTariff1Bool": CheckBox(self.img, [815, 899, 845, 931]),
                         "personal_account2Bool": CheckBox(self.img, [175, 1405, 209, 1442]),
                         "connectService1Bool": CheckBox(self.img, [815, 969, 845, 1007]),
                         "personal_account3Bool": CheckBox(self.img, [175, 1910, 209, 1947]),
                         "disableService1Bool": CheckBox(self.img, [815, 1185, 845, 1217]),
                         "newTariff2Bool": CheckBox(self.img, [815, 1409, 845, 1439]),
                         "connectService2Bool": CheckBox(self.img, [815, 1479, 845, 1515]),
                         "disableService2Bool": CheckBox(self.img, [815, 1695, 845, 1727]),
                         "newTariff3Bool": CheckBox(self.img, [815, 1913, 845, 1943]),
                         "connectService3Bool": CheckBox(self.img, [815, 1985, 845, 2019]),
                         "disableService3Bool": CheckBox(self.img, [815, 2200, 845, 2235]),
                         }

    def scan(self):
        for i in self.checkbox:
            self.checkbox[i].scan()
        self.scan_n_block(1)
        self.scan_n_block(2)
        self.scan_n_block(3)


    def scan_n_block(self, n):
        if self.checkbox["personal_account" + str(n) + "Bool"].value:
            self.field["personal_account" + str(n)].scan()
        else:
            self.field["Numbers" + str(n) + "1"].scan()
            self.field["Numbers" + str(n) + "2"].scan()
            self.field["Numbers" + str(n) + "3"].scan()
            self.field["Numbers" + str(n) + "4"].scan()
        if self.checkbox["newTariff" + str(n) + "Bool"].value:
            self.field["newTariff" + str(n) + ""].scan()
        if self.checkbox["connectService" + str(n) + "Bool"].value:
            self.field["connectService" + str(n) + "1"].scan()
            self.field["connectService" + str(n) + "2"].scan()
        if self.checkbox["disableService" + str(n) + "Bool"].value:
            self.field["disableService" + str(n) + "1"].scan()
            self.field["disableService" + str(n) + "2"].scan()

    def out(self):
        print(self.field["Numbers21"].scan())
        self.field["initials"].scan()
        outDict = {"personal_account": self.field["personal_account"].value}
        outDict.update({"initials": self.field["initials"].value})
        outDict.update({"block1": self.out_n_block(1)})
        outDict.update({"block2": self.out_n_block(2)})
        outDict.update({"block3": self.out_n_block(3)})
        return dumps(outDict)

    def out_n_block(self, n):
        outDict = {}
        if self.checkbox["personal_account" + str(n) + "Bool"].value:
            outDict.update({"personal_account": self.field["personal_account" + str(n)].value})
        else:
            outDict.update({"Numbers": []})
            outDict["Numbers"].append(self.field["Numbers" + str(n) + "1"].value)
            outDict["Numbers"].append(self.field["Numbers" + str(n) + "2"].value)
            outDict["Numbers"].append(self.field["Numbers" + str(n) + "3"].value)
            outDict["Numbers"].append(self.field["Numbers" + str(n) + "4"].value)
        if self.field["newTariff" + str(n)].value != '':
            outDict.update({"NewTariff": self.field["newTariff" + str(n) + ""].value})
        if self.field["connectService" + str(n) + '1'].value != '':
            outDict.update({"connectService": [self.field["connectService" + str(n) + "1"].value + self.field["connectService" + str(n) + "2"].value, self.checkbox["connectService" + str(n) + "Bool"].value]})
        if self.field["disableService" + str(n) + '1'].value != '':
            outDict.update({"disableService": [self.field["disableService" + str(n) + "1"].value + self.field["disableService" + str(n) + "2"].value, self.checkbox["disableService" + str(n) + "Bool"].value]})
        return outDict
