#Funny project just as a test
import os
import webbrowser
from pathlib import Path

confirmlist = ["yes", "YES", "yeah", "y", "Y"]
pathtogame = Path("C:\Program Files (x86)\Steam\steamapps\common\Overwatch")
decision = input("Would you like to play better games? ")
url = "https://www.roblox.com/games/920587237/Adopt-Me"

if decision in confirmlist:
    if os.path.exists(pathtogame):
        print("pretends to delete game")
        webbrowser.open(url)

