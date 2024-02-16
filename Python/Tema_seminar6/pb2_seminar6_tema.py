def aparitii(x):
    i = cb_st(0, n-1, x)
    if i == -1:
        return i
    j = cb_dr(i, n-1, x);     
    return j-i+1

def cb_st(st, dr, x):
    if dr >= st:
        mij = (st + dr)//2     
         
        if (mij == 0 or x > v[mij-1]) and v[mij] == x:
            return mij
        elif x > v[mij]:
            return cb_st((mij + 1), dr, x)
        else:
            return cb_st(st, (mij - 1), x)
    return -1
  
def cb_dr(st, dr, x):
    if dr >= st:
        mij = (st + dr)//2; 
        if(mij == n-1 or x < v[mij+1]) and v[mij] == x :
            return mij
        elif x < v[mij]:
            return cb_dr(st, (mij - 1), x)
        else:
            return cb_dr((mij + 1), dr, x)     
    return -1
 
v = [0, 1, 1, 2, 5, 5, 5, 5, 20, 23]
x = 5
n = len(v)
print (aparitii(x))