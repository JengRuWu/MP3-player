def choose():
    global playsong
    msg.set("\nNow playing: "+choice.get())
    playsong = choice.get()


def pause_mp3():
    mixer.music.pause()
    msg.set("\nStop playing {}".format(playsong))


def increase():
    global volume
    volume += 0.1
    if volume >= 1:
        volume = 1
    mixer.music.set_volume(volume)


def decrease():
    global volume
    volume -= 0.1
    if volume <= 0.3:
        volume = 0.3
    mixer.music.set_volume(volume)


def play_mp3():
    global playsong, preplaysong
    if playsong == preplaysong:
        if not mixer.music.get_busy():
            mixer.music.load(playsong)
            mixer.music.play(loops=-1)
        else:
            mixer.music.unpause()
        msg.set("\nNow playing: {}".format(playsong))
    else:
        play_new()
        preplaysong=playsong


def play_new():
    global playsong
    mixer.music.stop()
    mixer.music.load(playsong)
    mixer.music.play(loops=-1)
    msg.set("\nNow playing: {}".format(playsong))


def stop_mp3():
    mixer.music.stop()
    msg.set("\nMusic stopped!")


def exit_mp3():
    mixer.music.stop()
    win.destroy()


from pygame import mixer
import tkinter as tk
import glob

mixer.init()
win = tk.Tk()
win.geometry("640x380")
win.title("MP3 Player")

title_label = tk.Label(win, text="MP3 Player", fg="red", font=("Arial", 16))
title_label.pack()

frame01 = tk.Frame(win)
frame01.pack()

source_dir = "MP3/"
MP3_files = glob.glob(source_dir + "*.mp3")

playsong = preplaysong = ""
index = 0
volume = 0.6
choice = tk.StringVar()

for mp3 in MP3_files:
    rbtem = tk.Radiobutton(frame01, text=mp3, variable=choice, value=mp3, command=choose)
    if index == 0:
        rbtem.select()
        playsong = preplaysong = mp3
    rbtem.grid(row=index, column=0, sticky="w")
    index += 1

msg = tk.StringVar()
msg.set("\nNow playing:")
play_label = tk.Label(win, textvariable=msg, fg="blue", font=("Arial", 12))
play_label.pack()
sep = tk.Label(win, text="\n")
sep.pack()

frame02 = tk.Frame(win)
frame02.pack()
btn1 = tk.Button(frame02, text="Play", width=8, command=play_mp3)
btn1.grid(row=0, column=0, padx=5, pady=5)
btn2 = tk.Button(frame02, text="Pause", width=8, command=pause_mp3)
btn2.grid(row=0, column=1, padx=5, pady=5)
btn3 = tk.Button(frame02, text="Volume +", width=8, command=increase)
btn3.grid(row=0, column=2, padx=5, pady=5)
btn4 = tk.Button(frame02, text="Volume -", width=8, command=decrease)
btn4.grid(row=0, column=3, padx=5, pady=5)
btn5 = tk.Button(frame02, text="Stop", width=8, command=stop_mp3)
btn5.grid(row=0, column=4, padx=5, pady=5)
btn6 = tk.Button(frame02, text="Exit", width=8, command=exit_mp3)
btn6.grid(row=0, column=5, padx=5, pady=5)
win.protocol("WM_DELETE_WINDOW", exit_mp3)
win.mainloop()
