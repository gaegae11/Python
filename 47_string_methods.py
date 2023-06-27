# 1: Capitalize()

_txt: str = "hELlo"
txt_: str = "heLLO"

print(_txt.capitalize())
print(txt_.capitalize())

# Answer: Hello
# Answer: Hello

#-------------------------------------

# 2: Casefold()

_txt: str = "hELlo"
txt_: str = "heLLO"

print(_txt.casefold())
print(txt_.casefold())

# Answer: hello
# Answer: hello

#-------------------------------------

# 3: Center()

txt_: str = "Hello, World!"
_txt: str = "Hello, World!"

print(txt_.center(20))
print(_txt.center(20, "."))
print(_txt.center(20, "-"))
print(_txt.center(20, "_"))

# Answer:    Hello, World!
# Answer: ...Hello, World!....
# Answer: ---Hello, World!----
# Answer: ___Hello, World!____

#-------------------------------------

# 4: Count()

_txt: str = "abc_abc_abc_abc"

print(_txt.count("bc"))

# Answer: 4

#-------------------------------------

# 5: Endswith()

_txt: str = "apple"

print(_txt.endswith("e"))
print(_txt.endswith(("e", "a")))   # Tuple formate inside

# Answer: True
# Answer: True


# 5: Endswith()

_txt: str = "appla"

print(_txt.endswith(("e", "a")))   # Tuple formate inside checking more charecter

# Answer: True


# 5: Endswith()

_txt: str = "applz"

print(_txt.endswith(("e", "a")))  # Tuple formate inside checking more charecter, But when it's check 'z' in the last charecter, it's give False result.

# Answer: False

#-------------------------------------

# 6: Expandtabs()

_txt: str = "first_tab\tsecond_tab\tthird_tab"

print(_txt.expandtabs(20))

# Answer: first_tab           second_tab          third_tab

#-------------------------------------

# 7: Find()

_txt: str = "Remember to Follow in GitHub!"

possition: int = _txt.find("GitHub")
print(possition)
print(_txt[possition:])

# Answer: 22          # It's locate at index 22
# Answer: GitHub!

#-------------------------------------

# 8: Formate()

_txt: str = "Potka {subject} is doing: {action}."
print(_txt.format(subject="cat", action="meow"))

# Answer: Potka cat is doing: meow.

# Alternative way:
_txt: str = "Potka {} is doing: {}."
print(_txt.format("cat", "meow"))

# Answer: Potka cat is doing: meow.

#-------------------------------------

# 9: Format_Map()

points: dict = {"First": 10, "Second": -5}
_txt: str = "Points: ({First}, {Second})"
print(_txt.format_map(points))

# Answer: Points: (10, -5)

#-------------------------------------

# 10: Index()

_txt: str = "Remember to Follow me in GitHub!"

possition: int = _txt.index("Follow")
print(possition)
print(_txt[possition:])

# Answer: 12          
# Answer: Follow me in GitHub!

#-------------------------------------

# 11: IsAlNum()

_txt: str = "helloRaya123"
txt_: str = "helloRaya123!"   # Because here are exclamation mark symbol. ( False )

print(_txt.isalnum())
print(txt_.isalnum())

# Answer: True
# Answer: False

#-------------------------------------

# 12: 
