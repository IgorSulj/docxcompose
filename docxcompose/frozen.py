class Frozen:
    __slots__ = ("_frozen",)

    def __init__(self) -> None:
        self._frozen = False
    
    def __setattr__(self, name: str, value: object) -> None:
        if self._frozen:
            raise AttributeError(f"{self.__class__.__name__} is frozen")
        else:
            super().__setattr__(name, value)

