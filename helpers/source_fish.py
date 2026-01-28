import os
import shutil

items = os.listdir(os.path.expanduser("../awesome-scripts"))

def source_fish(*args, **kwargs):
    os.chdir(os.path.expanduser("~/.config/fish"))

    for item in items:
        with open("config.fish", "a") as f:
            f.write(f"source $HOME/.config/fish/functions/{item}\n")
            f.close()

source_fish()