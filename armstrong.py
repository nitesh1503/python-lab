n=input('Enter the Number')
ln=len(n)
s=0
for i in n:
    s+=int(i)**ln
if int(n)==s:
    print('Armstrong Number')
else:
    print('Its not a Armstrong Number')
    
