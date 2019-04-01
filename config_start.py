import configparser

parser = configparser.ConfigParser()

parser.read("config.cfg")

# print(parser.sections())
# print(parser.has_section("Section 1"))

using_time_travel = parser['DEFAULT']['USETimeTravel']
print(using_time_travel)
print(type(using_time_travel))
