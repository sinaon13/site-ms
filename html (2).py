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

a=input('site name:')
ht=open(a+'.html','w')
ht.write('''<!DOCTYPE html><html><head>
<title>'''+a+'''</title>
<style>
.topl1{
top:45px;
left:168px;
}
</style>
</head>
<body>
<p class="topl1">sina on va hasan kheng</p>
</body>
</html>
''')
ht.close()

