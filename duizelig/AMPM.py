i = 1

a = ":00"
am = "AM"
pm = "PM"
while i <= 12:

    while j <= 12:
        print(f"{j}{a}{pm}")
        j += 1
    print(f"{i}{a}{am}")
    i += 1

    