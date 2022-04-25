i = 1
j = 1
a = ":00 "
am = "AM"
pm = "PM"
#x = i + am
while i <= 12:
    print(f"{i}{a}{pm}")
    i += 1
while j <= 12:
    print(f"{j}{a}{am}")
    j += 1