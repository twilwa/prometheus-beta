import datetime

def get_current_date_formatted() -> str:
    """
    Returns the current date in YYYY-MM-DD format.

    Returns:
        str: Current date as a string in 'YYYY-MM-DD' format.
    """
    return datetime.date.today().strftime('%Y-%m-%d')