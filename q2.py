#! /usr/bin/env python3

class ClockTime:


    def setHours(self, hour):

        self.hour = hour
    
    def setMinutes(self, minute):
        self.minute = minute

    def setSecond(self, second):
        self.second = second

    def setTime(self, hour, minute, second):
        self.setHours(hour)
        self.setMinutes(minute)
        self.setSecond(second)

    def showTime(self):
        print(f'{self.hour}:{self.minute}:{self.second}')



def main():
    clockTime = ClockTime()
    try:
        hour = int(input('hour: '))
        minute = int(input('minute: '))
        second = int(input('second: '))

        if hour >= 0 and hour <= 24 and minute <= 59 and minute >=0 and second >= 0 and second <= 59:
            clockTime.setTime(hour, minute, second) 
            clockTime.showTime()

        else:
            print('Try again')
            main()
    except ValueError:
        print('Try again')
        main()




if __name__ == "__main__":
    main()
