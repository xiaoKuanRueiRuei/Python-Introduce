#insert(插入資料)
#>>> a=[8,2,7,0,6]
#>>> a.insert(1,9)
#>>> a
#[8, 9, 2, 7, 0, 6]

#index(尋找位置)
#>>> i=a.index(0)
#>>> a.insert(i,-1)
#>>> a
#[8, 9, 2, 7, -1, 0, 6]
#尋找出0的位置，並在0的位置插入-1

#pop找出指定位置的資料並移除
#>>> a.pop(1)
#9
#>>> a
#[8, 2, 7, -1, 0, 6]
#pop是利用資料的位置以移除

# remove(移除)
#>>> a.remove(-1)
#>>> a
#[8, 2, 7, 0, 6]
#remove是利用資料本身以移除

#using lists and stacks(將資料視為盤子，取資料時自最高處取用，此為堆疊)
#push(將資料放上去)
#pop(將資料取出)
#>>> stack=[1,2,3,4,5]
#>>> 
#>>> stack.append(6)
#>>> stack.append(7)
#>>> stack
#[1, 2, 3, 4, 5, 6, 7]
#>>> 
#>>> stack.pop()
#7
#>>> stack
#[1, 2, 3, 4, 5, 6]
#>>> 
#>>> stack.pop(-1)
#6
#>>> stack
#[1, 2, 3, 4, 5]
#想取出最後一筆資料，除了可以使用最後一筆資料的位置外
#亦可忽略不寫
#也可以利用-1
#last-in first-out priciple (LIFO 後進先出)
#函數的呼叫便是堆疊的應用(副程式的呼叫，尤其連CPU都使用硬體的堆疊)

#Using Lists as Queues(排隊 / 佇列)
#first-in first-out principle (FIFO 先進先出)
#資料不夠，增開更大的空間將資料騰過去
#缺點是所有資料的排序會受到影響
#because all of the other elements have to be shifted by one
#沒有效率(移動一個，所有資料都會左移或右移)
#>>> from collections import deque
#de表示雙向關係
#>>> queue = deque([1,2,3,4,5])
#>>> 
#>>> queue.append(6)
#>>> queue.append(7)
#>>> queue
#deque([1, 2, 3, 4, 5, 6, 7])
#>>> 
#>>> queue.appendleft(6)
#>>> queue.appendleft(7)
#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5, 6, 7])

#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5, 6, 7])
#>>>  
#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5, 6, 7])
#>>> queue.pop()
#7
#>>> queue.pop()
#6
#>>> queue
#deque([7, 6, 1, 2, 3, 4, 5])
#>>> queue.popleft()
#7
#>>> queue.popleft()
#6
#>>> queue
#deque([1, 2, 3, 4, 5])

#Using Heaps(資料結構的一種，適合實作Priority Queue，二元素作法) as Priority Queues(具優先次序的佇列(根據優先權決定順序)，簡單說就是插隊)
#How to use Heaps as Priority Queues?
#>>> import heapq as pq
#>>> h = [6,5,1,2,0]
#>>> pq.heapify(h)
#>>> h
#[0, 2, 1, 6, 5]
#>>> 
#>>> pq.heappush(h,9)
#>>> pq.heappush(h,7)
#>>> h
#[0, 2, 1, 6, 5, 9, 7]
#>>> 
#>>> pq.heappop(h)
#0
#>>> pq.heappop(h)
#1
#>>> h
#[2, 5, 7, 6, 9]

#堆積排序法(Heapsort)
import heapq as pq
def heapsort(a):
    h=[]
    for x in a:
        pq.heappush(h,x)
        
    return [pq.heappop(h) for _ in range(len(h))]

#>>> import random
#>>> a=random.sample(range(100),20)
#>>> a
#[83, 79, 28, 18, 55, 92, 61, 69, 19, 71, 95, 97, 34, 37, 94, 1, 81, 88, 90, 20]
#>>> 
#>>> heapsort(a)
#[1, 18, 19, 20, 28, 34, 37, 55, 61, 69, 71, 79, 81, 83, 88, 90, 92, 94, 95, 97]

#RSA公開金鑰系統
#Fermat's little theorem states that if p is prime and 1<a<p,then
#a**(p-1)等意於1  (mod p)
#>>> n=221
#>>> a=38
#>>> pow(a,n-1,n)
#1
#221 may be a prime number
#>>> a=24
#>>> pow(a,n-1,n)
#81
#221 is not a prime number

import random

def isprime(n, k = 128):
    if n<2:
        return False
        
    for _ in range(k):
        a = random.randrange(1,n)
        if pow(a, n-1, n) != 1:
            return False
    return True
    
#>>> n=2**127-1
#>>> isprime(n)
#True
#>>> n=2**127+1
#>>> isprime(n)
#False

def nextprime(n, k =128):
    if n<2:
        return 2
    
    n+=1
    while not isprime(n,k):
        n+=1
        
    return n
    
#>>> p=nextprime(random.randrange(10**200))
#>>> p
#62756299807539435861740661436024023267371433179232367639969413409427936012915825334535413998498960592008203871528363988102475873837917758232308608226471309111359149757800103786306450678970693972566073

#Hash Function
#>>> import hashlib
#>>> password='123456'
#>>> 
#>>> h=hashlib.md5()
#>>> h.update(password.encode())
#>>> h.hexdigest()
#'e10adc3949ba59abbe56e057f20f883e'
#>>> h.digest_size, 8*h.digest_size
#(16, 128)
#>>> 
#>>> h=hashlib.sha256()
#>>> h.update(password.encode())
#>>> h.hexdigest()
#'8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'
#>>> h.digest_size, 8*h.digest_size
#(32, 256)

#Salt(cryptography)
#密碼是儲存hash code而不是字串
#>>> dk = hashlib.pbkdf2_hmac('sha256',b'password',b'salt',10000)
#>>> dk.hex()
#'0394a2ede332c9a13eb82e9b24631604c31df978b4e2f0fbd2c549944f9d79a5'
#sha256是只有265位元
#b'password'是密碼
#反覆做100,000次

