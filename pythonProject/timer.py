import time
while True:
    print(time.localtime().tm_hour, time.localtime().tm_min, time.localtime().tm_sec)
    time.sleep(1)


def play_sound(filepath):
    playsound.playsound(filepath)


play_sound("C:\Users\Comp\Downloads\oh-my-god-meme.mp3")

