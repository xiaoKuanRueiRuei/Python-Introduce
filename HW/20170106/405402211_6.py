#10.3
a=[str(x) for x in input('Enter integers between 1 and 100:').split()]
a.sort()
while a  != []:
    b=a.count(a[0])
    if b>1:
        print(a[0],'occurs',b,'times')
    else:
        print(a[0],'occurs',b,'time')
    for _ in range (b):
        a.remove(a[0]) 
#10.4
a=[int(x) for x in input("請輸入成績:").split()]

average = sum(a) / len(a)
print("平均:",average,"分")

b=0
c=0

for x in range (0,len(a)):
    if a[x] >= average:
        b+=1
    else:
        c+=1
        
print("有",b,"人高於平均")
print("有",c,"人低於平均")
#10.9
a=[ float(x) for x in input("Enter numbers:").split()]

def mean(x):
    b = sum(x) / len(x)
    print("The mean is ", b)
    
def deviation(x):
    c=[]
    d=sum(a)/len(a)
    for x in range (0,len(a)):
        e=(a[x]-d)**2
        c.append(e)
    f=sum(c)/(len(c)-1)
    print('deviation=',f**0.5)
 
mean(a)
deviation(a)    
#10.10
def reverse(lst):
    result = []

    for element in lst:
        result.insert(0, element)
        
    return result
#10.16
def bubble(x):
    l = len(x)        
    for a in range(l):
        for b in range(l-1):
            if (x[a] < x[b]):
                x[a], x[b] = x[b], x[a]
    return x 
#10.20
def find_legal_position(arr, n_row, n_queens, trace_back=False):
    start = 0
    if trace_back:
        start = arr[n_row] + 1
    for col in range(start, n_queens):
        ok = True
        for row in range(n_row):
            if arr[row] == col:
                ok = False
                break
            if n_row - row == abs(col - arr[row]):
                ok = False
                break
        if ok:
            return col
    return None
    
def solve_queen_puzzle(n_queens):
    result = [0] * n_queens
    n_row = 0
    while n_row < n_queens:
        pos = find_legal_position(result, n_row, n_queens)
        if pos is not None:
            result[n_row] = pos
            if n_row == n_queens - 1:
                yield result[:]
        if pos is None or n_row == n_queens - 1:
            while 1:
                n_row -= 1
                if n_row < 0:
                    return
                pos = find_legal_position(result, n_row, n_queens, back_tracing=True)
                if pos:
                    result[n_row] = pos
                    break
        n_row += 1