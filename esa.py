import datetime

def get_weekday():
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
    return wochentage[datetime.datetime.now().weekday()]

print("Hallo, schoen, dass du da bist.")
print(f"Heute ist {get_weekday()}.")
print("Hab noch einen schoenen Tag.")
