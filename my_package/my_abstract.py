from abc import ABC, abstractmethod


class MyBaseClass(ABC):
    @abstractmethod
    def my_prop(self):
        raise NotImplementedError

    def some_method(self):
        pass
