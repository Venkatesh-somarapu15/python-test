def pattern(n):
    num=6
    for i in range(n):
        for j in range(i+1):
            ch=chr(num)
            print(ch,end=' ')
            num=num+1
            print('\n')
pattern(5)