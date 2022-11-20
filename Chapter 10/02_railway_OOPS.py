class RailwayForm():
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

honeysApplication = RailwayForm()
honeysApplication.name = "Honey"
honeysApplication.train = "Rajdhani Express"

honeysApplication.printData()