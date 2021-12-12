import os
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._string = False
        self._text = []
        self.count = 0
        self.lasttag = None

    def handle_starttag(self, tag, attrs):
        if tag == "p" or "h2":
            for name, value in attrs:
                if name == "class" and value == "m-ten  m-offset-one l-eight l-offset-two textabsatz columns twelve" or "meldung__subhead columns twelve  m-ten  m-offset-one l-eight l-offset-two":
                    self.count += 1
                    self._string = True
                    self.lasttag = tag

    def handle_endtag(self, tag):
        if tag == "p" or "h2":
            self._string = False

    def handle_data(self, data):
        if self.lasttag == "p" and self._string and data.strip():
            print(data)

def main():

    parser = MyHTMLParser()

    def get_files(path):
        for root, dirs, files in os.walk(path, topdown="False"):
            for file in files:
                if file.endswith(".html") and file != "index.html":
                    with open(os.path.join(root, file), encoding="utf-8") as f:
                        html = f.read().replace("\n", " ")
                        parser.feed(str(html))

    get_files(sys.argv[1])

if __name__ == "__main__":
    main()
