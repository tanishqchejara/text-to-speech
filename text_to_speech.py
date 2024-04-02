import tkinter as tk
from tkinter import ttk
import pyttsx3
import os

class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text-to-Speech Application")
        self.engine = pyttsx3.init()  # Initialize text-to-speech engine
        
        # Text Input
        self.text_input = tk.Text(self.root, height=10, width=50)
        self.text_input.pack(pady=10)
        
        # Language Selection
        self.language_label = ttk.Label(self.root, text="Select Language:")
        self.language_label.pack()
        self.languages = {'English': 'en', 'Spanish': 'es', 'French': 'fr'} # Add more languages as needed
        self.language_var = tk.StringVar()
        self.language_dropdown = ttk.Combobox(self.root, textvariable=self.language_var, values=list(self.languages.keys()))
        self.language_dropdown.pack()
        self.language_dropdown.set('English')
        
        # Voice Selection
        self.voice_label = ttk.Label(self.root, text="Select Voice:")
        self.voice_label.pack()
        self.voices = self.get_voices()
        self.voice_var = tk.StringVar()
        self.voice_dropdown = ttk.Combobox(self.root, textvariable=self.voice_var, values=self.voices)
        self.voice_dropdown.pack()
        self.voice_dropdown.set(self.voices[0])
        
        # Speech Parameters
        self.rate_label = ttk.Label(self.root, text="Rate:")
        self.rate_label.pack()
        self.rate_slider = ttk.Scale(self.root, from_=50, to=200, length=200)
        self.rate_slider.pack()
        self.rate_slider.set(100)
        
        self.pitch_label = ttk.Label(self.root, text="Pitch:")
        self.pitch_label.pack()
        self.pitch_slider = ttk.Scale(self.root, from_=0, to=200, length=200)
        self.pitch_slider.pack()
        self.pitch_slider.set(100)
        
        self.volume_label = ttk.Label(self.root, text="Volume:")
        self.volume_label.pack()
        self.volume_slider = ttk.Scale(self.root, from_=0, to=1, length=200,    orient='horizontal')

        self.volume_slider.pack()
        self.volume_slider.set(0.5)
        
        # Playback Controls
        self.play_button = ttk.Button(self.root, text="Play", command=self.play_text)
        self.play_button.pack()
        
        self.pause_button = ttk.Button(self.root, text="Pause", command=self.pause_text)
        self.pause_button.pack()
        
        self.stop_button = ttk.Button(self.root, text="Stop", command=self.stop_text)
        self.stop_button.pack()
        
        self.save_button = ttk.Button(self.root, text="Save Audio", command=self.save_audio)
        self.save_button.pack()
        
    def get_voices(self):
        voices = self.engine.getProperty('voices')
        return [voice.name for voice in voices]
    
    def play_text(self):
        text = self.text_input.get("1.0",'end-1c')
        language = self.languages[self.language_var.get()]
        voice = self.voice_var.get()
        rate = self.rate_slider.get()
        pitch = self.pitch_slider.get()
        volume = self.volume_slider.get()
        
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('pitch', pitch)
        self.engine.setProperty('volume', volume)
        
        self.engine.setProperty('voice', voice)
        self.engine.say(text)
        self.engine.runAndWait()
        
    def pause_text(self):
        self.engine.pause()
        
    def stop_text(self):
        self.engine.stop()
        
    def save_audio(self):
        text = self.text_input.get("1.0",'end-1c')
        language = self.languages[self.language_var.get()]
        voice = self.voice_var.get()
        rate = self.rate_slider.get()
        pitch = self.pitch_slider.get()
        volume = self.volume_slider.get()
        
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('pitch', pitch)
        self.engine.setProperty('volume', volume)
        
        self.engine.setProperty('voice', voice)
        
        file_format = "mp3"  # Change file format as needed
        file_name = "output." + file_format
        self.engine.save_to_file(text, file_name)
        self.engine.runAndWait()
        os.system(f"start {file_name}")  # Open the saved audio file

root = tk.Tk()
app = TextToSpeechApp(root)
root.mainloop()
