from Template.Warrant import Warrant
from Template.RemoteMaintenance import RemoteMaintenance
from Template.TariffChange import TrafficChanger
from Template.PersonalArea import PersonalArea
import smtplib

n = 1

file = str(n) + '.pdf'


def inpt(n, file):
    if n == 1:
        file = Warrant(file)
    elif n == '2':
        file = RemoteMaintenance(file)
    elif n == '3':
        file = TrafficChanger(file)
    elif n == '4':
        file = PersonalArea(file)
    return file


file = inpt(n, file)
file.scan()
out = file.out()


print(out)