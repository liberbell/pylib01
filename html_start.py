from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag: ", tag)
        pos = self.getpos()
        print("At line: ", pos[0]," and char: ", pos[1])
        if len(attrs) > 0:
            print("\tAttributes")
            for a in attrs:
                print("\t",a[0],"=",a[1])

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        pass

    def handle_comment(self, data):
        pass

parser = MyHTMLParser()

f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()
    parser.feed(contents)
