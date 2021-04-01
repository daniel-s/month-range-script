#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import arrow

def get_last_date_of_a_month(date):
    """
    Given date, returns the last day of the same month as date.
    i.e. if given 15 Jan it would return 31 Jan.
    """
    start_month = date.month
    next_try = date
    while next_try.shift(days=1).month == start_month:
        next_try = next_try.shift(days=1)
    return next_try

if __name__ == "__main__":
    # Get the first date of the month.
    for i in range(1, 13):
        month_start = arrow.get().replace(month=i, day=1)
        # This gives us the last day of the month. If we want to
        # add a buffer after the end of the month, we shift forward
        # from this last day.
        month_end = get_last_date_of_a_month(month_start)
        # I chose to shift forward 28 days (4 weeks (20 business days)), but one could
        # choose to shift forward further days to provide a buffer,
        # or use a list of known public holidays to skip over
        # if available.
        month_end_with_buffer = month_end.shift(days=28)

        # Print out results.
        print(f"Month of: {month_start.strftime('%B')} start date: {str(month_start)[:10]} to {str(month_end_with_buffer)[:10]}")
