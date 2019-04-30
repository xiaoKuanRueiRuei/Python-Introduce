asd=('Asd',10)
zxc=('Zxc',12)
qwe=('Qwe',45)
people=[asd,qwe,zxc]
sorted(people)






sorted(people,key=lambda x:x[1])

sorted(people,key=lambda x:x[1],reverse=True)



#lambda是一個用完即丟的函數意
#順序倒過來就用reverse=Ture
#key是排序用的