import time
start_time= time.time()
def fun():
    a=2
    v=8
    k=8
    c=a+v+k
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken) # 0.0345
