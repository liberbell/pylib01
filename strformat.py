from string import Template

the_str = "The quick brown fox jumps over the lazy dog"
the_templage = Template(the_str)
output_str = the_templage.substitute(animal="fox", action="jumped")
print(output_str)

args = {
"animal": "cow",
"action": "walked"
}
output_str = the_templage.substitute(args)
print(output_str)

foo = "foo"
bar = 123

product = "Widget"
price = 19.99
tax = 0.07
