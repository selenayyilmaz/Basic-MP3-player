import tkinter as tk
from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
import os

mixer.init()  #initializes the pygame.mixer

def updateListboxHeight():
    num_songs = listbox.size()
    listbox.config(height=num_songs)

def openFile():    #to select music files
    file_paths = filedialog.askopenfilenames(title="Select music",
                                           filetypes=(("mp3","*.mp3"),
                                                      ("all mp3","*.*")))
    if file_paths:
        for file_path in file_paths:
            addSong(file_path)

def addSong(file_path):
    try:
        file_name = os.path.basename(file_path)
        song_details = file_name.replace('.mp3','')
        if song_details:
            listbox.insert(tk.END,song_details)
            updateListboxHeight()
    except Exception as e:
        print(f"Dosya açılmadı: {e}")

def goToSecondWindow(event):
    selected_song = listbox.get(listbox.curselection())
    if selected_song:
        createSecondWindow(selected_song)


def pause():
    mixer.music.pause()

def play():
    song = listbox.get(tk.ACTIVE)
    song_path = f'C:/Users/cfryl/OneDrive/Desktop/musicpython/{song}.mp3'
    mixer.music.load(song_path)
    mixer.music.play()
    updateLabel(song)


def resume():
    mixer.music.unpause()

def nextMusic():
    current_selection = listbox.curselection()
    if current_selection:
        next_music = current_selection[0] + 1  # index version
        if next_music < listbox.size():
            listbox.selection_clear(0, tk.END)
            listbox.selection_set(next_music)
            listbox.activate(next_music)
            song = listbox.get(next_music)
            to_next = f'C:/Users/cfryl/OneDrive/Desktop/musicpython/{song}.mp3'
            mixer.music.load(to_next)
            mixer.music.play()
            updateLabel(song)

def previousMusic():
    current_selection = listbox.curselection()
    if current_selection:
        previous_music = current_selection[0] - 1  # index version
        if previous_music >= 0:
            listbox.selection_clear(0,tk.END)
            listbox.selection_set(previous_music)
            listbox.activate(previous_music)
            song = listbox.get(previous_music)
            to_previous = f'C:/Users/cfryl/OneDrive/Desktop/musicpython/{song}.mp3'
            mixer.music.load(to_previous)
            mixer.music.play()
            updateLabel(song)

def goToTheList(second_window):
    second_window.destroy()
    window.deiconify()

def createSecondWindow(song, canvas=None):
    global second_window, label
    second_window = tk.Toplevel(window)
    second_window.title("SellyPlayer")
    second_window.geometry("500x100")
    second_window.config(bg="#E5C1CD")


    label = tk.Label(second_window,text=f"{song} is playing", font=("Stencil Std",10),bg="#F2E0E6")
    label.pack(pady=40)

    button = tk.Button(second_window,text="Go To The List",command=lambda: goToTheList(second_window))
    button.place(x=5,y=10)

    pause_button = tk.Button(second_window,text="Stop",command=pause,width=7)
    pause_button.place(x=150,y=65)

    play_button = tk.Button(second_window, text="Play", command=play, width=7)
    play_button.place(x=100, y=65)

    resume_button = tk.Button(second_window, text="Resume", command=resume, width=7)
    resume_button.place(x=200, y=65)

    next_button = tk.Button(second_window, text="Next", command=nextMusic, width=7)
    next_button.place(x=250, y=65)

    previous_button = tk.Button(second_window, text="Previous", command=previousMusic, width=7)
    previous_button.place(x=50, y=65)

    window.withdraw()
    second_window.mainloop()

def updateLabel(song):
    label.config(text=f"{song} is playing")
def FirstWindow():
    global window, listbox
    window = tk.Tk()

    window.title("SellyPlayer")
    window.geometry("520x520")
    window.config(bg="#E5C1CD")

    scrollbar = Scrollbar(window)
    scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

    s_width = window.winfo_screenwidth()

    listbox = Listbox(window,width=s_width,height=25,
                         selectmode=tk.SINGLE,
                         bg="#F2E0E6",
                         yscrollcommand=scrollbar.set)
    listbox.pack(pady=50)

    listbox.bind('<<ListboxSelect>>',goToSecondWindow)

    button = tk.Button(window, text="Add Song", width=10, height=1, command=openFile)
    button.place(x=5, y=10)

    window.mainloop()

FirstWindow()


















