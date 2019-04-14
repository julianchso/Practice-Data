import os
from tinytag import TinyTag

# Edit music files to have format "song name - artist"
# iTunes/songs/ has hidden .jpg album files so I had to copy and paste to another folder

for root, dirs, files in os.walk("C:/Users/username/Desktop/Music/"):  # directory where music is stored
    for name in files:
        tag = TinyTag.get(root + "\\" + name)
        if tag.artist != "":
            if name.endswith((".mp3",".m4a")):
                try:
                    file_ext = os.path.splitext(name)[-1]
                    old_name = os.path.join(root, name)
                    new_name = os.path.join(root, tag.title + " - " + tag.artist + file_ext)

                    print(new_name)
                    os.rename(old_name, new_name)
                except Exception:
                    pass
