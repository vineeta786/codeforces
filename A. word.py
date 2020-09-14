try:
    s = input()
    cap=0
    low=0

    for i in s:
        if ord(i) in range(97,123):
            low+=1
        else:
            cap+=1
    if low>=cap:
        print(s.lower())
    else:
        print(s.upper())
except :
    pass