'''
高階関数
他の関数を引数として扱ったり、関数を戻り値として返したりする機能
a=print

変数に関数を代入する
引数として返す数に渡す（コールバック関数）
関数から関数を返す
関数内で関数を定義する
→関数を他のデータ型と同様に扱うことができる
'''



#以下は両方同じメモリになる（参照が同じ 1721538446816)
#a=print
#print(id(a))
#print(id(print))


import time
def after(seconds,func):
    time.sleep(seconds)
    func()#greetingはここで実行される
def greeting(msg):
    def inner():#クロージャーを使う
        print(msg)
    return inner

greet=greeting("HelloWorld")#greetにはreturnで返されたinnerが入る
after(2,greet)
print('処理を実行')

def process_number(number,even_callback,odd_callback):
    if number %2==0:
        even_callback(number)
    else:
        odd_callback(number)
def handle_even(number):
    print(f'{number}は偶数です')
    
def handle_odd(number):
        print(f'{number}は奇数です')

process_number(4,handle_even,handle_odd)
process_number(7,handle_even,handle_odd)
    
        

