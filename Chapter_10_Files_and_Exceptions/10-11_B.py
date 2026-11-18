from pathlib import Path
import json

path = Path('fav.json')
contents = path.read_text()
fav_num = json.loads(contents)

print(f"I know that your favourite number is {fav_num}!")