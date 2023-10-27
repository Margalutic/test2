import json


with open('superhero.json', 'r') as json_file:
    data = json.load(json_file)

# Добавление двух дополнительных членов команды
extra_members = [
    {
        "name": "Speedster",
        "age": 25,
        "secretIdentity": "Barry Allen",
        "powers": ["Super speed", "Time travel"]
    },
    {
        "name": "Telepath",
        "age": 30,
        "secretIdentity": "Charles Xavier",
        "powers": ["Telepathy", "Mind control"]
    }
]

data["members"].extend(extra_members)

# Отсортировать членов команды по количеству способностей
data["members"] = sorted(data["members"], key=lambda x: len(x["powers"]))

# Создать дополнительный JSON-файл для другой команды
second_squad = {
    "squadName": "X-Men",
    "homeTown": "New York",
    "formed": 1963,
    "secretBase": "Xavier's School for Gifted Youngsters",
    "active": True,
    "members": [
        {
            "name": "Wolverine",
            "age": 150,
            "secretIdentity": "Logan",
            "powers": ["Regeneration", "Adamantium claws"]
        },
        {
            "name": "Storm",
            "age": 35,
            "secretIdentity": "Ororo Munroe",
            "powers": ["Weather manipulation", "Flight"]
        }
    ]
}

# Сохранить данные о второй команде в другой JSON-файл
with open('second_squad.json', 'w') as second_json_file:
    json.dump(second_squad, second_json_file, indent=4)

# Рассчитать средний возраст и количество способностей для членов обеих команд
total_age = 0
total_powers = 0

for member in data["members"]:
    total_age += member["age"]
    total_powers += len(member["powers"])

average_age = total_age / len(data["members"])
total_powers_in_both_teams = total_powers + sum(len(member["powers"]) for member in second_squad["members"])

print(f"Средний возраст членов первой команды: {average_age}")
print(f"Общее количество способностей в обеих командах: {total_powers_in_both_teams}")
