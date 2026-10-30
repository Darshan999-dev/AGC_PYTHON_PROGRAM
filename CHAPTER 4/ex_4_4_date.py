# Exercise 4.4 - Practice: pull apart a date (YYYY-MM-DD)
date = "2026-10-18"

year = date[0:4]
month = date[5:7]
day = date[8:10]
uk_date = day + "/" + month + "/" + year

print("year:", year, "PASS" if year == "2026" else "FAIL")
print("month:", month, "PASS" if month == "10" else "FAIL")
print("day:", day, "PASS" if day == "18" else "FAIL")
print("uk_date:", uk_date, "PASS" if uk_date == "18/10/2026" else "FAIL")
