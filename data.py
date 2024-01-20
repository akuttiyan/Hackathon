# n by 4 matrix
suggestions = [
    ["Reusable water bottle","10","5","Reusable water bottels can save you from wasting plastic ones"],
    ["Walk or bike","15","10","Walking and biking can help reduce carbon emissions because you won\'t have to use a car"],
    ["Turn of lights","2","1","Saves electricity"],
    ["Keep your tires inflated","10","0(you\' have to do it anyways)","This increases your car's efficiency"],
    ["Eat more vegetables and fruits","40","10","This is actually one of the best things you can do and it\'s healthy for you!"],
    ["Better laundry practices","30","10","Use the cold water cycle for washing cloths and do all of your laundry at once. It\'s even better if you don\'t use a dryer"],
    ["Turn off AC and heater when not at home","20","-5","saves money and helps the climate!"]
]

def generate_table():
    columns = ["Name", "Impact(Ranked out of 100)", "Cost(Ranked out of 100)", "Description"]

    table_head = f"<thead>\n<tr><th>{'</th><th>'.join(columns)}</th></tr>\n</thead>"

    table_body = "\n<tbody>\n"
    for suggestion in suggestions:
        table_body += f"<tr><td>{'</td><td>'.join(suggestion)}</td></tr>\n"
    table_body += "</tbody>\n"

    print(f"<table id=\"The table\">\n{table_head}{table_body}</table>")
    return f"<table id=\"The table\">\n{table_head}{table_body}</table>"

def generate_list():
    input1 = input()
    res = []
    while input1 != "-1":
        res.append("[\"" + "\",\"".join(input1.split("|")) + "\"]")
        input1 = input()
    print(",\n".join(res))

input1 = input()
if input1 == "1": generate_list()
else: generate_table()