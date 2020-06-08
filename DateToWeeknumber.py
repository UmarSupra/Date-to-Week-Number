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
        try:
            if int(date[1]) not in range(0, 13):
                print("The month you have entered is not valid. Please enter a month between 1 and 12.")
                return False
            if int(date[0]) not in range(1950, 2050):
                print("The year entered is not in the valid range. Please enter an appropriate year in the date.")
                return False
            days_in_chosen_month = int(number_of_days[date[1]])
            if int(date[2]) not in range(0, (days_in_chosen_month + 1)):
                print("The day entered is not valid. Please try entering another date.")
                return False
            else:
                return True
        except:
            print("Invalid date entered.")
            return False

    def date_verification(self):
        if len(self.date) != 10:
            print("The date isn't in the correct format of DD-MM-YYYY.")
            return False
        date = self.date.split("-")
        leap_year = self.is_leap_year(date[0])
        number_of_days = self.days_in_month(leap_year)
        date_valid = self.is_date_valid(date, number_of_days)
        return date_valid

    def date_to_week_number(self):
        import datetime
        if self.date_verification() is False:
            print("Invalid date. please try again.")
            return
        date = self.date.split("-")
        day_week_year = (datetime.date(int(date[0]), int(date[1]), int(date[2])).isocalendar())
        week_year = (str(day_week_year[1]) + "/" + str(day_week_year[0]))
        return week_year

    def week_number(self):
        import datetime
        while True:
            self.date = input("What is the date you wish to obtain the week number for? Please enter in DD/MM/YY.")
            self.date = self.date.split("/")
            self.date = "20" + self.date[2] + "-" + self.date[1] + "-" + self.date[0]
            if self.date_verification() is False:
                print("Invalid date. Please try again.")
            else:
                print("Date is correct.")
                break
        week_number = self.date_to_week_number()
        print(week_number)


while True:
    DateToWeekNumber().week_number()
