import configparser

parser = configparser.ConfigParser()

parser.read("config.cfg")

print(parser.sections())
print(parser.has_section("Section 1"))
