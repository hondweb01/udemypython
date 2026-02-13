# for i in range(10): #0-9
#     print(i*10)
# for i in range(2,10): #0-9
#     print(i*10)

#リストを作ることができる
list_a=list(range(2,30))
print(list_a,type(list_a))


 # _は同じ処理を実行することを意味して、変数(_)は利用しない

for _ in range(10):    
 print('A')
 
 human={
     'name':'taro',
     'age':20,
     'gender':'man'     
 }
 
 #辞書型
for value in human.values():
    print(value)
#アンパックされたkey valueの値が返る
for item in human.items():
    print(item)

names=["太郎","花子","一郎"]
ages=[25,30,35]
for name,age in zip(names,ages):
    print(f'{name}さんは{age}歳です')
    
#enumerate→インデックス付きで取得する
fruits=['grape','pine','apple']
print(list(enumerate(fruits)))

for index,fruit in enumerate(fruits):
    print(f'{index}:{fruit}')

#zip →要素の少ないほうに合わせる
class_a=['taro','jiro','kyon','teru']
class_b=['toshi','ponio','momowarou']

for ca,cb in zip(class_a,class_b):
 print(f'{ca}:{cb}')
 

# while文
count=0
while count<10:
    print(count)
    count+=1
