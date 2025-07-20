
import json
from random import choice


def gen_person():
    name = ''
    tel = ''
    key = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    key = f"Abonent: {name}"

    person = {
        'name': name,
        'tel': tel
    }

    return person, key


def write_json(person_dict, val):
    try:
        data = json.load(open("../../persons_hw32.json"))
    except FileNotFoundError:
        data = {}

    data[val] = person_dict

    with open("../../persons_hw32.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person()[0], gen_person()[1])
