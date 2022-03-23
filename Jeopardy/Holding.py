#This is holding for code not yet used or unused
def file_len(g):
    with open(g) as f:
        for i, l in enumerate(f):
            pass
    return i + 1
file_len()
with open('test','r') as f_open:
    data = [f_open.read()]
f= open("test","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
print(data[0])
f.close()
jeop=open('test','r')
list1 = jeop.readlines()
with open("test", "r") as f:
    list2 = []
    for item in f:
        number = 0
        list2.append(item + str(number))
        number += 1
    print(list2)
file=open("guru99.txt", "r")
    '''for line in f:
        print(line)'''
    with open('guru99.txt') as f:
        data=f.readlines()
    print(data[5])
    print(file.readline(7)):
    if f.mode == 'r': 
         contents =f.read()
         print(contents)
    fl=f.readlines()
    print(fl[3])
    for x in fl:
        print(x)
    with open('/home/pi/Jeopardy/text/test','r') as f_open:
        data = f_open.read()
    print(data[3])
    qq=open('/home/pi/Jeopardy/text/test','r')
