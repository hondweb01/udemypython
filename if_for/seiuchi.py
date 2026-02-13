#セイウチ演算子（代入式）→変数への値の代入と、その値の評価を同時に行える
#変数名:=式

#=========例===========
# data=get_data()
# if data:
#    process(data)

#セイウチ演算子を使用 (データ)を変数に入れる→その後ifで評価するまでを1文でできる
# if data := get_data()
# process(data)


# name=input('名前を入力：')
# if name:
#     print(f'こんにちは{name}さん')
    

# if name:=input('名前を入力してください'):
#  print(f'こんにちは{name}さん')
 
numbers=[1,2,3,4,5]
 #この時は()を付ける lengthに取り出した後で3と比較する
# if (length:=len(numbers))>3:
#      print(length)
     

# if n:=int(input("数値："))>5:
#     print(f'nは5よりも大きい')
# else:
#     print(f'nは5よりも小さい')

while(line:=input('入力：'))!='quit':
    print(f'{line}')


                
        
    
