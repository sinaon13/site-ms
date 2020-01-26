import os
file = input()
with open(file, 'r') as f:
    lines = f.readlines()
    with open(file + '.html', 'w') as F:
        F.write('''
<!DOCTYPE html>
<html>
<style>
.pos{
    position : absolute;
    left: ''' + lines[1].split()[0] + '''px;
    top: ''' + lines[1].split()[1] + '''px;
</style>
<body>
<img class = "pos" src = "''' + lines[0] + '''" alt = "No Image">
</body>
</html>''')
        F.close()
    f.close()
        

