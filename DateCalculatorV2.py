import datetime
date = True
#Defines current date as mydate
mydate = datetime.date(1,1,1)
mydate = mydate.today()


#FUNCTIONS
#############################################################################

#Check if user wants to use the program one more time
def dateagain():
    global date
    print(' ')
    print('Você deseja verificar outra data?')
    x = input('Em caso afirmativo, digite Y. Se não, digite qualquer coisa. ')
    if x == '':
        date = False
    elif x[0].lower() == 'y':
        date = True
    else:
        date = False

#############################################################################

def datecalc(nowdate,inputdate):
#Check if input dates are from future or past
    if nowdate > inputdate:
        time = 0
        datedelta = nowdate - inputdate
    elif inputdate > nowdate:
        time = 1
        datedelta = inputdate - nowdate

#Boring math to organize days into years, months and days
    datedelta = datedelta.days
    yeardelta = ((datedelta - (datedelta%365))/365)
    monthdelta = (datedelta-(yeardelta*365)-((datedelta-(yeardelta*365))%30))
    daydelta = ((datedelta-(yeardelta*365))%30)
    yeardelta += ((monthdelta-(monthdelta%12))/12)
    monthdelta -= (monthdelta-(monthdelta%12))
    
    return (yeardelta,monthdelta,daydelta,time)

#############################################################################

def user_interface(ymdt):
    #Transforming datecalc() function data into more understandable variables
    year,month,day,time = int(ymdt[0]),int(ymdt[1]),int(ymdt[2]),int(ymdt[3])

    #Creating strings for year, month and day in its plural form
    yearstr,monthstr,daystr = f"{year} anos",f"{month} meses",f"{day} dias"

    if year == 1: #Check if year = 1 so it can change to singular form
        yearstr = f"{year} ano"

    if month == 1: #Check if month = 1 so it can change to singular form
        monthstr = f"{month} mês"

    if day == 1: #Check if day = 1 so it can change to singular form
        daystr = f"{day} dia"

    if time == 0: #If time = 0, all strings should be PAST based
        infostrp = 'Da data inserida, até hoje, se passaram' #Plural form
        infostrs = 'Da data inserida, até hoje, se passou'   #Singular form

    elif time == 1: #If time = 1, all strings should be FUTURE based
        infostrp = 'De hoje, até a data inserida, restam'    #Plural form
        infostrs = 'De hoje, até a data inserida, resta'     #Singular form

#Condition checks for sorting what to show and what not
    if year > 0 and month > 0 and day > 0: #If all will be shown
        print(f"{infostrp} {yearstr}, {monthstr} e {daystr}.")

    elif year > 0 and month > 0 and day == 0: #If day wont be shown
        print(f"{infostrp} {yearstr} e {monthstr}.")

    elif year > 0 and month == 0 and day > 0: #if month wont be shown
        print(f"{infostrp} {yearstr} e {daystr}.")

    elif year == 0 and month > 0 and day > 0: #If year wont be shown
        print(f"{infostrp} {monthstr} e {daystr}.")

    elif year > 0 and month == 0 and day == 0: #If only year will be shown
        if year == 1: #Check if string will be in plural form or singular form
            print(f"{infostrs} {yearstr}.") 
        else:
            print(f"{infostrp} {daystr}.")

    elif year == 0 and month > 0 and day == 0: #If only month will be shown
        if month == 1: #Check if string will be in plural form or singular form
            print(f"{infostrs} {monthstr}.")
        else:
            print(f"{infostrp} {daystr}.")

    elif year == 0 and month == 0 and day > 0: #if only day will be shown
        if day == 1: #Check if string will be in plural form or singular form
            print(f"{infostrs} {daystr}.")
        else:
            print(f"{infostrp} {daystr}.")

#############################################################################

#While loop for program
while date == True:
    #While loop for correct input format
    while True:
        try:
            #Ask for input date
            chosendate = input('Qual data deseja verificar? dia-mes-ano(D-M-YYYY): ')
            print(' ')
            #Split the numbers from the input date to a datetime date (DD-MM-YYYY)
            date = chosendate.split('-')
            newdate = datetime.date(int(date[2]),int(date[1]),int(date[0]))
            break
        except:
            #Error message incase of user input formating error
            print("Formatação inválida. Tente novamente.")
            print(' ')

    #Program Logic
    datedif = datecalc(mydate,newdate)
    user_interface(datedif)
    dateagain()