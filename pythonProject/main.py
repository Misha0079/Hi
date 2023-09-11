import playsound, time

def play_sound(filepath):
    playsound.playsound(filepath)


while True:
    print(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
    time.sleep(1)
    if time.localtime().tm_hour == 19 and time.localtime().tm_min == 21:
        play_sound("C:\\Users\\Comp\\Downloads\\oh-my-god-meme.mp3")
