from abc import ABC, abstractmethod
from typing import Iterable, Union

from docx.text.run import Run

from docxcompose.frozen import Frozen

ElementLike = Union["Element", str, int, float]

IntoElement = Union[ElementLike, Iterable[ElementLike]]


class Element(ABC, Frozen):
    @abstractmethod
    def _add_to_run(self, run: Run):
        pass

    @staticmethod 
    def coerce_one(element: ElementLike) -> "Element":
        if isinstance(element, Element):
            return element
        else:
            return Text(element)

    @staticmethod
    def coerced(element: IntoElement) -> Iterable["Element"]:
        if isinstance(element, Element):
            yield element
        elif isinstance(element, (str, int, float)):
            yield Text(element)
        else:
            for e in element:
                yield Element.coerce_one(e)


class Text(Element):
    __slots__ = ("text", "_frozen")

    def __init__(self, text: Union[str, int, float]) -> None:
        self.text = str(text)
        self._frozen = True
    
    def _add_to_run(self, run: Run):
        run.add_text(self.text)
