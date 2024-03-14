from datetime import datetime
def lengthen_date(date):
    date_object = datetime.strptime(date, '%d.%m.%Y')
    day_name = date_object.strftime('%A')
    day_number = date_object.strftime('%d')
    month_name = date_object.strftime('%B')
    year = date_object.strftime('%Y')

    

    if day_number[-1] == '1':
        suffix = 'st'
    elif day_number[-1] == '2':
        suffix = 'nd'
    elif day_number[-1] == '3':
        suffix = 'rd'
    else:
        suffix = 'th'


    return f'{day_name} {day_number}{suffix} {month_name} {year}'
