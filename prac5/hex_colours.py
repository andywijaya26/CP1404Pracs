colour_name={"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
             "azure1": "#foffff", "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4" : "#838b8b", "black": "#000000",
             "blue1" : "#0000ff"}
get_colour=input("Enter a colour: ")
while get_colour != "":
    print(("{}".format(colour_name.get(get_colour))))
    get_colour=input("Enter a colour: ")