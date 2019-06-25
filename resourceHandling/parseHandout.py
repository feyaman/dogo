from argparse import ArgumentParser

from jinja2 import Template
from bs4 import BeautifulSoup

def parseHandout(filename):
    # Read in the body of HTML
    infile = open(filename, 'r')
    start = False
    body = ''
    for line in infile:
        if not start:
            if line[:6] == '<body>':
                start = True
                body += line[6:]
        else:
            if line == '</body>\n':
                break
            body += line
    infile.close()

    # Get title
    html = open(filename, 'r').read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find_all('h1')[0].getText()
    title += ' - Machine Learning Materials'
    del(soup)

    # Create template and render
    temp_text = open('handout_template.html', 'r').read()
    template = Template(temp_text)
    rendered = template.render(title=title, content=body)
    return rendered

if __name__ == '__main__':
    # Parse arguments
    parser = ArgumentParser()
    parser.add_argument('-o', '--output', dest='outfile')
    parser.add_argument('-i', '--input', dest='infile')
    args = parser.parse_args()

    rendered = parseHandout(args.infile)

    # Write out
    fOut = open(args.outfile, 'w')
    fOut.write(rendered)