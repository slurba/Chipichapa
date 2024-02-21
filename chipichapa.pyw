from pynput import keyboard
import time
import vlc

cat1 = vlc.MediaPlayer("file:///./chipi.mp3")
cat2 = vlc.MediaPlayer("file:///./sad.mp3")
prevTime = 0
happyTime = 1
sadTime = 1.2
catVolume = 100

def on_press(key):
    try:
        chipichapa()
    except AttributeError:
        pass

def chipichapa():
    global prevTime, cat1, cat2
    #print(time.time() - prevTime)
    if prevTime == 0:
            pass
    elif time.time() - prevTime < happyTime:
        cat2.stop()
        #Start play
        cat1.play()
    elif time.time() - prevTime > sadTime:
        cat1.stop()
        cat2.play()
    else:
        #Stop play
        cat1.stop()
    if cat1.get_state() == vlc.State.Ended:
        cat1 = vlc.MediaPlayer("file:///./chipi.mp3")
    prevTime = time.time() 


def main():
    global prevTime, cat1, cat2
    #Crank up the volume
    for i in range(100):
        keyboard.Controller().press(keyboard.Key.media_volume_up)
        keyboard.Controller().release(keyboard.Key.media_volume_up)
    #Setup listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    #Set cat volumes
    cat2.audio_set_volume(catVolume) 
    cat1.audio_set_volume(catVolume)
    #Chipichapa loop (Starts sad cat if no keypresses) 
    while(True):
        if time.time() - prevTime > sadTime:
            cat1.stop()
            cat2.play()
            
            if cat2.get_state() == vlc.State.Ended:
                cat2 = vlc.MediaPlayer("file:///./sad.mp3")
                cat2.play()
        time.sleep(0.2)

if __name__ == "__main__":
    main()

    
    


