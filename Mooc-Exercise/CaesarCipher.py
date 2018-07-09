# 该程序一共有三种模式，分别为加密模式、解密模式和暴力破解。暴力破解模式将列出全部26种可能。


MAX_KEY_SIZE = 26

def getMode():
    while True:
        print('请选择加密或解密模式,或者选择暴力破解：')
        print('加密:encrypt(e)')
        print('解密:decrypt(d)')
        print('暴力破解:brute(b)')
        mode = input().lower()
        if mode in 'encrypt e decrypt d brute b'.split():
            return mode
        else:
            print('请输入"encrypt"或"e"或"decrypt"或"d"或"brute"或"b"!')






def getMessage():      #获取输入信息
    print('请输入你的信息：')
    return input()




#获取加密要求
def getKey():
    key = 0
    while True:
        print('请输入密钥数字(1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >=1 and key <= MAX_KEY_SIZE):
            return key




#加键
def getTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        if symbol.isalpha():
            num = ord(symbol)
            num += key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

            translated += chr(num)
        else:
            translated += symbol
    return translated




mode = getMode()
message = getMessage()
if mode[0] != 'b':
    key = getKey()




print("你要翻译的信息是:")
if mode[0] != 'b':
    print(getTranslatedMessage(mode, message, key))
else:
    for key in range(1, MAX_KEY_SIZE + 1):
        print(key, getTranslatedMessage('decrypt', message, key))
