classes = {
    "1年A組": {"佐藤": 85, "鈴木": 92, "高橋": 78},
    "1年B組": {"田中": 88, "渡辺": 76, "山本": 90, "中村": 85},
    "1年C組": {"伊藤": 80, "山田": 83}
}


#クラス平均の平均
def class_scores(className,students):
    print(f'{className}の成績処理を開始します')
    total=0
    count=0
    
    for student,score in students.items():
        yield{
            "type":"students",
            "student_name":student,
            "score":score
        }
        total+=score
        count+=1
        
    ave=total//count if count else 0
    return {"type":"class_average",
            "average":ave}

def school_scores(classes):
    school_total=0
    class_count=0
    for class_name,students in classes.items():
        ave=yield from class_scores(class_name,students)#yieldが終わればreturnの値がaveに入る
        school_total +=ave["average"]
        class_count+=1
        school_ave=school_total//class_count if class_count else 0
        yield{
            "type":"school_average",
            "class_name":class_name,
            "school_average":school_ave
        }
            
            
        
    
    
class_scores("1年A組",classes["1年A組"])
gen=school_scores(classes)
for result in gen:
    if result["type"]=="students":
        print(f"{result["student_name"]}:{result["score"]}")
    elif result["type"]=="class_average":
        print(f'{result['class']}の平均点は{result['average']}')
    elif result["type"]=="school_average":
        print(f'学校平均：{result["school_average"]}')
    

# print("成績処理開始")

# def class_avg(s):
#     count=0
#     total=0
#     avg=0
#     count=len(classes.get(s))
#     for k,v in classes.get(s).items():
#         total+=v
#     avg=total/count
#     yield avg

   

# def school_avg():
#  for i in classes.keys():
#   rs= yield from class_avg(i)
#   yield rs
   
# g=school_avg()
# print(next(g))
# print(next(g))   
# print(next(g))     


        

    
    # avg=total/len(classes.get(s))
    # print(avg)
        
        
    
    
    
       
    
    



        
        
        
