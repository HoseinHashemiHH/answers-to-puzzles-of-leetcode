


import time
strt_t=time.time()
def get_x():

    while True:
        try:
         x=int(input('''please enter your number: '''))
        except:
         print('please enter a round number: ')
         continue
        break
    return x

stp_t1=time.time()+get_x()
stp_t=time.ctime(stp_t1)
#import winsound
#winsound.Beep(440, 500)
# if time.time()==stp_t1:
#     winsound.Beep(300,400)

print('after {} seconds the time is {}'.format(get_x(),stp_t))
print(strt_t,stp_t1)