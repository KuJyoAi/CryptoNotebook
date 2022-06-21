import json
import crypto

# 读取文件并载入配置文件
file_obj = open('.\\conf.json')
file_data = file_obj.read()
file_obj.close()
# print(file_data)
# 配置
conf = json.loads(file_data)
# print(conf)


mod = input('选择模式:\n1:加密密码文件\n2:解密密码文件并保存\n')
print(mod)
if mod == '1':
    key = input("输入密钥:")
    if key == "":
        print("未输入密钥")
    else:
        crypto.Crypto(key, conf)
elif mod == '2':
    key = input("输入密钥:")
    if key == "":
        print("未输入密钥")
    else:
        crypto.Decrypto(key, conf)
