from datetime import datetime

class DateHelper:

    def get_today_date(self):

        return datetime.now().strftime(
            "%b %d, %Y"
        ).replace(
            " 0",
            " "
        )

    def extract_date(self, datetime_string):

        return datetime.strptime(
            datetime_string,
            "%b %d, %Y %I:%M:%S %p"
        ).strftime(
            "%b %d, %Y"
        ).replace(
            " 0",
            " "
        )