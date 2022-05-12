# python type / dict / associative array / literal object 
# * dict = ordered 3.5 + keyed collection (collection of key=value pairs)
# formulate 
# indexxed (list) -> homegenous [10, 20, 30], [0.25,0.50, ...]
# keyed (;dict) -> mixt         {"name": "John", "age": 30}

todo = {
    # key       : value 
    "2022-01-03": "Get a Job!",
    "2022-01-01": "Start a New Happy Year!",
    "2022-01-02": "Learn python basics",
}
todo["2022-01-03"] = "Get an intership"

print(todo)