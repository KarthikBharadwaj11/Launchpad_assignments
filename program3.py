list=[1, 2, 3, 2, 0, 65, 21, 4, 2, 10]
print(str(list))
result_list=[]
for i in range(0,len(list)):
    if list[i]==2:
        result_list.append(i)
        print(str(result_list))
