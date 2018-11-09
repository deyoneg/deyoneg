class Circle:
    def __init__(self, r):
        self.r = r
        self.__pr_attr = 0

    def get_attr(self):
        return self.__pr_attr

    def __repr__(self):
        return f"Circle {self.r}"

    def set_attr(self,value):
        if value < 100:
            self.__pr_attr = value

c1=Circle(5)
print (c1)
c1.set_attr(30)

print (c1.get_attr())
