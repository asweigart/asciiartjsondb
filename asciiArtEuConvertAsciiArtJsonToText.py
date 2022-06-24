# Run this after running asciiArtEuExtractArt.py

import json

with open('asciiartdb-asciiarteu.json', encoding='utf-8') as fp:
    content = json.loads(fp.read())

with open('asciiartdb-asciiarteu.txt', 'w', encoding='utf-8') as fp:
    for artData in content:
        fp.write(artData['desc'] + '\n' + str(artData['width']) + 'x' + str(artData['height']) + '\n' + artData['category'] + '\n' + artData['art'] + '\n\n\n\n\n')
