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
print(txt)
a=input('site name:')
ht=open(a+'.html','w')
ht.write('''<!DOCTYPE html><html><head>
<title>'''+a+'''</title>
<style>''')
for i in txt:
    
         

'''</style>
</head>
<body>

</body>
</html>
'''
ht.close()

