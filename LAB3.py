import calendar
c = calendar.TextCalendar(calendar.MONDAY)
year = 2022
Nomernedeli=1
mesjac = ['janvier', 'février', 'mars', 'avril',
          'mai', 'juin', 'juillet', 'août', 'septembre',
          'octobre', 'novembre' ,'décembre']

nedela = ["Lu","MA","ME","JU","VE","SA","DI"]
ii = ['01','02','03','04','05','06','07','08','09','10','11',
      '12','13','14','15','16','17','18','19','20','21','22',
      '23','24','25','26','27','28','29','30','31']

print("Bonne année  "+str(year)+" !!!")
j=0
while j<12:
    # print(j)
    month = j+1
    strrr = c.formatmonth(year,month,0,0)
    #print()
    #print(strrr)





# days and month
    for i in c.itermonthdays(year, month):
        if i != 0:
            dennedeli = calendar.weekday(year, month, i)
            if dennedeli == 0:
                Nomernedeli += 1
                print ("\nSemaine № ",Nomernedeli)
            print(str(year)+" - "+str(month)+" - "+ii[i-1]+" ("+nedela[dennedeli]+")")
    j += 1
print()
print("Bonne année  "+str(year+1)+" !!!")