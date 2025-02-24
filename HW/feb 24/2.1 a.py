class Employee:
    def __init__(self, hourlypay, employeenumber, jobtitle):
        self.HourlyPay = hourlypay
        self.EmployeeNumber = employeenumber
        self.JobTitle = jobtitle
        self.PayYear2022 = [0.0] * 52

    def GetEmployeeNumber(self):
        return self.EmployeeNumber

    def SetPay(self, WeekNumber, HoursWorked):
        self.PayYear2022[WeekNumber - 1] = HoursWorked * self.HourlyPay

    def GetTotalPay(self):
        Total = 0
        for i in range(len(self.PayYear2022)):
            Total += self.PayYear2022[i]
        return Total


Employee1 = Employee(10, 90, "job1")
print(Employee1.GetEmployeeNumber())
Employee1.SetPay(2,12)
print(Employee1.GetTotalPay())



