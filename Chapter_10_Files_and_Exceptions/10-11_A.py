from pathlib import Path
import json

fav = int(input("What is your favourite number?"))

path = Path('fav.json')
contents = json.dumps(fav)
path.write_text(contents)