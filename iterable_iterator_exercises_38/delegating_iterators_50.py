from collections import namedtuple


Person = namedtuple("Person", "first last")

persons = [
        Person("jOhn", "abrAham"),
        Person("aKshay", "kuMar"),
        Person("ayuShman", "khuRana")
        ]

class PersonNames(object):

    def __init__(self, persons):
        try:
            self._persons = [
                    person.first.capitalize() + " " + person.last.capitalize()
                    for person in persons
                    ]
        except (TypeError, AttributeError):
            self._persons = []

    def __iter__(self):
        return iter(self._persons)


if __name__ == "__main__":
    person_names = PersonNames(persons)
    for name in person_names:
        print(name)

