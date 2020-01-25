import glob, os
os.chdir(os.getcwd())
img=[]
txt=[]
for file in glob.glob("*.txt"):
    r=open(file,'r').readlines()
    if r[0][-4:][:-1] == 'txt' :
        txt.append(r[1:-1]+r[-1].split())
    else :
        img.append([r[0][:-5]]+r[-1].split())
oo=''
o=[]
for i in range(len(txt)):
    for g in range(len(txt[i])):
        if g<len(txt[i])-2:
            oo+=txt[i][g]
    o=[txt[i][-2]]+[txt[i][-1]]
    txt[i]=[oo]+o
    o=[]
    oo=''
print(txt)
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
    position: absolute;
    top: '''+str(i[-1])+'''px;
    left: '''+str(i[-2])+'''px;
    }

''')
    fl+=1
ht.write('''</style>
</head>
<body>
''')
for i in range(len(txt2)):
    ht.write('<p '+'class="'+txt2[i]+'">'+txt[i][0]+'''</p>
''')
ht.write('''</body>
</html>''')
ht.close()
print(txt,txt2)       

