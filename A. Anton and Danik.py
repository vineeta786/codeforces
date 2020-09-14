try:
    n = int(input())
    s=input()
    if 'A' in s:
        ca=s.count('A')
    if 'D' in s:
        cd = s.count('D')
    if ca>cd:
        print("Anton")
    elif cd>ca:
        print("Danik")
    elif cd==ca:
        print("Friendship")

except:
    pass