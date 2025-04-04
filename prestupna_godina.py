# Python program koji racuna prestupnu godinu

user = input("Unesite godinu: ")
godina = int(user)

if godina%4 == 0 and godina%100 != 0:
    print(f"Godina {godina} je prestupna.")
elif godina%400 == 0:
    print(f"Godina {godina} je prestupna.")
else:
    print(f"Godina {godina} nije prestupna.")