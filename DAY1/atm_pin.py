'''This is ATM pin_test code '''
import time
def pin_test(pin=0):
    if(pin == 0):
        return 0
    wobj = open('pin_history.log','a')
    pin = 1234
    count = 0
    while(count < 3):
        count = count + 1
        p = input('Enter a pin Number:')
        if(int(p) == pin):
            wobj.write(f'Success - pin {p} is matched at {count} date/time:{time.ctime()}\n')
            print(f'Success - pin is matched - {count}')
            break
        else:
            wobj.write(f'Failed - user input pin:{p}  not matched - {count} date/time:{time.ctime()}\n')
    if(int(p) != pin):
        print('Sorry your pin is blocked')
        wobj.write(f'Sorry your pin is blocked - {count} date/time:{time.ctime()}\n')
    wobj.close()


if __name__ == '__main__':
    pin_test(1)
