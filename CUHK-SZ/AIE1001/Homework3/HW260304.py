class Time:
    def __init__(self, hour, minute, second):
        self.__seconds = hour * 3600 + minute * 60 + second

    def advance(self, seconds):
        self.__seconds = (self.__seconds + seconds) % (24 * 3600)

    def getHour(self):
        return self.__seconds // 3600

    def getMinute(self):
        return (self.__seconds // 60) % 60

    def getSecond(self):
        return self.__seconds % 60

clock1_input = input().split()
clock2_input = input().split()
clock1 = Time(int(clock1_input[0]),int(clock1_input[1]), int(clock1_input[2]))
clock2 = Time(int(clock2_input[0]),int(clock2_input[1]), int(clock2_input[2]))

q = int(input())
for i in range(q):
    a = input().split()
    clockId = int(a[0])
    seconds = int(a[1])
    if clockId == 1:
        clock1.advance(seconds)
    else:
        clock2.advance(seconds)
    print(clock1.getHour(), clock1.getMinute(), clock1.getSecond(), clock2.getHour(), clock2.getMinute(), clock2.getSecond())

