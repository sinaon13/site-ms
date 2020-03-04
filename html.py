import glob, os
import fnmatch
os.chdir(os.getcwd())
img=[]
txt=[]
for file in glob.glob("*.txt"):
    if ".png" in file:
        continue
    r=open(file,'r').readlines()
    if r[0][-4:][:-1] == 'txt' :
        txt.append(r[1:-1]+r[-1].split())
    else:
        img.append([r[0][:-5]]+r[-1].split())
def get_files():
    listOfFiles = os.listdir('.')
    l = []
    pattern = "*.png.txt"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
                l.append(entry)
    return l
im = get_files()
img = []
for i in im:
    q = []
    for j in open(i, 'r').readlines():
        for d in j.split():
            q.append(d)
    img.append(q)
oo=''
o=[]
##for i in range(len(txt)):
##    for g in range(len(txt[i])):
##        if g<len(txt[i])-2:
##            oo+=txt[i][g]
##    o=[txt[i][-2]]+[txt[i][-1]]
##    txt[i]=[oo]+o
##    o=[]
##    oo=''
##print(txt)
a=input('site name:')
ht=open(a+'.html','w')
ht.write('''<!DOCTYPE html><html><head>
<title>'''+a+'''</title>
<style>
''')
txt2=[]
img2=[]
fl=1
for i in txt:
    txt2.append('p'+str(fl))

    ht.write('.p'+str(fl)+'''{
    font-size: '''+str(i[-6][:-1])+'px;'+'\n'
    'color:'+i[-5]+''';
    font-family:'''+i[-7][:-1]+';''''
    position: absolute;
    left : ''' + i[-2] + '''px;
    top : ''' + i[-1] + '''px;
}

''')
    fl+=1
fl = 0
for i in img:
    img2.append('i'+str(fl))

    ht.write('.i'+str(fl)+'''{
    position: absolute;
    left : ''' + i[-2] + '''px;
    top : ''' + i[-1] + '''px;
}

''')
    fl += 1
ht.write('''</style>
</head>
<body>
''')
for i in range(len(txt2)):
    clas='class="'+txt2[i]+'"'
    ht.write('<p '+clas+'>'+txt[i][0][:-1]+'</p>')

for i in range(len(img2)):
    clas='class="'+img2[i]+'"'
    ht.write('<img '+clas+' src = "' + img[i][0] +'">')
ht.write('''</body>
</html>''')
ht.close()
