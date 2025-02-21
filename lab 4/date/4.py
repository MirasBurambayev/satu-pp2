from datetime import datetime

date1 = datetime(2024, 11, 220, 14, 30, 0)
date2 = datetime(2025, 2, 20, 12, 15, 0)

difference_in_seconds = int((date1 - date2).total_seconds())
print(difference_in_seconds)
