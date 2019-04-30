#sample input:

#Jeremy Lin
#95 87 91
#Kobe Bryant
#86 96 73
#Michael Jordan
#89 91 80
#Larry Bird
#43 92 77
#Dirk Nowitzki
#76 75 96

#上面是文字檔

#檔案輸入
fn = 'sample.txt'
with open (fn,'r') as f:
    line = f.readlines()

data=[]
for i in range (0,len(line),2):
    name = line[i].strip()
    s = line[i+1].split()
    score = [int(x) for x in s]
    data.append((name,score))
#fn=File Name
#'r'指read
#只輸入不寫入
#as f 的 f是指檔案
#as 是取名的意思
#readlines指每一行都讀進來
#strip刪除多餘的字
#把字拆開
#沒有特別註明就當空白處理
#Note!頭尾拿掉-->srtip
#頭尾中間都要-->split
#刪除頭尾空白
#split用空白當空格
#將成績拆開來
#編號0是姓名
#編號1,3,5,7是成績
#i間隔是2
#是因為個人資料有兩筆
#如果個人資料有三筆
#間隔就是三
#以此類推
#int的處理是要將字串轉數字
#append的意思是附加檔案之意
#指說當成是處理完後
#附加上name和score的資料
#>>> data
#[('Jeremy Lin', [95, 87, 91]), ('Kobe Bryant', [86, 96, 73]), ('Michael Jordan', [89, 91, 80]), ('Larry Bird', [43, 92, 77]), ('Dirk Nowitzki', [76, 75, 96])]
#>>> score
#[76, 75, 96]
#>>> name
#'Dirk Nowitzki'
#score和name因為一次只處理一個人
#所以只有一個資料
#>>> line
#['Jeremy Lin\n', '95 87 91\n', 'Kobe Bryant\n', '86 96 73\n', 'Michael Jordan\n', '89 91 80\n', 'Larry Bird\n', '43 92 77\n', 'Dirk Nowitzki\n', '76 75 96']
#"\n"是一個看步道的符號，是換行字元





#檔案輸出(迴圈)
fn = 'output.txt'
with open (fn,'w')as f:
    for x in data:
        name,score = x
        total = sum(score)
        average = total / len(s)
        f.write('name = {} \n'.format(name))
        f.write('total = {} \n'.format(total))
        f.write('average = {:.2f} \n'.format(average))        
#w指write
#沒有寫輸出至哪裡
#就是輸出在河程式檔相同的儲存空間中
#:.2f是指取到小數點第二位
#.是指功能之意
#這邊的f是指float浮點數
#:.是舉到第幾位的意思
#{}這是輸出編排指令
#%功能比{}少
#%是舊的寫法
#{}是新的寫法
#大括號是文字編排
#format是指格式化的意思
#意思是將前面的隔是套在format括號中的東西





#新寫法
fn = 'sample.txt'
with open (fn,'r') as f:
    line = f.readlines()
    
name = [x.strip() for x in line[::2]]
score = [[int(x) for x in y.split()] for y in line[1::2]]
data = [(x,y) for x , y in zip(name , score)]
#[::2]把name從零開始間隔二的間隔strip掉
#[1::2]把data從零開始間隔二的間隔strip掉
#zip拉拉鏈的概念
#把東西配合起來
#>>> data
#[('Jeremy Lin', [95, 87, 91]), ('Kobe Bryant', [86, 96, 73]), ('Michael Jordan', [89, 91, 80]), ('Larry Bird', [43, 92, 77]), ('Dirk Nowitzki', [76, 75, 96])]
#>>> score
#[[95, 87, 91], [86, 96, 73], [89, 91, 80], [43, 92, 77], [76, 75, 96]]
#>>> name
#['Jeremy Lin', 'Kobe Bryant', 'Michael Jordan', 'Larry Bird', 'Dirk Nowitzki']
#>>> line
#['Jeremy Lin\n', '95 87 91\n', 'Kobe Bryant\n', '86 96 73\n', 'Michael Jordan\n', '89 91 80\n', 'Larry Bird\n', '43 92 77\n', 'Dirk Nowitzki\n', '76 75 96']
 