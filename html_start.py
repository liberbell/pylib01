from html.parser import HTMLParser

metacount = 0

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag: ", tag)
        pos = self.getpos()
        print("At line: ", pos[0]," and char: ", pos[1])
        if len(attrs) > 0:
            print("\tAttributes")
            for a in attrs:
                print("\t",a[0],"=",a[1])

        global metacount
        if tag == "meta":
            metacount += 1

    def handle_endtag(self, tag):
        print("Encountered an end tag: ", tag)

    def handle_data(self, data):
        print("Encountered some text: ", data)

    def handle_comment(self, data):
        print("Encountered a comment: ", data)

parser = MyHTMLParser()

f = open("samplehtml.html")
if f.mode == "r":
    contents = f.read()
    parser.feed(contents)

print(f"{metacount} meta tags were found")
