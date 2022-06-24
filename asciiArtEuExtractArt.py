import re, os, json

def extractArtFromPage(htmlPage):
    art = [] # list of (asciiart, desc)

    with open(htmlPage, encoding='utf-8') as fp:
        content = fp.read()

    artPat = re.compile("""<div class="border-header border-top p-3">(.*?)</div>""", re.DOTALL)

    matches = artPat.findall(content)
    for match in matches:
        if 'googlesyndication' in match:
            continue


        hasDescription = not match.startswith('<pre')
        if hasDescription:
            description = match[0:match.find('<pre')]
            description = description.replace('<strong>', '')
            description = description.replace('</strong>', '')
        else:
            description = 'No description.'

        match = match[match.find('<pre') + 1:]

        picture = match[match.find('>') + 1:match.rfind('<')]

        art.append([picture, description])
    return art

allArt = []
for dirpath, dirnames, filenames in os.walk('www.asciiart.eu'):
    for filename in filenames:
        if not filename.endswith('.html'):
            continue # skip non-html files


        fullPath = os.path.join(dirpath, filename)
        print(fullPath)
        art = extractArtFromPage(fullPath)
        if art == []:
            continue # skip files that don't have art

        category = fullPath[len('www.asciiart.eu\\'):-5]
        category = category.replace('\\', '/')

        for art_ in art:
            art_[0] = art_[0].rstrip()
            if art_[0] == '':
                continue

            height = art_[0].count('\n') + 1
            width = max([len(line) for line in art_[0].splitlines()])

            paddedArtLines = []
            for line in art_[0].splitlines():
                paddedArtLines.append(line.ljust(width))
            paddedArt = '\n'.join(paddedArtLines)

            allArt.append({'art':paddedArt, 'desc':art_[1], 'category':category, 'width': width, 'height':height}) # ascii art, description, category

        #input('press enter to continue...')

with open('asciiartdb-asciiarteu.json', 'w', encoding='utf-8') as fp:
    fp.write(json.dumps(allArt, indent=4))

