#inheritance acquiring properties of parent class
#place parent class name / import
# if you have constructor which is not default make sure to call parent constructor and child constructor


from OopsDemo import Calculator


class ChildImpl(Calculator):
    num2= 200

    def __init__(self): #child constructor
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj = ChildImpl()
print(obj.getCompleteData())