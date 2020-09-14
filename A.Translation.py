try:
    s=input()
    t=input()
    s=list(s)
    s.reverse()
    s=''.join(s)

    if s==t:
        print("YES")
    else:
        print("NO")
except :
    pass