NumberOfJobs = 0  # global integer
Jobs = [[]]  # 2d array with length 100 and 2 elements


def Initialise():
    global Jobs, NumberOfJobs
    for x in range(100):
        Jobs.append([-1, -1])
    NumberOfJobs = 0


def AddJob(job_number, priority):
    global Jobs, NumberOfJobs
    if NumberOfJobs == 100:
        print("Not added")
    else:
        Jobs[NumberOfJobs] = [job_number, priority]
        print("Added")
        NumberOfJobs += 1


Initialise()
AddJob(12, 10)
AddJob(526, 9)
AddJob(33, 8)
AddJob(12, 9)
AddJob(78, 1)


def InsertionSort():
    global Jobs, NumberOfJobs
    for i in range(1, NumberOfJobs):
        jnumber = Jobs[i][0]  # the job number
        priority = Jobs[i][1]  # the priority

        while i > 0 and Jobs[i - 1][1] > priority:
            Jobs[i][0] = Jobs[i - 1][0]
            Jobs[i][1] = Jobs[i - 1][1]
            i -= 1
        Jobs[i][0] = jnumber
        Jobs[i][1] = priority


def PrintArray():
    global Jobs, NumberOfJobs
    for i in range(0, NumberOfJobs):
        print(f"{Jobs[i][0]} priority {Jobs[i][1]}")


InsertionSort()
PrintArray()
