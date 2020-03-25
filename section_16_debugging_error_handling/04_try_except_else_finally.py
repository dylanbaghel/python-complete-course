# try, except, else and finally

while True:
    try:
        num = int(input('Please Enter a Number: '))
    except ValueError:
        print('It is not a number.')
    else:
        print('Else Block Run after try if no error')
        print('Good job, you entered a number')
        break
    finally:
        print('Runs No Matter What')
