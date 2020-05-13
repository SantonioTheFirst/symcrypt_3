from datetime import datetime
import numpy as np

def text_to_numbers(string):
    numbers = []
    length = len(string)
    for i in np.arange(0, length):
        # if(i % 50000 == 0):
        #     print(i)
        if string[i] == 'а':
            numbers.append(0)
        elif string[i] == 'б':
            numbers.append(1)
        elif string[i] == 'в':
            numbers.append(2)
        elif string[i] == 'г':
            numbers.append(3)
        elif string[i] == 'д':
            numbers.append(4)
        elif string[i] == 'е':
            numbers.append(5)
        elif string[i] == 'ё':
            numbers.append(5)
        elif string[i] == 'ж':
            numbers.append(6)
        elif string[i] == 'з':
            numbers.append(7)
        elif string[i] == 'и':
            numbers.append(8)
        elif string[i] == 'й':
            numbers.append(9)
        elif string[i] == 'к':
            numbers.append(10)
        elif string[i] == 'л':
            numbers.append(11)
        elif string[i] == 'м':
            numbers.append(12)
        elif string[i] == 'н':
            numbers.append(13)
        elif string[i] == 'о':
            numbers.append(14)
        elif string[i] == 'п':
            numbers.append(15)
        elif string[i] == 'р':
            numbers.append(16)
        elif string[i] == 'с':
            numbers.append(17)
        elif string[i] == 'т':
            numbers.append(18)
        elif string[i] == 'у':
            numbers.append(19)
        elif string[i] == 'ф':
            numbers.append(20)
        elif string[i] == 'х':
            numbers.append(21)
        elif string[i] == 'ц':
            numbers.append(22)
        elif string[i] == 'ч':
            numbers.append(23)
        elif string[i] == 'ш':
            numbers.append(24)
        elif string[i] == 'щ':
            numbers.append(25)
        elif string[i] == 'ъ':
            numbers.append(26)
        elif string[i] == 'ы':
            numbers.append(27)
        elif string[i] == 'ь':
            numbers.append(26)
        elif string[i] == 'э':
            numbers.append(28)
        elif string[i] == 'ю':
            numbers.append(29)
        elif string[i] == 'я':
            numbers.append(30)
        # elif string[i] == ' ':
        #     numbers.append(31)
        # else:
        #     numbers.append(31)
    numbers_np = np.array(numbers)
    return numbers_np

def numbers_to_text(numbers_array):
    string = ''
    for i in np.arange(0, len(numbers_array)):
        if numbers_array[i] == 0:
            string += 'а'
        elif numbers_array[i] == 1:
            string += 'б'
        elif numbers_array[i] == 2:
            string += 'в'
        elif numbers_array[i] == 3:
            string += 'г'
        elif numbers_array[i] == 4:
            string += 'д'
        elif numbers_array[i] == 5:
            string += 'е'
        elif numbers_array[i] == 6:
            string += ('ж')
        elif numbers_array[i] == 7:
            string += ('з')
        elif numbers_array[i] == 8:
            string += ('и')
        elif numbers_array[i] == 9:
            string += ('й')
        elif numbers_array[i] == 10:
            string += ('к')
        elif numbers_array[i] == 11:
            string += ('л')
        elif numbers_array[i] == 12:
            string += ('м')
        elif numbers_array[i] == 13:
            string += ('н')
        elif numbers_array[i] == 14:
            string += ('о')
        elif numbers_array[i] == 15:
            string += ('п')
        elif numbers_array[i] == 16:
            string += ('р')
        elif numbers_array[i] == 17:
            string += ('с')
        elif numbers_array[i] == 18:
            string += ('т')
        elif numbers_array[i] == 19:
            string += ('у')
        elif numbers_array[i] == 20:
            string += ('ф')
        elif numbers_array[i] == 21:
            string += ('х')
        elif numbers_array[i] == 22:
            string += ('ц')
        elif numbers_array[i] == 23:
            string += ('ч')
        elif numbers_array[i] == 24:
            string += ('ш')
        elif numbers_array[i] == 25:
            string += ('щ')
        elif numbers_array[i] == 26:
            string += ('ь')
        elif numbers_array[i] == 27:
            string += ('ы')
        elif numbers_array[i] == 28:
            string += ('э')
        elif numbers_array[i] == 29:
            string += ('ю')
        elif numbers_array[i] == 30:
            string += ('я')
        # elif numbers_array[i] == 31:
        #     string += (' ')
    return string

def get_numbers_from_X(X):
    numbers = []
    x0 = 0
    x1 = 0
    for item in X:
        x0 = np.floor(item / 31)
        x1 = item - x0 * 31
        numbers.append(x0)
        numbers.append(x1)
    numbers_np = np.array(numbers)
    return numbers_np

def get_X_from_numbers(numbers):
    X = []
    if len(numbers) % 2 == 0:
        for i in np.arange(0, len(numbers), 2):
            X.append(numbers[i] * 31 + numbers[i + 1])#       print(numbers[i : i + 2], i)
    elif len(numbers) % 2 == 1:
        numbers = np.append(numbers, 20)# np.random.randint(0, 32, 1))
        for i in np.arange(0, len(numbers), 2):
            X.append(numbers[i] * 31 + numbers[i + 1])
    X_np = np.array(X)
    return X_np

def mod(number):
    if number > 961:
        while number >= 961:
            number %= 961
    elif number < 0:
        while number < 0:
            number += 961
    else:
        number = 0
    return number

def bezout(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)

def encrypt(X, key):
    Y = []
    for item in X:
        Y.append(mod((key[0] * item) + key[1]))
    Y_np = np.array(Y)
    return Y_np

def decrypt(Y, key):
    a = bezout(key[0], 961)[0]
    b = key[1]
    X = []
    for item in Y:
        X.append(mod(a * (item - b)))
    X_np = np.array(X)
    return X_np

a = int(input('A: '))
b = int(input('B: '))
key = np.array([a, b])
print(key)

start = datetime.now()
print(start)
# file = open('karenina_result.txt', 'r')
# print('File open ok!', datetime.now())
string = 'тесттест'
# print('File read ok!', datetime.now())
string.replace(' ', '')
# print('Text filtering ok!', datetime.now())
# file.close()
# print('File close ok!', datetime.now())
string = text_to_numbers(string)
print('Text to numbers ok!', datetime.now())
# print('Numbers: ', string)
# print('X: ', get_X_from_numbers(string))
X = get_X_from_numbers(string)
print('Get X ok!', datetime.now())
encrypted = encrypt(X, key)
print(numbers_to_text(get_numbers_from_X(encrypted)))
print('Encrypted ok!', datetime.now())
print(numbers_to_text(get_numbers_from_X(decrypt(encrypted, key))))
print('Decrypt ok!', datetime.now())
# print(numbers_to_text(get_numbers_from_X(decrypt(encrypt(get_X_from_numbers(string), key), key))))

print(datetime.now() - start)
