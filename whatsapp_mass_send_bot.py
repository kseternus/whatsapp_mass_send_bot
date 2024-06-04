import pywhatkit

# list that will store all phone numbers you want to send a message to
numbers_list = []
# please enter you country phone prefix here
phone_prefix = '+48'

# while loop where we enter all wanted phone number, when user types Q loop ends
while True:
    enter_number = input('Enter all the phone numbers you want to send a message to\n'
                         '(type Q to stop, only numbers): ').upper()
    # to make sure we enter only digits
    try:
        # ending list
        if enter_number == 'Q':
            break
        # we check if entered number contains only digits
        int(enter_number)
        # checking if number is not duplicate
        if (phone_prefix+enter_number) in numbers_list:
            print('Number exist!')
            pass
        # if everything is ok, we add this number to list
        else:
            numbers_list.append(phone_prefix+enter_number)
        print(f'Numbers in list: {len(numbers_list)}\n{numbers_list}')
    except ValueError:
        print('Enter valid number')


how_many = int(input('How many messages you want to send? '))
message = input('Enter what message you want to send: ')

for i in range(how_many):
    for j in numbers_list:
        # 6 is wait time, in pywhatkit it is 'time.sleep(wait_time - 4)' so if you put 6 delay will be 2s
        # don't put anything lower than 4, 6 I think is the best option
        pywhatkit.sendwhatmsg_instantly(f'{j}', f'{message}', 6, tab_close=True)
