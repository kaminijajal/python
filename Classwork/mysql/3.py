import tkinter as tk
from tkinter import filedialog, ttk
import pygame
import os

# Initialize mixer
pygame.mixer.init()

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("🎵 Stylish Music Player")
        self.root.geometry("500x400")
        self.root.configure(bg="#1e1e2e")

        self.playlist = []
        self.current_index = 0
        self.is_playing = False

        # Title
        self.title_label = tk.Label(root, text="🎶 Music Player", font=("Helvetica", 18, "bold"), bg="#1e1e2e", fg="white")
        self.title_label.pack(pady=10)

        # Playlist Box
        self.playlist_box = tk.Listbox(root, bg="#2d2d44", fg="white", font=("Arial", 12), selectbackground="#00adb5", width=50, height=10)
        self.playlist_box.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(root, bg="#1e1e2e")
        btn_frame.pack(pady=20)

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 11, "bold"), padding=6)

        self.play_btn = ttk.Button(btn_frame, text="▶ Play", command=self.play_music)
        self.play_btn.grid(row=0, column=0, padx=10)

        self.pause_btn = ttk.Button(btn_frame, text="⏸ Pause", command=self.pause_music)
        self.pause_btn.grid(row=0, column=1, padx=10)

        self.stop_btn = ttk.Button(btn_frame, text="⏹ Stop", command=self.stop_music)
        self.stop_btn.grid(row=0, column=2, padx=10)

        self.next_btn = ttk.Button(btn_frame, text="⏭ Next", command=self.next_music)
        self.next_btn.grid(row=0, column=3, padx=10)

        self.prev_btn = ttk.Button(btn_frame, text="⏮ Prev", command=self.prev_music)
        self.prev_btn.grid(row=0, column=4, padx=10)

        # Load Music Button
        self.load_btn = ttk.Button(root, text="📂 Add Music", command=self.load_music)
        self.load_btn.pack(pady=5)

        # Song Label
        self.song_label = tk.Label(root, text="No song playing", font=("Arial", 12), bg="#1e1e2e", fg="lightgray")
        self.song_label.pack(pady=5)

    def load_music(self):
        files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.mp3 *.wav")])
        for f in files:
            self.playlist.append(f)
            self.playlist_box.insert(tk.END, os.path.basename(f))

    def play_music(self):
        if not self.playlist:
            return
        self.current_index = self.playlist_box.curselection()[0] if self.playlist_box.curselection() else self.current_index
        song = self.playlist[self.current_index]
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        self.is_playing = True
        self.song_label.config(text="🎧 Playing: " + os.path.basename(song))

    def pause_music(self):
        if self.is_playing:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.song_label.config(text="⏸ Paused")
        else:
            pygame.mixer.music.unpause()
            self.is_playing = True
            self.song_label.config(text="🎧 Resumed")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.song_label.config(text="⏹ Stopped")

    def next_music(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play_music()

    def prev_music(self):
        if not self.playlist:
            return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play_music()

# Run App
root = tk.Tk()
app = MusicPlayer(root)
root.mainloop()