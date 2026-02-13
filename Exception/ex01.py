grades = {
    "math": [85, 92, 78, 90, 88],
    "english": [88, 76, 95, 82, 91],
    "science": [91, 87, 84, 89, 93]
}



try:
   subjects=input('科目名の入力：')
   print(subjects)
   if subjects!="math" and subjects!="english" and subjects!="science":
        raise Exception("科目が存在しません")
    
   else:
        num=int(input("学生番号を入力してください"))
        if num>=6:
            raise Exception("学生番号は5以下で入力してください")
        else:
            
         score=grades[subjects][num-1]
        if score<=0 or score>100:
            raise Exception("スコアの値は0~100の間に設定してください")
        print(score)
        if score>=90:
            print('A')
        elif score>=80:
            print('B')
        elif score>=70:
            print('C')
        elif score>=60:
            print('D')
        else:
            print('F')
except Exception as e:
    print(e)


    
    
    
     
