import json
from argparse import ArgumentParser

from bs4 import BeautifulSoup
from jinja2 import Template

from parseHandout import parseHandout

if __name__ == '__main__':
    f = open('filelist.json', 'r')
    filelist = json.load(f)
    f.close()
    for filee in filelist:
        rendered = parseHandout('../resource/raw_data/' + filee['Handout'])
        f = open('../resource/' + filee['Handout'], 'w')
        f.write(rendered)

    rows = []
    row = []
    cnt = 0
    for i in range(len(filelist)):
        if cnt == 0:
            row = [filelist[i]]
            if i == len(filelist) - 1:
                rows.append(row)
            cnt = 1
            continue
        if cnt == 1:
            row.append(filelist[i])
            if i == len(filelist) - 1:
                rows.append(row)
            cnt = 2
            continue
        if cnt == 2:
            row.append(filelist[i])
            rows.append(row)
            cnt = 0
            continue

    # Create template and render
    temp_text = open('index_template.html', 'r').read()
    template = Template(temp_text)
    rendered = template.render(rows=rows)

    # Write out
    fOut = open('../resource/index.html', 'w')
    fOut.write(rendered)
