# -*- coding:utf-8 -*-
import requests as re
import hmac
from crypto.Cipher import AES

BS = 16


def un_pad(s):
    return s[:-ord(s[len(s)-1:])]


def change_id(card_id):
    card_id = str(card_id)
    while len(card_id) < 5:
        card_id = '0' + card_id
    return card_id


def change_key(key):
    lst = []
    seed = 37
    test = b''
    for i in key:
        lst.append((i ^ seed).to_bytes(length=1, byteorder='big'))
        seed += 13
    for i in lst:
        test += i
    return test


def decrypt(key, enc, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return un_pad(cipher.decrypt(enc))


def get_card_image_data_init():
    url = "https://api.t7s.jp/resource/images/card/l/"
    header = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0'}
    # key1 = b"3HGWxMZz6f2egL84"
    key2 = b"J9h4j5eNds+aq1=="
    key = change_key(key2)
    iv = b"0000000000000000"
    return url, header, key, iv


def get_card_image(card_id, direction, url, header, key, iv):
    card_id = change_id(card_id)
    test = hmac.new(b'J4jIkd4Nvg=8N##=', msg=('card_l_' + card_id).encode('utf-8'), digestmod='sha256')
    total = url + 'card_l_' + card_id + '_' + test.hexdigest().upper() + '.jpg.enc'
    src = re.get(total, headers=header)
    if src.text == '{"result":false,"error":{"errorMessage":"404 NOT FOUND","errorCode":2}}':
        print("%s failed." % card_id)
        return False
    else:
        cont = src.content[7:]
        data = decrypt(key, cont, iv)
        data = data[16:]
        with open(direction + 'card_l_%s.jpg' % card_id, 'wb') as f:
            f.write(data)
        print('%s Done.' % card_id)
        return True


def main():
    url, header, key, iv = get_card_image_data_init()
    for i in range(4200, 4230):
        if not get_card_image(i, 'test/', url, header, key, iv):
            break


if __name__ == "__main__":
    main()
