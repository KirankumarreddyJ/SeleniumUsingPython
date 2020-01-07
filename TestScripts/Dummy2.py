#int('jhj')

from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
# driver = Chrome(executable_path = "..\Drivers\chromedriver.exe")
# driver.implicitly_wait(20)
# driver.maximize_window()
# driver.back()
#
# driver.get('https://www.thetestingworld.com/testings/')
# try:
#     driver.find_element_by_xpath('//div[@id="tab-content1"]/div/span').text
#
# except NoSuchElementException as exception:
#     print("Element not found and test failed");
#import TestScripts.Dummy
#print()
# import base64
# import os
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.fernet import Fernet
#
# password_provided = "password" # This is input in the form of a string
# password = password_provided.encode() # Convert to type bytes
# salt = b'salt_' # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
# kdf = PBKDF2HMAC(
#     algorithm=hashes.SHA256(),
#     length=32,
#     salt=salt,
#     iterations=100000,
#     backend=default_backend()
# )
# key = base64.urlsafe_b64encode(kdf.derive(password)) # Can only use kdf once
# def encrypt(key, message):
#     f = Fernet(key)
#     message = message.encode()
#     encrypted = f.encrypt(message)
#     return encrypted
#
# def decrypt(key, encrypted):
#     f = Fernet(key)
#     decrypted = f.decrypt(encrypted)
#     return decrypted
#
# message = input("Enter the password")
# encrypted_mes = encrypt(key,message)
# print(encrypted_mes)
# print(type(encrypted_mes))
# decrypted_mes = decrypt(key,encrypted_mes)
# print(decrypted_mes)

# encode = 'gAAAAABdTy6dNK-9W6UcYU7v8E-2hnFHm0rUF_ElYDj2JSWUXu14hkT4Vkm1TzC5F_l_o2Wg07sMmTymWM-4d-49RZok_j9AnQ=='
# print(decrypt(key,encode))
try:
    raise Exception
except:
    print('exception')