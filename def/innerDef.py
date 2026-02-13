
'''
#内部関数
#関数の中に定義した別の関数、外部の関数から呼び出せる、そして外側の関数を参照できる。（カプセル化）
外部から呼ばれたくない処理の記述や、外側の変数を使って内側の変数で処理をする際に使用する（クロージャ）
コードを分けて整理する際に有効
'''
#内部関数
def process_user(name,age):
    def validate(): #内部関数
     if not name or not isinstance(age,int)or age<0:
        raise ValueError('無効な入力です')
    validate()
    print(f'{name}({age})の処理を実行しました')
process_user("太郎",25)

'''
クロージャ

'''
def make_multiplier(factor):#factorがクロージャ(multiplyから参照している)
    def multiply(x):
        return x * factor
    return multiply
times3=make_multiplier(3) #multiply(x) return x*3　
print(times3(10)) #xに10が入る

'''
nonlocal
内部から外部の変数を書き換えること
'''
def outer(y):
    x=0
    def inner():
       # x=x+1 #内部から外部の変数を書き換えることはできない
       nonlocal x #内部→外部の変数の書き換えが可能になる
       x=x+1
       print(x,y)
    inner()
    print(x)
outer(12)
