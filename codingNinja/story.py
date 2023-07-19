def countStories(x, y, z):
    # Write your code here.
    no_of_course=z//y

    temp=no_of_course//x
    acc=0
    
    while(temp):
        no_of_course+=temp

        if (temp//2)%2==1 or temp==1:
            acc+=1
        
        
        if acc%2==0 and acc!=0:
            no_of_course+=1
            acc=0

       
        temp=temp//2
    
    return no_of_course

print(countStories(2,1,6))