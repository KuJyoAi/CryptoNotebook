import sm4
import hashlib


def Crypto(key, conf):
    path = conf['Path']
    try:
        fr = open(path, 'r', encoding='utf8')
        data = fr.read()
        fr.close()
    except:
        print("读取文件错误")

    try:
        enc_data = crypto_sm4(key, data)
    except:
        print("加密发生错误")
    else:
        print("加密成功")
        fw = open(path, 'w', encoding='utf8')
        fw.write(enc_data)
        fw.close()
    # print(path)


def Decrypto(key, conf):
    path = conf['Path']
    try:
        fr = open(path, 'r', encoding='utf8')
        data = fr.read()
        fr.close()
    except:
        print("打开密码文件错误")

    try:
        enc_data = decrypto_sm4(key, data)
    except:
        print("解密错误")
    else:
        fw = open(path, 'w', encoding='utf8')
        print("解密成功")
        fw.write(enc_data)
        fw.close()


def show(conf):
    path = conf['Path']
    fr = open(path, 'r')
    data = fr.read()
    fr.close()
    print(data)


def crypto_sm4(key, data):
    """
    使用国密算法SM4
    :param key:密钥
    :param data:要加密的文本
    :return:返回加密后的文本数据
    """
    s = sm4.SM4()
    key = hashlib.md5(key.encode('utf8')).hexdigest()
    res = s.encryptSM4(key, data)
    return res


def decrypto_sm4(key, data):
    """
    使用国密算法SM4
    :param key:密钥
    :param data:要解密的文本
    :return:返回解密后的文本数据
    """
    s = sm4.SM4()
    key = hashlib.md5(key.encode('utf8')).hexdigest()
    res = s.decryptSM4(key, data)
    return res
