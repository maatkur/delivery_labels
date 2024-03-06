import datetime


def get_current_date():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%d/%m/%Y")
    return formatted_date
