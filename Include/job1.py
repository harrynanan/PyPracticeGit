with open('report.txt',encoding='utf-8') as f:
    data = [i.strip() for i in f.readlines()]
grades=[]
#各科成绩总和
sub_score=[0 for i in range(9)]
for i in data[1:]:
    score = i.split()
    total = sum(list(map(int,score[1:])))
    avg = round(total/len(score[1:]),2)
    #算出各科成绩总和以及不及格的处理
    for j in range(1,len(score)):
        sub_score[j-1] = sub_score[j-1]+int(score[j])
        if(int(score[j]) <=60):
            score[j]='不及格'
    score.extend([str(total),str(avg)])
    grades.append(score)
#各科的平均分
sub_avg=list(map(lambda x:round(x/len(grades),2),sub_score))
sub_avg.extend([sum(sub_avg),round(sum(sub_avg)/len(sub_avg),2)])
sub_avg.insert(0,'平均')
sub_avg=list(map(str,sub_avg))
#按照每个人总分的大小进行排序
grades.sort(key=lambda x:x[-2],reverse=True)
#将平均分行加进去
grades.insert(0,sub_avg)
#增加序号
for i in grades:
    i.insert(0,str(grades.index(i)))
#增加title
title = ('名次 '+data[0]+' 总分 平均分').split()
grades.insert(0,title)
print(grades)
#将结果写入result文件
with open('result.txt','w',encoding='utf-8') as f:
    for i in grades:
        for j in i:
            f.write(j+' ')
        f.write('\n')
