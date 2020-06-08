class DateToWeekNumber:
    def __init__(self, date=None, price=None):
        self.date = date
        self.price = price

    @staticmethod
    def is_leap_year(year):
        if int(year) % 4 == 0:
            return True
        else:
            return False

    @staticmethod
    def days_in_month(leap_year):
        number_of_days = {
            '01': '31',
            '02': '28',
            '03': '31',
            '04': '30',
            '05': '31',
            '06': '30',
            '07': '31',
            '08': '31',
            '09': '30',
            '10': '31',
            '11': '30',
            '12': '31'
        }
        if leap_year:
            number_of_days['02'] = '29'
        return number_of_days

    @staticmethod
    def is_date_valid(date, number_of_days):
        # noinspection PyBroadException
        try:
            if int(date[1]) not in range(0, 13):
                print("The month you have entered is not valid. Please enter a month between 1 and 12.")
                return False
            if int(date[2]) not in range(0, 99):
                print("The year entered is not in the valid range. Please ensure the year is between 00 and 99.")
                return False
            days_in_chosen_month = int(number_of_days[date[1]])
            if int(date[0]) not in range(0, (days_in_chosen_month + 1)):
                print("The day entered is not valid. Please try entering another date.")
                return False
            else:
                return True
        except ValueError:
            print("Invalid date entered.")
            return False

    def date_verification(self):
        if self.date[2] != "/" or self.date[5] != "/":
            print("Please reenter the date in format DD/MM/YY")
            return False
        try:
            int(self.date.replace("/", ""))
        except ValueError:
            print("Please ensure all characters except the / are integers")
        if len(self.date) != 8:
            print("The date isn't in the correct format of DD/MM/YY.")
            return False
        date = self.date.split("/")
        leap_year = self.is_leap_year("20" + date[2])
        number_of_days = self.days_in_month(leap_year)
        date_valid = self.is_date_valid(date, number_of_days)
        return date_valid

    def date_to_week_number(self):
        import datetime
        date = self.date.split("/")
        day_week_year = (datetime.date(int(date[2]), int(date[1]), int(date[0])).isocalendar())
        week_year = (str(day_week_year[1]) + "/" + str(day_week_year[0]))
        return week_year

    def week_number(self):
        import datetime
        while True:
            self.date = input("What is the date you wish to obtain the week number for? Please enter in DD/MM/YY.")
            if self.date_verification() is False:
                print("Invalid date. Please try again.")
            else:
                print("Date is correct.")
                break
        week_number = self.date_to_week_number()
        print(week_number)


while True:
    print("WARNING : This program is only meant for dates within the range of the years 20xx")
    DateToWeekNumber().week_number()
