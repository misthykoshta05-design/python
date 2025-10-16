N=int (input("Enter no of works"))
for i in range(N):
    SH,SM,EH,EM=map(int,input().split())
    start_time=SH* 60 +SM
    end_time=EH* 60 +EM
    duration=end_time-start_time
    hours=duration// 60
    minutes=duration% 60
    print(hours,minutes)
