try:
    from itertools import combinations as c
    from itertools import permutations as p
    import numpy as np
    for _ in range(int(input())):
        n = int(input())
        arr=[int(x) for x in input().split()]
        a=[]
        ans= list(p(arr,5))
        for i in ans:
            #i=list(i)
            a.append(np.prod(i))
        print(max(a))
except :
    pass