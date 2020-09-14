try:
    def ifnearlylucky(n):
        n=n.replace('7','')
        n=n.replace('4','')
        if n=='':
            return True
        else:
            return False

    n = input()
    c47 = str(n.count('7')+n.count('4'))
    if ifnearlylucky(c47):
        print("YES")
    else:
        print("NO")
    


except:
    pass