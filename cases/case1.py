from LoginOut import login_out
from selenium import webdriver
import unittest
import os, csv


with open('/Users/shirleyxu/PycharmProjects/SME/Datas/IP.txt', 'r') as address:
    ip = address.readlines()

username = []
password = []
'''
方法一：
调用csv.reader()方法，读取CSV内容，按照每行返回数组
自己加了dict(zip())再转成字典
'''
# with open('/Users/shirleyxu/PycharmProjects/SME/Datas/users_info.csv', 'r') as accounts:
#     users = csv.reader(accounts)
#     for user in users:
#         username.append(user[0])
#         password.append(user[1])
#
# users = dict(zip(username, password))

'''
方法二:
当csv文件中第一行为列头，需要忽略第一行数据
'''
with open('/Users/shirleyxu/PycharmProjects/SME/Datas/users_info.csv', 'r') as csvfile:
    accounts = csv.DictReader(csvfile)
    users = [row for row in accounts]

print(users[admin])



# ip = '172.20.3.160'
# name = 'admin'
# pwd = '123123'
#
# driver = webdriver.Chrome()
# mylogin = login_out(ip, driver)
# mylogin.login(name, pwd)
#
