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

'''def countConflicts(queens,N):
    rows = {}
    rdiags = {}
    ldiags = {}
    for col, row in enumerate(queens):
        rows[row] = rows.get(row, -1) + 1
        rdiags[row - col] = rdiags.get(row - col, -1) + 1
        ldiags[row - (N - col)] = ldiags.get(row - (N - col), -1) + 1
    conflicts = []
    for col, row in enumerate(queens):
        conflicts.append(rows.get(row, 0) + rdiags.get(row - col, 0) + ldiags.get(row - (N - col), 0))
    return sum(conflicts)//2'''
def heuristic(queens,N):
        result=0
        [lineCount,mainDiaCount,secDiaCount] = [Counter() for i in range(3)]
        for i in range(N):
            lineCount[queens[i]] += 1
            mainDiaCount[queens[i]-i] += 1
            secDiaCount[queens[i]+i] +=1
        for count in [lineCount,mainDiaCount,secDiaCount]:
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
    hit = 0
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
