'''
def.Generator の Docstring
Generator
    →イテレーションの仕組みを効率的に実装するための関数
    途中で処理を止めて１つずつ値を生成することが特徴
    
 yieldキーワードを使用して値を返す
 yieldで値を返した後、関数の状態を保持し、次のnext()呼び出しで処理を再開する
 →逐次処理
'''
def generator():
    yield 1
    yield 2
    yield 3

gen=generator()#ジェネレータオブジェクト（この時点ではまだ実行されない）
print(type(gen))
# print(next(gen))#1
# print(next(gen))#2
# print(next(gen))#3

for i in gen:
    print(i)
    
    
#ジェネレータ２
def print_num(max):
    print('ジェネレータ作成')
    for n in range(max):
        print(f'n:{n}')
        yield n #戻り値になり変数genに入る

gen=print_num(10)
for i in gen:#ジェネレータが返した戻り値を使用する。
    print(f'i:{i}')

import sys
N=10**6

###メモリ使用量の節約###

#普通にリストを使った場合
# def get_list():
#     return [i for i in range(N)]

# lst=get_list()
# print(sys.getsizeof(lst),'byte')#8448728 byte


# #ジェネレータを使用
# def get_gen():
#     for i in range(N):
#         yield i
# genlst=get_gen()
# print(sys.getsizeof(genlst),'byte') #200 byte

'''
サブジェネレータ
yield from 
    →ジェネレータから別のジェネレータを呼び出す
'''

def subgen():
    yield 'X'
    yield 'Y'
    return 'サブジェネレータの結果'

def main_gen():
    result=yield from subgen()#yieldの値はresultに入らずそのまま外に流れる、returnの値はresultに入る
    print(f'サブジェネレータから受け取った値:{result}')#ここに入るのはreturnの値のみ
    yield result 
    

g=main_gen()
print(next(g))
print(next(g))
print(next(g))#returnの値
print(next(g))
        
