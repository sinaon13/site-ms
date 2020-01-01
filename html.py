import glob, os
os.chdir(os.getcwd())
img=[]
txt=[]
for file in glob.glob("*.txt"):
    r=open(file,'r').readlines()
    if r[0][-4:][:-1] == 'txt' :
        txt.append(r[1:-2]+r[-1].split())
    else :
        img.append([r[0][:-5]]+r[-1].split())

a=input('site name:')
ht=open(a+'.html','w')
ht.write('<!DOCTYPE html>\n<html>\n<head>\n<title>'+a+'</title>\n')
for i in txt:
    print(i)
ht.close()

