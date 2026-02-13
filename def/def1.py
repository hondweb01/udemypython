#関数 def
def hello():
    print("hello")

abs=hello

print(abs())

#タプルで入る
def sample4(*args):
    print(args)#値として使うときは*を外す
    
    print(type(args))

sample4(1,2,3,4,5)

# **だと辞書型になる
def sample5(**args):
    print(args)
sample5(name='ぽにお',age=20)

#アンパック(tuple型で返る)
def get_person():
    name='田中'
    age=30
    ponio='オーガポン'
    city='東京'
    
    return name,age,city,ponio

result=get_person()
print(result)

#部分的なアンパック
first,*others,last=get_person()
print(others)


#ミュータブルとイミュータブル
#引数がミュータブルなのか、イミュータブルなのかに応じて値を変更した時の動作が異なる。

#関数内での変更は呼び出しもとに反映されない

#イミュータブル(関数外で更新されない)
def try_modify_number(num):
    num+=100
    print(f'関数内：{num}')
x=5
try_modify_number(x)
print(x)


#ミュータブル(変更可能な型)
def try_modify_list(numbers):
    numbers.append(100)

my_list=[1,2,3]
try_modify_list(my_list)
print(my_list)#中で変更した値が外にまで反映される[1, 2, 3, 100]


#ミュータブルの際に中の値を外に出したくない場合は新しい変数を使う
def try_modify_list2(numbers):
    new_numbers=numbers.copy()#新しい変数に値をコピーする
    new_numbers.append(100)

my_list=[1,2,3]
try_modify_list2(my_list)
print(my_list)#コピーすると外部に影響がなくなる[1, 2, 3]





    





    
