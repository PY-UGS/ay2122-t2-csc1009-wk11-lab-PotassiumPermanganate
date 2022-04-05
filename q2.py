#! /usr/bin/env python3

class ClockTime:


    def setHours(self, hour):
        # Get hour
        self.hour = hour
    
    def setMinutes(self, minute):
        # Get min
        self.minute = minute

    def setSecond(self, second):
        # Get second
        self.second = second

    def setTime(self, hour, minute, second):
        # Get time with the above ans
        self.setHours(hour)
        self.setMinutes(minute)
        self.setSecond(second)

    def showTime(self):
        # output
        print(f'{self.hour}:{self.minute}:{self.second}')



def main():
    # init the clock
    clockTime = ClockTime()
    try:
        # input the time and then convert to number 
        # catch error
        hour = int(input('hour: '))
        minute = int(input('minute: '))
        second = int(input('second: '))

        # check limit if within range
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
