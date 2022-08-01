while True:
    try:
        isikukood = input('Please enter your ID or type "exit": ')
        if isikukood.lower() == 'exit':
            break
        int(isikukood)
        if len(isikukood) != 11:
            raise UserWarning
    except UserWarning:
        if len(isikukood) > 11:
            print('ID is too long!')
        else:
            print('ID is too short!')
        continue
    except ValueError:
        print('Code is not numeric!')
        continue
    else:
        while True:
            user_choice = input('Please choose:\n1.Get gender\n'
                                '2.Get date of birth\n3.Get region of birth\n'
                                '4.Validate\n5.Change ID\n'
                                '0.Exit\n-->')
            if user_choice == '1':
                if isikukood[0] not in ['9', '0']:
                    if int(isikukood[0]) % 2 == 0:
                        gender = 'female'
                    else:
                        gender = 'male'
                    print('You are ' + gender)
                else:
                    print('Unable to determine gender!')
            elif user_choice == '2':
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
            elif user_choice == '3':
                pass
            elif user_choice == '4':
                pass
            elif user_choice == '5':
                break
            elif user_choice == '0':
                print('Goodbye!')
                quit()
