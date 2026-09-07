from abc import ABC, abstractmethod


class Person(ABC):

    def __init__(self, name, email):
        self._name = name
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @abstractmethod
    def display_info(self):
        pass