"""
d1 = {'name': '隔壁老王', '身高': 171, 'sex': 44, 'birthday': '1976.10.10'}
if d1['身高'] > 180:
    if d1['sex'] > 50:
        print(d1['name'], '是一位成功的企业家')
    else:
        print(d1['name'], '是一位小屁孩')
elif d1['身高'] > 170:
    if d1['sex'] > 40:
        print(d1['name'], '是一位成功的企业家')
    else:
        print(d1['name'], '是一位小屁孩')
else:
    print(d1['name'], '是我')

d = {'时间': '2020-09-26', '地点': '上海', '人物': '我', '目标': '学习python'}
if d['地点'] == '北京':
    if d['时间'] == '2020-09-11':
        print(d['人物'], '在', d['地点'], d['目标'])
    elif d['时间'] == '2020-09-22':
        print(d['人物'], '在', '北京', d['目标'])
    elif d['时间'] == '2020-08-02':
        print('小明', '在', '杭州', d['目标'])
    else:
        print('我并没有学习python')
elif d['地点'] == '杭州':
    if d['时间'] == '2020-09-27':
        print('在', d['地点'], d['目标'])
    elif d['时间'] == '2020-04-21':
        print('在', '北京', d['目标'])
    else:
        print('我正在学习python')
else:
    print('python太难了')





ab=i=0
while i<=100:
    ab=ab+i
    i=i+1
print(ab)



key=1
while key>=0:
    key= input('请输入正整数：')
    key= int(key)
    if key>=100:
        print(key,'不小于100')
    else:
        print(key,'小于100')



ab=0
while ab<=10:
    ab = ab + 1
    if ab==8:
        continue
    print(ab)

print('____________________________________')


l=['name','sex','id']
for woodman in l:
    if woodman == 'sex':
        continue
    print(woodman)
else:
    print('循环结束')



l=['name','sex','id']
for woodman in l:
    print(woodman)
    if woodman == 'sex':
        continue
else:
    print('循环结束')

print('________________________________________')

dict={'name':'laowang','sex':'nan','id':1187}
for key,value in dict.items():
    print(key,value)
else:
    print('循环完成后结束循环')


#for <变量> in <循环序列>

#for <外循环变量> in <外循环序列>
    #for<内循环变量> in <内循环序列>
        #《内循环体》
    #《外循环体》

for l in range(-1,-5,-2):
    print(l)

print('______________________________')


lll=['name','sex','id']
for i in range(len(lll)):
    print(i,lll[i])



print('________________________')


for test011 in range(1,10):
    for j in range(test011,10):
        print('%d*%d=%d' % (test011,j,test011*j),end='\t')
    print('')


for test011 in range(-9,0):
    test011=test011*-1
    for j in range(test011,10):
        print('%d*%d=%d' % (test011,j,test011*j),end='\t')
    print('')



test00011=[12,45,21,6,58,7,46,1,-71,-3,-7,-11]

#返回列表元素个数，长度为12，长度固定
length=len(test00011)

#赋值isss迭代为元素个数，值12，长度对应的迭代器随着for下改变而改变
for isss in range(length):

    for jsss in range(length-isss):
        n=length-jsss
        if test00011[n-1]<test00011[n-2]:
            test00011[n-1],test00011[n-2]=test00011[n-2],test00011[n-1]
print(test00011)




test111111=[1,4,7,2,21,5125,1241412,1241241241,12312312313,-1111,-111111,-21321321]
ij=len(test111111)
for jjjj in range(ij):
    for issss in range(ij-jjjj):
        n=ij-issss
    if test111111[n-1]<test111111[n-2]:
        test111111[n-1],test111111[n-2]=test111111[n-2],test111111[n-1]
print(test111111)



abc=[123,5125,1231,14121412,12312,12,214,242,52,-112,-21312,-233,-4214]
abcd=len(abc)
for abcde in range(abcd):
    for abcdef in range(abcd-abcde):
        aa=abcd-abcdef
        if abc[aa-1]<abc[aa-2]:
            abc[aa - 1],abc[aa-2]=abc[aa-2],abc[aa-1]
print(abc)

"""


# a=input('请输入:')
# b=input('请输入:')
# print('结果:',int(a)+int(b))
#
#
# print(type(a))
# print(type(233333))
# print(type(2.33))
# print(type(()))
# print(type({}))
# print(type(True))
# print(type([]))


# a=['a',2323,'dasd','老王']
# print(len(a))




a='隔壁老王就是你'
b='隔壁老王在身边'
c='3'
d='23'
print(a+b)
print(c+d)
print(int(c)+int(d))
print(len(a+b+c+d))
print(len(a)+len(b)+len(c)+len(d))
















