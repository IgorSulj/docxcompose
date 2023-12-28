class Frozen:
    def __setattr__(self, name: str, value: object) -> None:
        if getattr(self, "_frozen", False):
            raise AttributeError(f"{self.__class__.__name__} is frozen")
        else:
            super().__setattr__(name, value)

