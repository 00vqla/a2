'''
Jobs # global integer, 100 by 2 elements
NumberOfJobs # as global integer
'''

Jobs = []  # 2d array of integer
NumberOfJobs = None

def Initialise():
    global Jobs
    global NumberOfJobs
    for x in range(100):
        Jobs.append(-1)
    NumberOfJobs = 0


Initialise()


def AddJobs(JobNumber, Priority):
    global NumberOfJobs
    global Jobs
    if NumberOfJobs != 100:
        Jobs[NumberOfJobs] = [JobNumber, Priority]
        print("Added")
        NumberOfJobs += 1
    else:
        print("Not added")