# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def suma_propus(symma):
    tus = symma // 100
    os_sotni = symma % 100
    des = os_sotni // 10
    od = os_sotni % 10

    sotni = {9:"дев'ятосот", 8:"вісімсот", 7:"сімсот", 6:"шістсот" , 5:"п'ятьсот", 4:"чотириста", 3:"триста", 2:"двісті", 1:"сто" }
    desytku = {9:"дев'яностоо", 8:"вісімдесять", 7:"сімдесять", 6:"шістдесять" , 5:"п'ятдесять", 4:"сорок", 3:"тридцять", 2:"двадцять"}
    desytku_plus = {19:"дев'ятнадцять", 18:"вісімнадцять", 17:"сімнадцять", 16:"шістнадцять" , 15:"п'ятнадцять", 14:"чотирнадцять", 13:"тринадцять", 12:"дванадцять", 11:"одиннадцять", 10:"десять" }
    odunutci = {9:"дев'ять", 8:"вісім", 7:"сім", 6:"шість" , 5:"п'ять", 4:"чотир", 3:"три", 2:"дві", 1:"одна" }

    if tus != 0:
        propis.append(sotni[tus])


    if  os_sotni >= 20:
        propis.append(desytku[des])

    if 20 > os_sotni > 10 and des !=0  :
        propis.append(desytku_plus[os_sotni])
    if os_sotni == 10:
        propis.append(desytku_plus[os_sotni])

    if (os_sotni < 10 or os_sotni > 20) and od !=0:
         propis.append(odunutci[od])



def money(symma):
    if symma % 10 == 1:
        propis.append("гривня")
    elif (symma % 10 == 2 or symma % 10 == 3 or symma % 10 == 4) and (symma < 10 or symma > 20):
        propis.append("гривні")
    else:
        propis.append("гривень")



def coin(coins):
    if coins % 10 == 1:
        propis.append(str(coins))
        propis.append("копійка")
    elif (coins % 10 == 2 or coins % 10 == 3 or coins % 10 == 4) and ( coins < 10 or coins > 20 ) :
        propis.append(str(coins))
        propis.append("копійки")
    else:
        propis.append(str(coins))
        propis.append("копійок")




zagal = float(input('Enter symma -->>'))
propis = []
if zagal >= 1000:
    symma = int(zagal) // 1000
    suma_propus(symma)

    if symma % 10 == 1 and symma < 10:
        propis.append("тисяча")
    elif (symma % 10 == 2 or symma % 10 == 3 or symma % 10 == 4) and (symma < 10 or symma > 20) :
        propis.append("тисячі")
    else:
        propis.append("тисяч")

    symma = int(zagal) % 1000
    suma_propus(symma)
    money(symma)

elif zagal < 1000:
    symma = int(zagal)
    suma_propus(symma)
    money(symma)
#print(propis)
if zagal % 1 != 0:
    cop = zagal % 1 * 100
    coins = round(cop)
    coin(coins)


print(" ".join(propis))




