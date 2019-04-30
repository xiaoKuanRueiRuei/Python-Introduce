#GLOBAL
def f():
    print(s)
    
#s is global
s = ' I love Paris!'
f()
# I love Paris!





#整體變數、局部變數
#s第一次出現在函數外
#在外面出現的資料叫"整體變數(Global)"





#LOCAL
def f():
    #s is local
    s = ' I love London!'
    print(s)
    
#s is global
s = ' I love Paris!'
f()
print(s)
# I love London!
# I love Paris!





#錯誤範例
def f():
    print(s)
    #s is local and global (ERROR!)
    s='I love London!'
    print(s)
    
#s is global
s='I love Paris!'
f()
print(s)
#UnboundLocalError: local variable 's' referenced before assignment
#Python是全部編譯後才執行
#對第一個print(s)而言
#s為global
#對第二個print(s)而言
#s為local
#因此發現順序有問題
#ERROR!
#常犯錯誤請記得!





#新指令gloabl
def f():
    global s
    print(s)
    s = 'I love London!'
    print(s)
    
#s is global
s='I love Paris!'
f()
print(s)
#I love Paris!
#I love London!
#I love London!
#最後一個print(s)
#因為跑過 s='I love London!'
#所以s='I love Paris!'被 s='I love London!'取代了
#為了避免這種狀況
#盡量避免global的用法





#錯誤範例
def f():
    s='I love London!'
    print(s)
    
f()
print(s)
#UnboundLocalError: local variable 's' referenced before assignment
#就是黑箱作業啦(封裝處理)!!!
#在程式中越黑越好
#這樣才不會相互干擾





#LOCAL Versus NONLOCAL
#LOCAL
def f():
    def g():
        s='I love Berlin!'
        print(s)
        
    def h():
        s='I love Rome!'
        print(s)
        
    s = 'I love London!'
    g()
    h()
    print(s)
    
s = 'I love Paris!'
f()
print(s)
#I love Berlin!
#I love Rome!
#I love London!
#I love Paris!

#g()、h()是f()的local function
#g()、h()的 s都是local
#所以不會被取代



#NONLOCAL
def f():
    def g():
        nonlocal s
        s='I love Berlin!'
        print(s)
        
    def h():
        nonlocal s
        s='I love Rome!'
        print(s)
        
    s = 'I love London!'
    g()
    h()
    print(s)
    
s = 'I love Paris!'
f()
print(s)
#I love Berlin!
#I love Rome!
#I love Rome!
#I love Paris!

#nonlocal將local變成f()中公有的
#因為nonlocal s
#所以g()開始往外面找
#這時找到f()
#找到s了!
#可是是s='I love Berlin!'-->第一個print
#而不是s = 'I love London!'
#因為s = 'I love London!'被s='I love Berlin!'取代了
#相同的道理執行h()
#此時原本取代London的Berlin又被Rome取代了
#這是第二個print
#在執行第三個print時
#因為Rome是最後一個s了
#因此再次輸出Rome
#最後一個print則是輸出Paris