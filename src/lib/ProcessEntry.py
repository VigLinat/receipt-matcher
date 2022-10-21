import re

def insertDot(target: str, fixedPoint: int) -> str:
    result = target
    if '.' not in target: 
        dotPosition = len(target)-fixedPoint
        result = target[0:dotPosition] + '.' + target[dotPosition:]
    return result

def trimSpaceAndReplaceComma(target: str) -> str:
    trimSpace = re.compile(r''' +''')
    replaceComma = re.compile(r'''[,]''')

    trimmed = trimSpace.sub('', target) # all occurences are replaced 
    result = replaceComma.sub('.', trimmed) # all occurences are replaced 
    
    return result

def processEntry(entry: tuple) -> tuple:
    '''
    Обработка позиции в чеке.
    Замены:  
        1. Убрать последний пробел в названии продутка [0]
        2. Убрать все пробелы из цены [1] и количества [2]
        3. Все запятые в ценах и количествах заменить на точки 

    Добавления: 
    1. Если в цене/весе нет точки, то добавить точку: 
        a. Если исправляем цену, то добавить точку перед _двумя_ последними цифрами 
        b. Если исправляем вес, то добавить точку перед _тремя_ последними цифрами
    '''
    trimEndSpace = re.compile(r'''( \Z)+''')
    name = trimEndSpace.sub('', entry[0])

    price = trimSpaceAndReplaceComma(entry[1])
    qty = trimSpaceAndReplaceComma(entry[2])

    price = insertDot(price, 2)
    if len(qty) >= 4:
        qty = insertDot(qty, 3)

    return (name, price, qty)