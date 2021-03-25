n=int(input('Emter the Number'))
for i in range(1,n+1):
    if i%5==0:
        if i%2==0:
            continue
        print('Numbers which are divisibe by 5 is :',i)
        
