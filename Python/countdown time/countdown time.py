import time

def countdown(t):
    while t:
        #divmod method gets the dividend and the divisor then gives as outputs the quotient and the remainder.
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer)
        time.sleep(1)
        t -= 1

    print('Time is over !!')

t = input("Enter the time in seconds: ")

countdown(int(t))


