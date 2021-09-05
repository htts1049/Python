'bat.y.abcdefghi'

new_id = "".lower()
    
for i in new_id:
    if i not in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
        new_id = new_id.replace(i,'')
        
while '..' in new_id:
    new_id=new_id.replace('..','.')

if new_id[0] == '.':
    new_id = list(new_id)
    del new_id[0]
    new_id = ''.join(new_id)

    
if new_id[-1] == '.':
    new_id = list(new_id)
    del new_id[-1]
    new_id = ''.join(new_id)
    
    

if new_id == '':
    new_id ='a'
        
if len(new_id)>=16:
    new_id= new_id.replace(new_id[15:],'')
    if new_id[-1]=='.':
        new_id= new_id.replace(new_id[-1],'')
    
while len(new_id)<= 2:
    new_id += new_id[-1]

answer = new_id

print(answer)
