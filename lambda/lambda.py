'''
lambda式
名前を持たない小さな匿名関数で簡単に関数を定義できる
lambda 引数:式
匿名性が高い→変数に代入しない限り名前を持たない
単一式→複数のステートやブロックは不可
自動的な戻り値→returnは存在せず、式の評価結果が自動的に返される
関数オブジェクトを作成する→ラムダは関数オブジェクトを生成する→引数にラムダ式を入れると関数として実行できる

使い捨ての関数定義に使用する
'''

f=lambda x:x+10
print(f(3))#→x:の部分に引数が入る

f=lambda x,y: x*y
print(f(3,4))#12

#デフォルト引数の使用
f=lambda x,y=2: x** y
print(f(4))#4の2乗
print(f(3,20))#3の20乗

#1行で書ける条件式であれば使える
f=lambda x:"even" if x%2==0 else "odd"

print(f(2))#even

def process_list(numbers,func):
    for number in numbers:
        print(func(number))

numbers=list(range(5))
process_list(numbers,lambda x:x**2)
    




