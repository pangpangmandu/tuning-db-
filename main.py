
#-*- coding:utf-8 -*-

import csv
import io

with open('members.csv', mode='r') as inp:
    reader = csv.reader(inp)
    dict_from_csv = {rows[0]:rows[2] for rows in reader}

new_dict = { row.split('"')[5]: dict_from_csv[row].split('"')[1] for row in dict_from_csv}


student_row = []

temp = []
temp.append("학생이름")
temp.append("문제이름")
temp.append("청음 점수")
temp.append("시창 점수")
temp.append("4성 점수")
temp.append("날짜")
student_row.append(temp)

with open ('lessons.csv', mode='r') as inp2:
    log_reader = csv.reader(inp2)
    for rows in log_reader :
        single_check = False
        duo_check = False
        quartet_check = False
        single_scored = False
        duo_scored = False
        quartet_scored = False
        score_list = []

        problem_name = "none"

        single_value = "none"
        duo_value = "none"
        quartet_value = "none"
        sname = "none"
        time_str = "none"

        for row in rows :
            if "sid" in row :
                sid = row.split("\"")[1]
                student = new_dict.get(sid)
                if student == None:
                    break
                sname = student
            if "fileName" in row:
                problem_name = row.split("\"")[1]

            if "type:0" in row :
                single_check = True
            if "type:1" in row :
                duo_check = True
            if "type:2" in row :
                quartet_check = True
            if "score" in row :
                score_list.append(row)
            if "createdAt:{" in row :
                time_str = row.split("\"")[3]
            
        if len(score_list) == 3 :
            
            single_value = score_list[0]
            duo_value = score_list[1]
            quartet_value = score_list[2]

        elif len(score_list) == 2:
            single_value = score_list[0]
            duo_value = score_list[1]
        elif len(score_list) == 1:
            single_value = score_list[0]
        else :
            donothing  =1 
        
        if sname != "none" :
            temp = []
            temp.append(sname)
            temp.append(problem_name)
            temp.append(single_value)
            temp.append(duo_value)
            temp.append(quartet_value)
            temp.append(time_str)
            student_row.append(temp)


formated = []

for rr in student_row:
    temp = []
    # temp.append(u'{}\n'.format(rr[0]))
    temp.append(rr[1])
    temp.append(rr[2])
    temp.append(rr[3])
    temp.append(rr[4])
    temp.append(rr[5])
    formated.append(temp)


with io.open('result.csv', mode='wt' ,encoding='utf8') as csvfile:
    resultwriter = csv.writer(csvfile)
    for wt in formated :
        resultwriter.writerow(wt)
        




