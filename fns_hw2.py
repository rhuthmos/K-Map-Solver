#Rhythm Gupta
#2018082
#Sec A Gp 2
def uniq(L):
    T = []
    for i in L:
        if T.count(i) == 0:
            T.append(i)
    return(T)


def decoder(L):
    a = L.count('&')
    T = []
    if a==1:
        for i in range(2):
            b = L.index('&')
            M = L[:b] + str(i) + L[b+1:]
            T.append(M)
    elif a==2:
            b = L.index('&')
            c = L.index('&', b+1)
            for y in range(2):
                for z in range(2):
                    M = L[:b] + str(y) + L[b+1:c] + str(z) + L[c+1:]
                    T.append(M)
    elif a==3:
            b = L.index('&')
            c = L.index('&', b+1)
            d = L.index('&', c+1)
            for y in range(2):
                for z in range(2):
                    for x in range(2):
                        M = L[:b] + str(y) + L[b+1:c] + str(z) + L[c+1:d] + str(x) + L[d+1:]
                        T.append(M)
    elif a==0:
            T = L
    else:
        for w in range(2):
            for x in range(2):
                for y in range(2):
                    for z in range(2):
                        M = str(w) + str(x) + str(y) + str(z)
                        T.append(M)
    return(T)


def pi_mul(s1, s2):  # a function to multiply two prime implicants (reduntant)
    s = ''
    for i in range(4):
        if (s1[i] == '0' and s2[i] == '1') or (s1[i] == '1' and s2[i] == '0'):
            s = s + '#'
        elif s1[i] == '&':
            s = s + s2[i]
        elif s2[i] == '&':
            s = s + s1[i]
        elif s1[i] == s2[i]:
            s = s + s1[i]
    return(s)

def  pi_hr(s):   # convert prime implicants to human readable form i.e,in terms of A, B, C, D and their complements.
    v = ''
    L = ['w','x','y','z']
    for i in range(4):
        if s[i] == '1':
            v = v + L[i]
        elif s[i] == '0':
            v = v + L[i] + "'"
    return(v)

def sum_list_opt(L1): # optimize sum list
    for i in L1:      # ensure that each term contains a particular pi atmost once i.e, x*x = x
        L = []
        for j in range(len(i)):
            L.append(i[j])
        M = uniq(L)
        s = ''
        for j in M:
            s = s + j
        L1[L1.index(i)] = s
    
    for k in L1:     # apply x + xy = x
        for d in L1:
            if k!=d and len(k)<=len(d):
                flag = 0
                for f in k:
                    if d.find(f) > -1:
                        flag += 1
                if flag == len(k):
                    L1[L1.index(d)] = '@'
    L2 = []
    for t in L1:
        if t != '@':
            L2.append(t)
    return(L2)



def converter_4bit(s):
    return(('0' * (4-len(s))) + s)


def mult(L1, L2):  # multiplies two lists so as to convert pos to sop
    ans = []
    for i in L1:
        for j in L2:
            if i == j:
                ans.append(i)
            else:
                ans.append(i + j)
    ans1 = uniq(ans) # ensures x + x = x
    ans2 = sum_list_opt(ans1)
    return(ans2)


def sop(P):
    if len(P) == 0:
        return(P)
    elif len(P)==1:
        return(list(P[0].keys()))
        
    if len(P) == 2:
        return(mult(list(P[0].keys()), list(P[1].keys())))
    else :
        return(mult(list(P[0].keys()), sop(P[1:])))
















