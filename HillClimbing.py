# Online Python - IDE, Editor, Compiler, Interpreter
import random
from collections import Counter

def initiate(N):#Khởi tạo
    queens = random.sample(range(N),N)
    return queens

def swap(queens,N,x1,x2):#Hàm Swap, Thường gặp rất nhiều ở các bài toán liên quan tới mảng.
    temp = queens[x1]
    queens[x1] = queens[x2]
    queens[x2] = temp

def heuristic(queens,N):#Tính Heuristic bằng cách đếm số queens ở đường chéo.
        result=0
        [mainDiaCount,secDiaCount] = [Counter() for i in range(2)]
        for i in range(N):
            mainDiaCount[queens[i]-i] += 1 #Các queens ở cùng đường chéo chính sẽ có toạ độ dòng - toạ độ cột bằng nhau.
            secDiaCount[queens[i]+i] +=1 #Các queens ở cùng đường chéo phụ sẽ có toạ độ dòng + toạ độ cột bằng nhau.
        for count in [mainDiaCount,secDiaCount]:
            for i in count:
                result += count[i]*(count[i]-1)//2 #Gom lại các cặp queens cùng đường chéo, tính theo nguyên tắc bắt tay.
        return result
def hC(N):
    #Khởi tạo và đếm Heuristic ở queens khởi tạo.
    q=initiate(N)
    h=heuristic(q,N)
    found = True #Đưa found = True để tránh việc found = False làm phá vỡ vòng lặp.
    while(1):
        if h == 0:#Lúc này là đã tìm được đáp án, return True.
            return q,True
        if found == False:#Lúc này đã xác định rơi vào tối ưu cục bộ, return False. Cho dù True hay False đều return ra Queens tìm được.
            return q,False
        found = False
        for i in random.sample(range(N), N):#Swap random 2 chỗ với nhau.
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
                    break #Lưu ý break này chỉ break vòng lặp 2, để break toàn bộ ta cần biến boolean là found.
def randRestart(N,max_times=1000): #Hàm random restart, chỉ là chạy nhiều lần N-Queens đến khi tìm được lời giải thôi.
    for i in range(max_times):
        hillClimb = hC(N)
        if hillClimb[1] == True:
            return hillClimb[0],i+1
    assert "Can't find the final result with " + str(max_times) + " steps"
#Hàm để tính Hit rate, vì hàm hill climbing mang tính chất ngẫu nhiên nên Hit rate thường sẽ chênh nhau
#Max_times càng ít hit rate chênh càng nhiều.
def CalcHitRate(N,max_times=1000):
    hit = 0
    for i in range(max_times):
        hillClimb = hC(N)
        if hillClimb[1] == True:
            hit +=1
    print(res[0])
    print("Hit rate with n = : " + str(N) + " is: " + str(hit/max_times))    
