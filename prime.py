n=int(input('Enter the Number'))
for i in range(2,n+1):
    if n%i==0:
        print('Number is not Prime',n)
        break
    else :
        print('Number is prime ',n)
else :
    print('Number is not Prime',n)
