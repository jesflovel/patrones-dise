from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    '''
    La clase mediador contendrá los elementos que se comunicaran con
    los demás componentes. en este caso sender y event como objeto y 
    cadena respectivamente.
    '''
    """
    The Mediator interface declares a method used by components to notify the
    mediator about various events. The Mediator may react to these events and
    pass the execution to other components.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    #Esta clase encapsula las relaciones entre los componentes
    
    def __init__(self, component1: Component1, component2: Component2) -> None:
        self._component1 = component1
        self._component1.mediator = self
        self._component2 = component2
        self._component2.mediator = self

    def notify(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._component1.do_b()
            self._component2.do_c()


class BaseComponent:
    """
    The Base Component provides the basic functionality of storing a mediator's
    instance inside component objects.
    """
    #se inicia el mediador
    def __init__(self, mediator: Mediator = None) -> None:
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


"""
Concrete Components implement various functionality. They don't depend on other
components. They also don't depend on any concrete mediator classes.
"""


class Component1(BaseComponent):
#do_a define que el componente 1 hace la actividadA
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.mediator.notify(self, "A")
#do_b define que el componente 1 hace la actividad b
    def do_b(self) -> None:
        print("Component 1 does B.")
        self.mediator.notify(self, "B")


class Component2(BaseComponent):
    '''
    component2 
    '''
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.mediator.notify(self, "D")


if __name__ == "__main__":
    # The client code.
    c1 = Component1()
    c2 = Component2()
    mediator = ConcreteMediator(c1, c2) 
    '''
    mediator contiene a concreteMediator, que a su vez contiene a c1 y c2
    '''
    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
    
    