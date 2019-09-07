class GetCal:

    @classmethod
    def getdayvalue(cls, reminder):
        lst = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        return lst[reminder]

    @classmethod
    def getmonthvalue(cls, actualmonth):
        lst = [0, 0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
        return lst[actualmonth]

    @classmethod
    def getyearvalue(cls, actualyear):
        lst = {'setone': 6, 'settwo': 4, 'setthree': 2, 'setfour': 0, 'setfive': 6}
        if 1600 <= actualyear <= 1699:
            return lst['setone']
        elif 1700 <= actualyear <= 1799:
            return lst['settwo']
        elif 1800 <= actualyear <= 1899:
            return lst['setthree']
        elif 1900 <= actualyear <= 1999:
            return lst['setfour']
        elif 2000 <= actualyear <= 2099:
            return lst['setfive']

    @classmethod
    def getday(cls, date, month, year):
        """
        rr=int(str(year)[2:4])
        a=int(int(str(year)[2:4]) / 4)
        b=date
        c=cls.getmonthvalue(month)
        d=cls.getyearvalue(year)
        """
        reminder = (int(str(year)[2:4]) + int(int(str(year)[2:4]) / 4) + date + cls.getmonthvalue(
            month) + cls.getyearvalue(year)) % 7
        return cls.getdayvalue(reminder)


if __name__ == "__main__":
    print("Please run the main file main.py to perform operation")
