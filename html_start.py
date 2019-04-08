from html.parser import HTMLParser


class HTMLParser(HTMLParser):
    def handler_starttag(self, tag, attrs):
        print("Encountered a start tag: ", tag)
        pos = self.getpos()
        print("At line: ", pos[0],"and char ", pos[1])

    def handler_endtag(self, tag):
        pass

    def handler_data(self, data):
        pass

    def handler_comment(self, data):
        pass
