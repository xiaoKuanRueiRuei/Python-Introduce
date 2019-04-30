#any(iterable)
#Return Ture if any element of the iterable id ture.
#If the iterable is empty,return False.
#Equivalent to :
def any(iterable):
    for element in iterable:
        if element:
            return True
    return False
#input-->any(c.isupper() for c in "Hello")-->
#裡面有一個大寫就對了
#input-->any(c in ["!","@"."#","$"] for c in iPhone@Apple)-->
#iPhone@Apple是密碼，在密碼中有前述4個特殊字元，所以正確
#input-->all(c.isupper() for c in "Hello")-->
#裡面有一個大寫就錯了
#input-->all(c in ["!","@"."#","$"] for c in iPhone@Apple)-->
#iPhone@Apple是密碼，在密碼中有前述4個特殊字元，所以錯誤
#all跟any的差異在，any是只要一個有就可以了，all是要全部都符合才正確
def check_password(a):
    return all([
        any(c.isupper()for c in a),
        any(c.islower()for c in a),
        any(c.isdigit()for c in a),
        any(c in ["!","@","#","$"]for c in a),
        len(a)>=8])