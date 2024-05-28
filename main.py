import numpy as np
# There is N people
# Person with odd number can be selected

# store the probability of selecting No. n from N people at time t
pdict = {}

# Get the probability of selecting No. n from N people at time t
def getp(N: int,n: int,t: int) -> float:
    # check if the value is already calculated
    if (N,n,t) in pdict:
        return pdict[(N,n,t)]
    # if not, calculate the value
    isodd = n%2==1
    odds = (N+1)//2
    smallerodds = n//2
    biggerodds = odds - isodd - smallerodds
    if (t==1):
        return isodd/odds
    if (N==1):
        return 1
    # store the value
    pdict[(N,n,t)] = (isodd/odds + # die in this round
            isodd/odds*smallerodds*getp(N-1,n-1,t-1) + # is odd, become smaller
            (1-isodd)/odds*smallerodds*getp(N-1,n-1,t-1) + # is even, become smaller
            isodd/odds*biggerodds*getp(N-1,n,t-1) + # is odd, unchanged
            (1-isodd)/odds*biggerodds*getp(N-1,n,t-1)) # is even, unchanged
    
    return pdict[(N,n,t)]


N = 600
Matgetp = np.array([[getp(N,n,t) for n in range(1,N+1)] for t in range(1,N+1)])

# get the index of minimum number for each row from matrix
np.argmin(Matgetp, axis=1) + 1
