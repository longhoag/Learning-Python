people = [
    {"name": "Kobe", "team": "Lakers"},
    {"name": "Curry", "team": "GSW"},
    {"name": "Kyrie", "team": "Celtics"}
]

# def f(person):
#     return person["name"]

people.sort(key=lambda person: person["name"])

print(people)