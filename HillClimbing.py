# Online Python - IDE, Editor, Compiler, Interpreter
import random
from collections import Counter

def initiate(N):
    queens = random.sample(range(N),N)
    return queens

def swap(queens,N,x1,x2):
    temp = queens[x1]
    queens[x1] = queens[x2]
    queens[x2] = temp

def heuristic(queens,N):
        result=0
        [mainDiaCount,secDiaCount] = [Counter() for i in range(2)]
        for i in range(N):
            mainDiaCount[queens[i]-i] += 1
            secDiaCount[queens[i]+i] +=1
        for count in [mainDiaCount,secDiaCount]:
            for i in count:
                result += count[i]*(count[i]-1)//2
        return result
def hC(N):
    q=initiate(N)
    h=heuristic(q,N)
    found = True
    while(1):
        if h == 0:
            return q,True
        if found == False:
            return q,False
        found = False
        for i in random.sample(range(N), N):
            if found == True:
                break
            for j in random.sample(range(N), N):
                if i == j:
                    pass
                newQ = list(q)
                swap(newQ,N,i,j)
                newH = heuristic(newQ,N)
                if newH<h:
                    found = True
                    q=newQ
                    h=newH
                    break
def randRestart(N,max_times=1000):
    for i in range(max_times):
        hillClimb = hC(N)
        if hillClimb[1] == True:
            return hillClimb[0],i+1
    assert "Can't find the final result with " + str(max_times) + " steps"
def CalcHitRate(N,max_times=1000):
    hit = 0
    for i in range(max_times):
        hillClimb = hC(N)
        if hillClimb[1] == True:
            hit +=1
    print(res[0])
    print("Hit rate with n = : " + str(N) + " is: " + str(hit/max_times))    
print(randRestart(7))
