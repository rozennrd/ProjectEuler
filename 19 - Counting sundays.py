from Timer import Timer
# calendrier
# on sait que le 1e janvier 1900 était un lundi
# il nous faudra scanner tout le calendrier, ou calculer toutes les dates des lundis


months = {1 : 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
def bisextile(year):
    if (year % 4 ==0 and year % 100 != 0) or (year % 100 == 0 and year % 400 != 0):
        months[2] = 29
    else :
        months[2] = 28



#génération du calendrier
def calendar():
    sunday_counters = 0 # initialisation du compteur de dimanches
    year = 1900
    day_of_month=1
    day_of_week = 1
    month = 1
    while True:
        day_of_month += 1
        day_of_week += 1
        if day_of_month > months[month]: # Réinitialisation du mois
            day_of_month = 1
            month += 1
            if month > 12: # Si on passe le mois de décembre, réinitialisation du mois, ajout d'une année au
                month = 1 # compteur et vérification/changement du nombre de jours en février
                year += 1
                if year == 2001 :
                    break
                bisextile(year)
        if day_of_week > 7: # Réinitialisation du jour :
            day_of_week = 1

        if year > 1900 and day_of_month == 1 and day_of_week == 7: #comptage des dimanches
            sunday_counters += 1
            print(" année ", year, " jour ", day_of_month, " mois ", month, " semaine ", day_of_week)
    return sunday_counters

with Timer() as t :
    print(calendar())
print(t.elapsed)

## compteur qui incrémente les mois de 1 à 12 puis générer date qui est le mois, le jour...
import datetime


with Timer() as t:
    month=1
    year=1901
    count_sunday = 0

    while True:
        date = datetime.date(year, month, 1)
        if date.weekday() == 6:
            count_sunday += 1
        month +=1
        if month > 12 :
            month  = 1
            year += 1
            if year == 2001:
                break
    print(count_sunday)
print(t.elapsed)
