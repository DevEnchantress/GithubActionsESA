import datetime

def get_wochentage():
    wochentage = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
  return wochentage[datetime.datetime.now().wochentage()]

print ("Hallo, schön, dass du da bist.")
print (f"Heute  ist {get_wochentage()}.")
print ("Hab noch einen schönen Tag.")
