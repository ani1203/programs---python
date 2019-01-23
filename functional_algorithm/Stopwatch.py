from utilities import utility
try:
    start = 0
    stop = 0
    start_time = int(input("enter 0 to start\n"))
    if start_time == 0:
        utility.start1()
    stop_time = int(input("enter 1 to stop\n"))
    if stop_time == 1:
        utility.stop1()
    utility.elapsed_time()
except Exception as e:
    print("enter the valid values")
