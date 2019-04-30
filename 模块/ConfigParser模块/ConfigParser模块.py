#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 17:18
# @Author   : 洪松
# @File     : ConfigParser模块.py

import configparser

'''
该模块适用于配置文件的格式与windows ini文件类似，可以包含一个或多个节（section），每个节可以有多个参数（键=值）。
'''

#写入配置文件
config = configparser.ConfigParser()

config["DEFAULT"] = {'ServerAliveInterval': '45',
                      'Compression': 'yes',
                     'CompressionLevel': '9',
                     'ForwardX11':'yes'
                     }

config['bitbucket.org'] = {'User':'hg'}

config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}

with open('example.ini', 'w') as configfile:

   config.write(configfile)

#从配置文件里面读
# config.read('example.ini')
# print(config.sections())#['bitbucket.org', 'topsecret.server.com']
# print(config.defaults())#OrderedDict([('serveraliveinterval', '45'), ('compression', 'yes'), ('compressionlevel', '9'), ('forwardx11', 'yes')])
# print(config['bitbucket.org']['User'])#hg

# for key in config['bitbucket.org']:
#     print(key)


#改写
config.remove_section('topsecret.server.com')
print(config.has_section('topsecret.server.com'))#False
config.remove_option('DEFAULT','forwardx11')

config.set('bitbucket.org','User','hongsong')


config.write(open('example_1.ini','w'))

