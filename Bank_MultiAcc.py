# Non-OOP Bank
# Version 5
# Any number of accaunts - with a list of dictionaries

# 1
# Создается список аккаунтов, который будет содержать словари аккаунтов
# Словарь каждого аккаунта содержит имя, баланс и пароль. Номер аккаунта =
# индексу словаря в списке.

# accountList - приходится передавать в каждую функцию, как глобальную переменную

accountList = []

def newAccount(aName, aBalance, aPassword):
    global accountList
    newAccountDict = {'name':aName, 'balance':aBalance, 'password':aPassword}
    accountList.append(newAccountDict)

def show(accountNumber):
    global accountList
    if accountNumber >= len(accountList):
        print('Такого счета не существует!')
        return None
    else:
        print('Номер счета: ', accountNumber)
        thisAccountDict = accountList[accountNumber]
        print('      Имя: ', thisAccountDict['name'])
        print('      Остаток на счете: ', thisAccountDict['balance'])
        print('      Пароль: ', thisAccountDict['password'])
        print()

def getBalance(accountNumber, userPassword):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if userPassword != thisAccountDict['password']:
        print('Вы ввели неверный пароль!')
        return None
    return thisAccountDict['balance']

def setChangeBalance(accountNumber, userChangeAmount, userPassword, action):
    global accountList
    thisAccountDict = accountList[accountNumber]
    if userPassword != thisAccountDict['password']:
        print('Вы ввели неверный пароль!')
        return None
    if action == 'd':
        if userChangeAmount <= 0:
            print('Сумма депозита должна быть больше 0!')
            return None
        thisAccountDict['balance'] = thisAccountDict['balance'] + userChangeAmount

    if action == 'w':
        if userChangeAmount <= 0:
            print('Сумма для снятия должна быть больше 0!')
            return None
        if userChangeAmount > thisAccountDict['balance']:
            print('Сумма для сняти превышает текущий баланс')
            return None
        thisAccountDict['balance'] = thisAccountDict['balance'] - userChangeAmount

    return thisAccountDict['balance']



# main Code

# Создадим пару аккаунтов, чтобы что-то уже было в списке
print("Joe's account is account number: ", len(accountList))
newAccount("Joe", 100, 'soup')

print("Mary's account is account number: ", len(accountList))
newAccount("Mary", 12345, 'nuts')

# Основное тело кода, вызов соответствующих выбору полльзователя процедур
while True:
    print()
    print('Нажмите "b", чтобы посмотреть баланс')
    print('Нажмите "n", чтобы создать новый счет')
    print('Нажмите "d", чтобы пополнить депозит')
    print('Нажмите "w", чтобы снять наличные')
    print('Нажмите "s", чтобы посмотреть аккаунт')
    print('Нажмите "q", чтобы выйти')

    action = input('Что бы Вы хотели сделать сейчас? Нажмите нужный символ: ')
    action = action.lower()
    action = action[0] # Эти 2 строки берут первую маленькую букву выбора

    print()

    if action == 'n': # Новый счет
        print('Новый счет:')
        userName = input('Введите Ваше имя: ')
        userStraightAmount = input('Каков будет Ваш первоначальный взнос? ')

# поскольку с клаиватуры прилетает СТРОКА, я ее сперва привожу к
# вещественному числу, затем окургляю до целого и после этого
# привожу его к типу int:
        userStraightAmount = int(round(float(userStraightAmount)))
        userPassword = input('Введите пароль, который будете использовать для доступа к счету: ')

        userAccountNumber = len(accountList)
        newAccount(userName, userStraightAmount, userPassword)
        print('Номер вашего счета: ', userAccountNumber)

    elif action == 's': # Показать счет
        print('Информация о счете:')
        userAccountNumber = input('Укажите номер интересующего Вас счета: ')
        userAccountNumber = int(round(float(userAccountNumber)))
        show(userAccountNumber)

    elif action == 'q': # Выход из программы
        break

    elif action == 'b': # Посмотреть бвланс
        print('Проверить баланс')
        userAccountNumber = input('Введите номер счета: ')
        userAccountNumber = int(round(float(userAccountNumber)))
        userPassword = input('Введите пароль от счета: ')
        theBalance = getBalance(userAccountNumber, userPassword)
        if theBalance is not None:
            print('Баланс счета номер %d - %d' % (userAccountNumber, theBalance))

    elif action == 'd': # Внести депозит
        print('Внести депозит')
        userAccountNumber = input('Введите номер счета: ')
        userAccountNumber = int(round(float(userAccountNumber)))
        userPassword = input('Введите пароль от счета: ')
        userDepositAmount = input('Введите сумму депозита: ')
        userDepositAmount = int(round(float(userDepositAmount)))
        theBalance = setChangeBalance(userAccountNumber, userDepositAmount, userPassword, action)
        if theBalance is not None:
            print('Счет №%d пополнен. Баланс счета: %d' % (userAccountNumber, theBalance))

    elif action == 'w': # Снять наличные
        print('Снять наличные')
        userAccountNumber = input('Введите номер счета: ')
        userAccountNumber = int(round(float(userAccountNumber)))
        userPassword = input('Введите пароль от счета: ')
        userWithdrawAmount = input('Введите сумму для выдачи: ')
        userWithdrawAmount = int(round(float(userWithdrawAmount)))
        theBalance = setChangeBalance(userAccountNumber, userWithdrawAmount, userPassword, action)
        if theBalance is not None:
            print('Наличные выданы. Баланс счета №%d: %d' % (userAccountNumber, theBalance))

    print('Done!')
