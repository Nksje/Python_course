def enter_id():
    global isikukood
    while True:
        user_id = input('Please enter your ID or type "exit": ')
        if user_id.lower() == 'exit':
            print('Goodbye!')
            quit()
        else:
            try:
                int(user_id)
                if len(user_id) != 11:
                    raise UserWarning
            except UserWarning:
                if len(user_id) > 11:
                    print('ID is too long!')
                else:
                    print('ID is too short!')
                    continue
            except ValueError:
                print('Code is not numeric!')
                continue
            else:
                isikukood = user_id
                break


def get_gender():
    if isikukood[0] not in ['9', '0']:
        if int(isikukood[0]) % 2 == 0:
            gender = 'female'
        else:
            gender = 'male'
        print('You are ' + gender)
    else:
        print('Unable to determine gender!')


def get_date_of_birth():
    if isikukood[0] not in ['9', '0']:
        if isikukood[0] in ['1', '2']:
            bcent = '18'
        elif isikukood[0] in ['3', '4']:
            bcent = '19'
        elif isikukood[0] in ['5', '6']:
            bcent = '20'
        elif isikukood[0] in ['7', '8']:
            bcent = '21'
        print(f'Your date of birth is {isikukood[5:7]}.{isikukood[3:5]}.{bcent}{isikukood[1:3]}')
    else:
        print('Can\'t determine date of birth')


def get_region():
    if '001' <= isikukood[7:10] <= '010':
        print('You were born in Kuresaare haigla')
    elif '011' <= isikukood[7:10] <= '019':
        print('You were born in Tartu Ülikooli Naistekliinik')
    elif '021' <= isikukood[7:10] <= '150':
        print('You were born in Ida-Tallinna keskhaigla, Pelgulinna sünnitusmaja')
    elif '151' <= isikukood[7:10] <= '160':
        print('You were born in Keila haigla')
    elif '161' <= isikukood[7:10] <= '220':
        print('You were born in Rapla haigla, Loksa haigla, Hiiumaa haigla')
    elif '221' <= isikukood[7:10] <= '270':
        print('You were born in Ida-Viru keskhaigla')
    elif '271' <= isikukood[7:10] <= '370':
        print('You were born in Maarjamõisa kliinikum')
    elif '371' <= isikukood[7:10] <= '420':
        print('You were born in Narva haigla')
    elif '421' <= isikukood[7:10] <= '470':
        print('You were born in Pärnu haigla')
    elif '471' <= isikukood[7:10] <= '490':
        print('You were born in Haapsalu haigla')
    elif '491' <= isikukood[7:10] <= '520':
        print('You were born in Järvamaa haigla')
    elif '521' <= isikukood[7:10] <= '570':
        print('You were born in Rakvere haigla, Tapa haigla')
    elif '571' <= isikukood[7:10] <= '600':
        print('You were born in Valga haigla')
    elif '601' <= isikukood[7:10] <= '650':
        print('You were born in Viljandi haigla')
    elif '651' <= isikukood[7:10] <= '700':
        print('You were born in Lõuna-Eesti haigla, Põlva haigla')
    else:
        print('Can\'t determine region of birth')


def validate():
    chk1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    chk2 = [3, 4, 5, 6, 7, 8, 9, 1, 2, 3]
    result = 0
    cnt = 0
    for number in chk1:
        result += number * int(isikukood[cnt])
        cnt += 1
    if result % 11 == int(isikukood[-1]):
        print('ID is valid')
    elif result % 11 == 0:
        result = 0
        cnt = 0
        for number in chk2:
            result += number * int(isikukood[cnt])
            cnt += 1
        if result % 11 == int(isikukood[-1]):
            print('Code is valid')
        else:
            print('Code is not valid')


def main_menu():
    while True:
        if not isikukood:
            enter_id()
        user_choice = input('Please choose:\n1.Get gender\n'
                            '2.Get date of birth\n3.Get region of birth\n'
                            '4.Validate\n5.Change ID\n'
                            '0.Exit\n-->')
        if user_choice == '1':
            get_gender()
        elif user_choice == '2':
            get_date_of_birth()
        elif user_choice == '3':
            get_region()
        elif user_choice == '4':
            validate()
        elif user_choice == '5':
            enter_id()
        elif user_choice == '0':
            print('Goodbye!')
            quit()


isikukood = ''
main_menu()
