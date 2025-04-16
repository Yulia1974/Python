from smartphone import Smartphone


catalog = [
    Smartphone("Самсунг", "1", "+7912345678"),
    Smartphone("Онор",  "2",  "+7913594789"),
    Smartphone("Эпл", "3",  "+7919563248"),
    Smartphone("Ксиоми",  "4",  "+7923547890"),
    Smartphone("Редми",  "5",  "+7901258796")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} , {smartphone.number}")
