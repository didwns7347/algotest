class bus:
    def __init__(self,time,cl):
        self.time=time
        self.cl=cl
        self.first=0
        self.last=0

    
def solution(n, t, m, timetable):
    answer = ''
    buses=[ ]
    a=bus([9,0],0)
    buses.append(a)
    time=[9,0]
    for x in range(n-1):
        time[1]+=t
        if time[1]>=60:
            time[0]+=1
            time[1]-=60
        buses.append(bus(time,0))
    for x in range(n):
        for y in range(46):
            if buses[x].cl==m or not timetable:
                break
            tm=timetable.pop()
            if comp(buses[x].time,tm) :
                if buses[x].cl==0:
                    buses[x].last=list(map(int,tm.split(":")))
                else:
                    if not comp(buses[x].last,tm):
                        buses[x].last=list(map(int,tm.split(":")))
                buses[x].cl+=1
            else:
                timetable.append(tm)
                
                        
                

    
    if buses[-1].cl==m:
        hm=buses[-1].last
        if hm[1]==0:
            hm[1]=59
            hm[0]-=1
        else:
            hm[1]-=1
        if hm[0]<10:
            h="0"+str(hm[0])
        else:
            h=str(hm[0])
        if hm[1]<10:
            m="0"+str(hm[1])
        else:
            m=str(hm[1])
        answer=h+":"+m
    else:
        hm=buses[-1].time
        if hm[0]<10:
            h="0"+str(hm[0])
        else:
            h=str(hm[0])
        if hm[1]<10:
            m="0"+str(hm[1])
        else:
            m=str(hm[1])
        answer=h+":"+m
        
            
            
        
    return answer
        
def comp(a,b):
    b=list(map(int,b.split(":")))
    if a[0]>b[0]:
        return True
    elif a[0]==b[0]:
        if a[1]>=b[1]:
            return True
    return False
        
    

    
print(solution(	2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]))
print(solution(	1, 1, 5, ["00:01", "00:01", "00:01", "00:01"]))
print(solution(	10, 60, 45, ["23:59", "23:59", "23:59",
                             "23:59", "23:59", "23:59",
                             "23:59", "23:59", "23:59",
                             "23:59", "23:59", "23:59",
                             "23:59", "23:59", "23:59", "23:59"]))
print(solution(	1, 1, 1, ["00:01"]))
mybus=bus([9,0],5)
print(mybus.first)
mybus.first=[9,59]

