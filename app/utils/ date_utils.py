from datetime import datetime
from typing import Optional

class DateUtils:
    DATE_FORMATS = [
        '%Y-%m-%d',    # ISO format
        '%d/%m/%Y',    # DD/MM/YYYY
        '%m/%d/%Y',    # MM/DD/YYYY
        '%d-%b-%Y',    # DD-Mon-YYYY
    ]

    @staticmethod
    def parse_date(date_str: str) -> datetime:
        """Parse date string with multiple format support"""
        date_str = date_str.strip()
        for fmt in DateUtils.DATE_FORMATS:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        raise ValueError(f"Unable to parse date: {date_str}")

    @staticmethod
    def is_weekday(date: datetime, weekday: str) -> bool:
        """Check if date matches specified weekday"""
        weekdays = ['monday', 'tuesday', 'wednesday',
                   'thursday', 'friday', 'saturday', 'sunday']
        target_day = weekdays.index(weekday.lower())
        return date.weekday() == target_day
