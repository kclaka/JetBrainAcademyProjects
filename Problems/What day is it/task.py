offset = int(input())

if offset in range(14, 15):
    print("Wednesday")
elif offset in range(-10, 15):
    print("Tuesday")
elif offset in range(-12, -8):
    print("Monday")