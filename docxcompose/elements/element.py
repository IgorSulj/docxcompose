from abc import ABC, abstractmethod
from typing import Iterable, Union

from docx.text.paragraph import Paragraph

from docxcompose.frozen import Frozen

ElementLike = Union["Element", str, int, float]

IntoElement = Union[ElementLike, Iterable[ElementLike]]


class Element(ABC, Frozen):
    Like = ElementLike
    Into = IntoElement

    @abstractmethod
    def _add_to_paragraph(self, paragraph: Paragraph):
        pass

    @staticmethod 
    def coerce_one(element: ElementLike) -> "Element":
        if isinstance(element, Element):
            return element
        else:
            return Text(element)

    @staticmethod
    def iter_coerced(element: IntoElement) -> Iterable["Element"]:
        if isinstance(element, Element):
            yield element
        elif isinstance(element, (str, int, float)):
            yield Text(element)
        else:
            for e in element:
                yield Element.coerce_one(e)

    @staticmethod
    def coerced(element: IntoElement) -> "Element":
        if isinstance(element, Element):
            return element
        elif isinstance(element, (str, int, float)):
            return Text(element)
        else:
            return Composed(Element.iter_coerced(element))


class Text(Element):
    __slots__ = ("text", "_frozen")

    def __init__(self, text: Union[str, int, float]) -> None:
        self.text = str(text)
        self._frozen = True
    
    def _add_to_paragraph(self, paragraph):
        paragraph.add_run(self.text)


class Composed(Element):
    __slots__ = ("elements", "_frozen")

    def __init__(self, elements: Iterable[ElementLike]) -> None:
        self.elements = Element.iter_coerced(elements)
        self._frozen = True

    def _add_to_paragraph(self, paragraph):
        for element in self.elements:
            element._add_to_paragraph(paragraph)
