import configparser

parser = configparser.ConfigParser()

parser.read("config.cfg")

# print(parser.sections())
# print(parser.has_section("Section 1"))

using_time_travel = parser['DEFAULT']['USETimeTravel']
# print(using_time_travel)
# print(type(using_time_travel))
#
# using_time_travel = bool(parser['DEFAULT']['USETimeTravel'])
# print(using_time_travel)
# print(type(using_time_travel))
#
# opd = parser['DEFAULT'].getboolean('ObeyPrimeDirective')
# print(opd)
# speed = parser['DEFAULT'].getfloat('Ship Speed')
# print(speed)

try:
    title = parser['Section 3']['Title']
    print(title)
except KeyError as err:
    print(err)
