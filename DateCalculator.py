import datetime
date = True
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
#Calculates the difference between the date today and the date inserted by the user
def datecalc(nowdate,inputdate):
    #Check if date has already passed or not
    #Same comments from down below apply to this part of the function
    #Strings based on future input dates
    if nowdate < inputdate:
        timedelta = inputdate - nowdate

        if timedelta.days > 365:
            if timedelta.days < 730:
                print(' ')
                print(f'De hoje até a data inserida, ainda restam 1 ano e {int(timedelta.days - ((timedelta.days -(timedelta.days % 365))/365)*365)} dias.')
                print(' ')
            else:
                print(' ')
                print(f'De hoje até a data inserida, ainda restam {int((timedelta.days -(timedelta.days % 365))/365)} anos e {int(timedelta.days - ((timedelta.days -(timedelta.days % 365))/365)*365)} dias.')
                print(' ')

        else:
            if timedelta.days != 1:
                print(' ')
                print(f'De hoje até a data inserida, ainda restam {timedelta.days} dias.')
                print(' ')
            else:
                print(' ')
                print('De hoje até a data inserida, resta apenas 1 dia, ou seja, será amanhã.')
                print(' ')

    #Check if date has already passed or not
    #Strings based on past input dates
    elif nowdate > inputdate:
        timedelta = nowdate - inputdate

        #Check if the time between the dates is more than 1 year
        if timedelta.days > 365:
            #Check if the time between the dates is more than 2 years/if its less, the year string is said in singular form(ANO)
            if timedelta.days < 730:
            #Year string in singular form (ANO)
                print(' ')
                print(f'Da data inserida até hoje, se passaram 1 ano e {int(timedelta.days - ((timedelta.days -(timedelta.days % 365))/365)*365)} dias.')
                print(' ')
            else:
            #Year string in plural form (ANOS)
                print(' ')
                print(f'Da data inserida até hoje, se passaram {int((timedelta.days -(timedelta.days % 365))/365)} anos e {int(timedelta.days - ((timedelta.days -(timedelta.days % 365))/365)*365)} dias.')
                print(' ')

        else:
            #Check if time between dates is more than 1 day
            if timedelta.days != 1:
                #Day string in plural form (DIAS)
                print(' ')
                print(f'Da data inserida até hoje, se passaram {timedelta.days} dias.')
                print(' ')
            else:
                #Day string in singular form (DIA)
                print(' ')
                print('Da data inserida até hoje, se passou apenas 1 dia, ou seja, foi ontem.')
                print(' ')
    #In case input date = today date
    else:
        print(' ')
        print(f'Tanto a data de hoje quanto a data inserida correspondem ao dia de hoje: {nowdate}')
#############################################################################


#While loop for program
while date == True:
    #While loop for correct input format
    while True:
        try:
            chosendate = input('Qual data deseja verificar? dia-mes-ano(X-X-XXXX): ')
            print(' ')
            date = chosendate.split('-')
            newdate = datetime.date(int(date[2]),int(date[1]),int(date[0]))
            break
        except:
            #Error message incase of user input formating error
            print("Formatação inválida. Tente novamente.")
            print(' ')

    #Program Logic
    datecalc(mydate,newdate)
    dateagain()