# n by 7 matrix
suggestions = [
    ['Reusable water bottle', '10', '5', 'n/a', 'n/a', 'Reusable water bottels can save you from wasting plastic ones', "guessed(we're working on calculating it)"],
    ['Walk or bike', '15', '10', 'n/a', 'n/a', "Walking and biking can help reduce carbon emissions because you won't have to use a car", "guessed(we're working on calculating it)"],
    ['Turn of lights', '2', '1', 'n/a', 'n/a', 'Saves electricity', "guessed(we're working on calculating it)"],
    ['Keep your tires inflated', '10', "0(you' have to do it anyways)", 'n/a', 'n/a', "This increases your car's efficiency", "guessed(we're working on calculating it)"],
    ['Eat more vegetables and fruits', '40', '10', 'n/a', 'n/a', "This is actually one of the best things you can do and it's healthy for you!", "guessed(we're working on calculating it)"],
    ['Better laundry practices', '30', '10', 'n/a', 'n/a', "Use the cold water cycle for washing cloths and do all of your laundry at once. It's even better if you don't use a dryer", "guessed(we're working on calculating it)"],
    ['Turn off AC and heater when not at home', '20', '-5', 'n/a', 'n/a', 'saves money and helps the climate!', "guessed(we're working on calculating it)"], ['RRR', '15', '2', 'n/a', 'n/a', "This one's a classic, it's good old reduce, reuse, recycle!", "guessed(we're working on calculating it)"],
    ['Use public transportation', '30', '30', 'n/a', 'n/a', 'Public transport is very nice', "guessed(we're working on calculating it)"], ['Buy an electric car', '80', '100', 'n/a', 'n/a', "This is very expensive but it's also very helpful", "guessed(we're working on calculating it)"],
    ['Change your energy provider to a reusable energy provider', '80', '50', 'n/a', 'n/a', 'The expensiveness of this varies depending on what you switch to', "guessed(we're working on calculating it)"]
]

# generates a html table from the list suggestions
def generate_table():
    columns = ["Name", "Impact(Ranked out of 100)", "Cost(Ranked out of 100)", "CO2 emissions saved(metric ton/year)", "Water saved(kiloliters/year)", "Description", "How was this ranked?"]

    table_head = f"<thead>\n<tr><th>{'</th><th>'.join(columns)}</th></tr>\n</thead>"

    table_body = "\n<tbody>\n"
    for suggestion in suggestions:
        table_body += f"<tr><td>{'</td><td>'.join(suggestion)}</td></tr>\n"
    table_body += "</tbody>\n"

    print(f"<table id=\"The table\">\n{table_head}{table_body}</table>")

# generates a list that you can copy and past into the list suggestions
def generate_list():
    input1 = input()
    res = []
    while input1 != "-1":
        res.append("[\"" + "\",\"".join(input1.split("|")) + "\"]")
        input1 = input()
    print(",\n".join(res))

# for i in range(len(suggestions)):
#     suggestions[i].insert(3, "n/a")
#     suggestions[i].insert(4, "n/a")
# print(suggestions)

input1 = input()
if input1 == "1": generate_list()
else: generate_table()

