f=open('poem.txt')
content=f.read()
if 'good' in content:
    print('Poem content contain word good')
else:
    print('Poem content does not contain word good')
f.close()