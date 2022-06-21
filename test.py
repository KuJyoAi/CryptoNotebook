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

mod = input('选择模式:\n1:加密密码文件\n2:解密密码文件并保存\n3:解密密码文件不保存,回显到控制台\n')
print(mod)
if mod == '1':
    if conf['Crypto']:
        print('已经加密过了!')
    else:
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
elif mod == '3':
    key = input("输入密钥:")
    if key == "":
        print("未输入密钥")
    else:
        crypto.Decrypto(key, conf)
        crypto.show(conf)
