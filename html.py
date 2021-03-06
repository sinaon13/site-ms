import glob, os
import fnmatch
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("--file", "-f", type=str, required=True)
try:
    args = parser.parse_args()
    os.chdir(args.file)
    os.system('cls');
except:
    os.chdir(input())
img=[]
txt=[]
btn = []
inp = []
video=[]
tab=[]
data = []
videoname = []
#function for find png file and open it or open txt
for file in glob.glob("*.txt"):
    if ".png" in file:
        continue
    r=open(file,'r').readlines()
    if r[0][-4:][:-1] == 'txt' :
        txt.append(r[1:-1]+r[-1].split())
#get all of files and save in list
def get_files():
    listOfFiles = os.listdir('.')
    l = []
    pattern = "*.png.txt"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
                l.append(entry)
    return l
im = get_files()
btn_name = []
#open txt file and read it and find btn and run that work
for file in glob.glob("*.txt"):
    r=open(file,'r').readlines()
    if r[0][-4:][:-1] == 'btn' :
        btn.append(r[1:-1]+r[-1].split())
        btn_name.append(r[0][:-1])
#open txt file and find inp in that and run that work
for file in glob.glob("*.txt"):
    if ".png" in file:
        continue
    r=open(file,'r').readlines()
    if r[0][-4:][:-1] == 'inp' :
        inp.append(r[1:-1]+r[-1].split())

#open txt file and find vid in that and run that work
for file in glob.glob("*.txt"):
    if ".png" in file:
        continue
    r=open(file,'r').readlines()
    if r[0][-5:][:-1] == '.vid' :
        video.append(r[1:-1] + r[-1].split())
        videoname.append(r[0][:-5])

#open txt file and find data in that and run that work
for file in glob.glob("*.txt"):
    if ".png" in file:
        continue
    r=open(file,'r').readlines()
    if r[0][-5:][:-1] == '.tab' :
        tab.append(r[1:-1] + r[-1].split())
        data.append(r[0][:-1] + '.data')
link=[]
#open txt file and find link in that and run that work
for file in glob.glob("*.txt"):
    if ".png" in file:
        continue
    r=open(file,'r').readlines()
    if r[0][-6:][:-1] == '.link' :
        link.append(r[1:-1] + r[-1].split())
img = []
#get all of the images
for i in im:
    q = []
    for j in open(i, 'r').readlines():
        for d in j.split():
            q.append(d)
    img.append(q)
oo=''
o=[]
print(btn)
print(img)
print(txt)
print(video)
print(tab)
print(inp)
scription = []
for i in btn:
    if i[-5][-4:-1] == '.js':
        if(i[-5][:-1] not in scription):
            scription.append(i[-5][:-1])
btn2 = []
inp2 = []
vid2=[]
tab2=[]
link2=[]
print(scription)
##for i in range(len(txt)):
##    for g in range(len(txt[i])):
##        if g<len(txt[i])-2:
##            oo+=txt[i][g]
##    o=[txt[i][-2]]+[txt[i][-1]]
##    txt[i]=[oo]+o
##    o=[]
##    oo=''
##print(txt)
a=os.getcwd()
ht=open(a +'\\' + a.split('\\')[-1][:-5]+'.html','w')
ht.write('''<!DOCTYPE html><html><head>
''')
for i in scription:
    ht.write('''<script type="text/javascript" src="'''+ i + '''"></script>''')
ht.write('''
<title>'''+a.split('\\')[-1][:-5]+'''</title>
<style>
''')
txt2=[]
img2=[]
fl=1
#convert txt with their angle(in html)
for i in txt:
    txt2.append('p'+str(fl))

    ht.write('.p'+str(fl)+'''{
    font-size: '''+str(i[-5][:-1])+'px;'+'\n'
    'color:'+i[-4]+''';
    font-family:'''+i[-6][:-1]+';''''
    position: absolute;
    left : ''' + i[-2] + '''px;
    top : ''' + i[-1] + '''px;
}

''')
    fl+=1
#set position text(in html)
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
fl = 0
#set in btn angle of text
for i in btn:
    btn2.append('b' + str(fl))
    w = i[-3].split()[0]
    h = i[-3].split()[-1]
    ht.write('.b' + str(fl) + '''{
    position: absolute;
    left : ''' + str(int(i[-2]))  + '''px;
    top : ''' + str(int(i[-1])) + '''px;
    background-color : ''' + i[-8] + ''';
    ''' + i[-5][:-1] + '''px;
    width: '''+ w +'''px;
    height: '''+ h +'''px;
    border: 2px solid black;
}''')
    fl += 1
fl = 0


##for i in range(0,len(tab),2):
##    if i<len(tab):
##        tab2.append('tab'+str(fl))
##        ht.write('.tab' + str(fl) + '''{
##        position: absolute;
##        width:''' + tab[i][-2] + '''px;
##        height: ''' + tab[i][-1] + ''' px;\n''')
##        fl+=1
fl=0
#set in inp angle of text
for i in inp:
    inp2.append('in' + str(fl))
    ht.write('.in' + str(fl) + '''{
    position: absolute;
    '''+ i[-5][:-1]+'''px;
    left : ''' + i[-2] + '''px;
    top : ''' + i[-1] + '''px;
    width:''' + i[-3].split()[0]+ '''px;
    height: '''+ i[-3].split()[-1] + '''px;

    border: 2px solid '''+ i[-7][:-1]+''';
}''')
    fl+=1
fl=0
##set in tab angle of text
for i in tab:
    ht.write('''\ntable {
      font-family: arial, sans-serif;
      border-collapse: collapse;
      position:absolute;
      top:''' + i[-1] + '''px;
      left:''' + i[-2] + '''px;
      border-color:black;
    }
    td, th {
      border: 1px solid;
      text-align: left;
      padding: 8px;
    }
    ''')
    fl+= 1
fl=0
##set in link angle of text
for i in link:
    link2.append('''link'''+str(fl))
    ht.write('''\n.link'''+str(fl)+'''{
    position:absolute;
    top:'''+ i[-1]+'''px;
    left:'''+i[-2]+'''px;
    font-family:'''+i[2]+''';
    font-size:'''+i[3]+'''px;
    color:'''+i[4]+''';}''')
    fl+=1
fl = 0
#set in video angle of text
for i in video:
    vid2.append('vid' + str(fl))
    ht.write('.vid'+str(fl) + '''{
    position: absolute;
    left:'''+i[2]+'''px;
    top:'''+ i[3]+'''px;
    width:''' + i[1].split()[0] +'''px;
    height:''' + i[1].split()[0] +'''px;
}''')
ht.write('''</style>
</head>
<body>
''')
#push texts in html page
for i in range(len(txt2)):
    clas='class="'+txt2[i]+'"'
    ht.write('<p '+clas+'>')
    for j in txt[i][:-6]:
        ht.write(j)
        ht.write('<br>')
    ht.write('</p>')
#push images in html page
for i in range(len(img2)):
    clas='class="'+img2[i]+'"'
    ht.write('<img '+clas+' src = "' + img[i][0] +'">')
#push buttons in html page
for i in range(len(btn2)):
    clas='class="'+btn2[i]+'"'
    ht.write('<button '+clas+' onclick = "' + btn[i][-7].split(':')[-1][:-1] + '">' +btn_name[i][:-3]+ '</button>')
#push inputs in html page
for i in range(len(inp2)):
    clas='class="'+inp2[i]+'"'
    ht.write('<input '+clas+' type = "' + inp[i][-5][:-1] + '">')
#push videos in html page
for i in range(len(vid2)):
    clas='class="'+vid2[i]+'"'
    ht.write('''<video '''+clas+''' controls>
    <source src="'''+videoname[i]+'''" type="video/''' + videoname[i].split('.')[-1] +'''">
    </video>
    ''')
#push links in html page
for i in range(len(link2)):
    clas='class="'+link2[i]+'"'
    ht.write('\n<a href="'+link[i][0]+'" ' +clas+'>'+link[i][1]+'</a>')
sf=-1
#push tables in html page
for i in range(len(tab)):
    if not len(tab[i]):break
    ht.write('''<table >\n''')
    ht.write('<tr>\n')
    x = 0
    f = False
    for j in range(len(tab[i])):
        if '-th' in tab[i][j]:
            break
        if f:
            ht.write('<th>' + tab[i][j][:-1] + '</th>\n')
            x+=1
        if 'th-' in tab[i][j]:
            f = True
    ht.write('</tr>\n')
    with open(data[i], 'r') as f:
        l = f.readlines()
        for j in range(int(tab[i][-4])):
            ht.write('<tr>\n')
            d = l[j].split('\n')[0]
            for p in range(x):
                q = ''
                for a in d.split()[p].split(';;')[:-1]:
                    q+=a + ' '
                q += d.split()[p].split(';;')[-1]
                ht.write('<td>'+ q +'</td>\n')
            ht.write('</tr>\n')
        f.close()

    ht.write('</table>\n')
ht.write('''</body>
</html>''')
ht.close()
