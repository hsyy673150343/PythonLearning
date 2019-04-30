#！/usr/bin/env python
# -*- coding:utf8 -*-
# @TIME     : 20:56
# @Author   : 洪松
# @File     : re模块.py


# s = 'hello world'
'''
string提供的方法是完全匹配
'''
# print(s.find('llo'))
# ret = s.replace('ll','xx')
# print(ret)
# print(s.split(' '))


'''
引入正则表达式---->模糊匹配
#元字符：. ^ $ * + ? { } [ ] | ( ) \
'''

import re

ret = re.findall('hong','hongsongyangyang')
print(ret)

'''
. 通配符
'''
ret = re.findall('w..l','hello world')#.只能代指任意一个字符
print(ret)
ret = re.findall('w.l','hello w\nld')#.只能代指任意一个字符,除了换行符\n
print(ret)

'''
^ 从开始匹配
'''
ret = re.findall('^h...o','hjasoflhello')
print(ret)

'''
$ 从结尾匹配
'''
ret = re.findall('test_before..x$','alsjffalexkkkalfx')
print(ret)

'''
* 重复匹配 0次到无穷多次
+ 重复匹配 1次到无穷次
? 匹配0次到1次
{ } 
'''
ret = re.findall('ba*','hasfeofhsdkfbaaaaaaa')
print(ret)#['baaaaaaa']

ret = re.findall('test_before*','hasfeofhsdkfbaaaaaa')
print(ret)

ret = re.findall('test_before+b','aaaabhabghfa')
print(ret)

ret = re.findall('test_before?b','aaabhghabfb')#a匹配0次到1次
print(ret)#['ab', 'ab', 'b']

ret = re.findall('test_before{1,3}b','vaaaaaabbbb')#a匹配1到3次
print(ret)#['aaab']

'''
[] 字符集:用来表示一组字符  --->取消元字符的特殊功能(\ ^ - 例外)
'''
ret = re.findall('test_before[cde]x','aex')#[cde]匹配'c','d','e'
print(ret)

ret = re.findall('[w,*]','awdx*')
print(ret)#['w', '*']

ret = re.findall('[1-9，test_before-z,A-Z]','sfjklsjA3G7yN73q')
print(ret)

'''
^ 放在[]里：取反
'''
ret = re.findall('[^t,b]','hongstyabgyabg')#匹配除t和b以外的所有字符
print(ret)



'''
\ --->反斜杠后面跟元字符去除特殊功能
  --->反斜杠后边跟普通字符实现特殊功能
  \d 匹配任何十进制数
  \D 匹配任何非数字字符
  \s 匹配任何空白字符
  \S 匹配任何非空白字符
  \w 匹配任何字母数字字符
  \W 匹配任何非字母数字字符
  \b 匹配一个特殊字符边界 比如空格 ，&，＃等
'''
print(re.findall('\d{11}','sjfeojfsljie1234567895214568'))#['12345678952']
print(re.findall('\sasd','fak asd'))#[' asd']
print(re.findall('\w','fak asd'))#['f', 'test_before', 'k', 'test_before', 's', 'd']

print(re.findall(r'I\b','hello,I am test_before LI$T'))
#############################################################################
#匹配出第一个满足条件的结果
ret = re.search('sb','sfskfflsb')
print(ret)#<re.Match object; span=(7, 9), match='sb'>
print(ret.group())

ret = re.search('test_before\.','test_before.dj').group()
print(ret)#test_before.

print(re.findall('\\v','adhf\v'))#['\x0b']

ret = re.findall('\\\\','abc\de')
ret = re.findall(r'\\','abc\de')
print(ret)#['\\']
'''
原始字符串(raw)的产生正是由于有正则表达式的存在。原因是ASCII字符和正则表达式特殊字符间所产生的冲突。
比如，特殊符号'\b'在ASCII字符中代表退格键，但同时'\b'也是正则表达式的特殊符号，代表匹配一个特殊边界。
为了让RE编译器把两个字符'\b'当成你想要表达的字符串，而不是一个退格键，你需要用另一个反斜杠对它进行转义，
即可以这样写：'\\b'
原始字符串就是被用于简化正则表达式的复杂程度
'''
m = re.search('\\bblow','blow')
# m = re.search(r'\bblow','blow')
print(m)


'''
() 分组
 |
'''
print(re.search('(as)+','sdjkfasas').group())#asas
print(re.search('(as)|3','3as').group())#匹配'as'或3

ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
print(ret.group())
print(ret.group('id'))
print(ret.group('name'))
#------------------------------------------------------------------------------------------------------------------------#


'''
正则表达式的方法：
1.findall():所有结果都返回到一个列表里
2.search():返回匹配到的第一个对象(object)，对象可以调用group()返回结果
3.match():只在字符串开始匹配,也返回匹配到的第一个对象(object)，对象可以调用group()返回结果
4.split()
5.sub()
6.compile()
'''

ret = re.match('asd','asdgjfkgjjeir')
print(ret)
print(ret.group())

ret = re.split('k','djkhgdfh')
print(ret)#['dj', 'hgdfh']


ret = re.split('[j,s]','djksal')#先以'j'分开，再以's'分开  ********
print(ret)#['d', 'k', 'al']

ret = re.split('[j,s]','sdjksal')
print(ret)#['', 'd', 'k', 'al']

ret = re.sub('test_before..x','s..b','hfjasalexxdhf')
print(ret)#hfjass..bxdhf

'''
re.compile（pattern，flags ）
用于将字符串形式的正则表达式编译为Pattern对象，第二个参数flag是匹配模式，取值可以使用按位或运算符'|'。
表示同时生效，比如re.I | re.M
当在单个程序中多次使用表达式时，使用和保存生成的正则表达式对象以便重用会更有效。
'''
obj = re.compile('\.com')
ret = obj.findall('fsfnsdfk.comfaffa')
print(ret)