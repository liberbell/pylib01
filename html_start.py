from html.parser import HTMLParser


class HTMLParser(HTMLParser):
    def handler_starttag(self, tag, attrs):
        pass

    def handler_endtag(self, tag):
        pass

    def handler_data(self, data):
        pass

    def handler_comment(self, data):
        pass
