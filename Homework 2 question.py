def extract_date(date):
    crrct_date = 0
    new_date = ""

    if date.find(",") != -1:
        mnth_day, year = date.split(',')

        if mnth_day.find(" ") != -1:
            month, day = mnth_day.split(" ")

            crrct_date = 1

            day = day.strip()
            month = month.strip()
            year = year.strip()

            if month == "January":
                new_date = "1" + "/"
            elif month == "February":
                new_date = "2" + "/"
            elif month == "March":
                new_date = "3" + "/"
            elif month == "April":
                new_date = "4" + "/"
            elif month == "May":
                new_date = "5" + "/"
            elif month == "June":
                new_date = "6" + "/"
            elif month == "July":
                new_date = "7" + "/"
            elif month == "August":
                new_date = "8" + "/"
            elif month == "September":
                new_date = "9" + "/"
            elif month == "October":
                new_date = "10" + "/"
            elif month == "November":
                new_date = "11" + "/"
            elif month == "December":
                new_date = "12" + "/"
            else:
                crrct_date = 0

            new_date += day + "/"

            new_date += year

    if crrct_date == 1:
        return new_date
    else:
        return ""


file = open('inputDates.txt', 'r')
file_dates = []

file_dates = file.readlines()

file.close()

for i in range(len(file_dates) - 1):
    file_dates[i] = file_dates[i][:-1]

file = open('parsedDates.txt', 'w')

for i in file_dates:
    if i == "-1":
        break
    else:
        new_date = extract_date(i)
        if new_date != "":
            file.write(new_date + "\n")

file.close()

file = open('parsedDates.txt', 'r')
file_parsed_dates = []

file_parsed_dates = file.readlines()

file.close()

print("Input file content:\n")
for i in file_dates:
    print(i)

print("\nOutput file content:\n")
for i in file_parsed_dates:
    print(i)
