class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        # String representation of the date in day.month.year format
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        # Equality check
        return (self.day == other.day and
                self.month == other.month and
                self.year == other.year)

    def __ne__(self, other):
        # Not equal check
        return not self.__eq__(other)

    def __lt__(self, other):
        # Less than comparison
        return self.to_days() < other.to_days()

    def __gt__(self, other):
        # Greater than comparison
        return self.to_days() > other.to_days()

    def to_days(self):
        # Convert the date to the total number of days since the start of year 0
        return self.year * 360 + self.month * 30 + self.day

    @classmethod
    def from_days(cls, total_days: int):
        # Create a SimpleDate object from a total number of days
        year = total_days // 360
        total_days %= 360
        month = total_days // 30
        day = total_days % 30
        if day == 0:
            day = 30
            month -= 1
        if month == 0:
            month = 12
            year -= 1
        return cls(day, month, year)

    def __add__(self, days: int):
        # Add a certain number of days to the date
        total_days = self.to_days() + days
        return SimpleDate.from_days(total_days)

    def __sub__(self, other):
        # Subtract two SimpleDate objects and return the difference in days
        return abs(self.to_days() - other.to_days())