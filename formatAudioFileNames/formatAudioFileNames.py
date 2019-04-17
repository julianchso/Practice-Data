import os
import tkinter as tk
from tkinter import filedialog
from tinytag import TinyTag


# Edit music files to have format "song name - artist"
# iTunes/songs/ has hidden .jpg album files so I had to copy and paste to another folder

def format_audio_file_names():
    directory = tk.filedialog.askdirectory()
    extensions = (".mp3",".m4a")

    for root, dirs, files in os.walk(directory):  # directory where music is stored
        for name in files:
            tag = TinyTag.get(root + "\\" + name)
            if tag.artist != "":
                if name.endswith(extensions):
                    try:
                        file_ext = os.path.splitext(name)[-1]
                        old_name = os.path.join(root, name)
                        new_name = os.path.join(root, tag.title.strip() + " - " + tag.artist.strip() + file_ext)
                        print(root)
                        print(new_name)
                        os.rename(old_name, new_name)
                    except Exception:
                        pass

if __name__ == "__main__":
    format_audio_file_names()
