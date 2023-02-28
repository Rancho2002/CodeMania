if __name__ == '__main__':
    grade=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        grade.append([name,score])
    sortedMarks=sorted(list(set([x[1] for x in grade])))

    # print(sortedMarks)
    secondLow=sortedMarks[1]
    nameList=[]
    for i in grade:
        if(secondLow==i[1]):
            nameList.append(i[0])
    for names in sorted(nameList):
        print(names)