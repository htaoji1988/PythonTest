class PrintData():
    day = 0
    mounth = 0
    year = 0

    def __init__(self, year, mounth, day):
        self.year = year
        self.mounth = mounth
        self.day = day

    @classmethod
    def GetData(cls, string_data):
        year, mounth, day = map(int, string_data.split("-"))
        date1 = cls(year, mounth, day)
        return date1

    def OutPut(self):
        print("year:", self.year)
        print("mounth:", self.mounth)
        print("day:", self.day)


t = PrintData.GetData("2017-1-16")
t.OutPut()
