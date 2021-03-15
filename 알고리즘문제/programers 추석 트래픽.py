def solution(lines):
    answer = 0
    ss=[]
    during=[]
    sf=[]
    for x in lines:
        tmp=x.split()
        ss.append(tmp[1])
        during.append(tmp[2][0:-1])
    for x in range(len(ss)):
        tmp=makesf(ss[x],during[x])
        sf.append(tmp)
    start=ss[0]
    
    return answer
t=["2016-09-15 03:10:33.020 0.011s"]
l= [ "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"]
def makesf(time,d):
    print(time)
    during=float(d)
    hms=time.split(":")
    print(hms)
    s=float(hms[2])
    m=int(hms[1])
    h=int(hms[0])
    sstart=s-during+0.001
    sstart=round(sstart,4)
    print(h,m,sstart)
    print(h,m,s)
    return 0
solution(t)
