list=[1,2,-2,66,85,54,36,-3,24,666,-333,568,54,-6,78,24,66]


def inserti_sort(list):
    for i in range(0,len(list)):

        for j in range(i-1,-1,-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

inserti_sort(list)
for element in list:
    print(element)


