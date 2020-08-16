def readable_timedelta(days):
    # insert your docstring here
'''the readable_timedelta functions is creayed inorder to return the week and number of days of any integer number argument give  to it'''
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s)".format(weeks, remainder)