import datetime 
import winsound 
#pip install Playsound
def alarm(Timing):
    #print(Timing)
    altime=str(datetime.datetime.now().strptime(Timing,"%I:%M %p"))
    #print(altime)
    altime=altime[11:-3]
    #print(altime)
    Horeal=altime[:2]
    #print(Horeal)
    Horeal=int(Horeal)
    #print(Horeal)
    Mireal=altime[3:5]
    #print(Mireal)
    Mireal=int(Mireal)
    #print(Mireal)

    print(f"Done, alarm set for {Timing}")
    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)
            elif Mireal<datetime.datetime.now().minute:
                break

if __name__ =='__main__':
    alarm('02:31 PM')

