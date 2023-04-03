class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        x=0
        y=len(people)-1
        people.sort()
        ans=0
        while(x<=y):
            if(people[x]+people[y]<=limit):
                x+=1
                y-=1
            else:
                y-=1
            ans+=1            
        return ans 
                
           
                