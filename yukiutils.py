import sys,time,random

def langsamschreib(str):
    speedometer = 50
    for x in str:
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/speedometer)
    print("")
