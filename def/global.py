#global(バグの元)
count=0 #グローバル変数
def increment():
    # count =2 #ローカル変数
    #count=count+2 →globalを付けない場合、グローバル変数は関数内から参照はできるが変更はできない
    global count #明示的にグローバル関数を定義
    count=count+2 #globalを宣言しているとエラーにならない
    print("関数内",count)
    print("関数内(id):",id(count))

increment()
print("関数内",count)
print("関数内(id):",id(count))
