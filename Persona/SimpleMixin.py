import json as JSON


class Person:
    def __init__(self, name: str = "") -> None:
        self.name = name


class DictMixin:
    def to_dict(self) -> dict:
        dictionary = {
            "name": self.name,
            "skills": self.skills,
            "family": self.family
        }
        return dictionary


class JsonMixin:
    def to_json(self) -> str:
        dictionary = {
            "name": self.name,
            "skills": self.skills,
            "family": self.family
        }
        json = JSON.dumps(dictionary)
        return json


# employee = Employee("Pablo", ["Cocinar", "Programar"], {"madre":"Carla"})

class Employee(Person, DictMixin, JsonMixin):
    def __init__(self, name: str = "", skills: list = None, family: dict = None) -> None:
        super().__init__(name)
        self.employee_name = self.name
        self.skills = skills
        self.family = family
