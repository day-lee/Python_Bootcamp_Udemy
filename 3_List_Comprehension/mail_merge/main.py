open_names = open("Input/Names/invited_names.txt", "r")
names_list= open_names.readlines()

stripped_names= []
for name in names_list:
    word = name.strip()
    stripped_names.append(word)

with open("Input/Letters/starting_letter.txt") as data:
    content = data.read()

for name in stripped_names:
    with open(f"Output/ReadyToSend/Letter to {name}.txt", mode="w") as file:
        name_replaced_letter = content.replace("[name]", f"{name}")
        file.write(name_replaced_letter)