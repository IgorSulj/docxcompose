from typing import IO, Union

import docx
from docx import document

from docxcompose.elements import Element


class Document:
    __slots__ = ("_elements",)

    def __init__(self, *elems: Element.Into) -> None:
        self._elements = Element.iter_created(*elems)

    @property
    def elements(self):
        return self._elements

    def save(self, path: Union[str, IO[bytes]]) -> None:
        doc: document.Document = docx.Document()
        for elem in self._elements:
            paragraph = doc.add_paragraph()
            Element.create(elem)._add_to_paragraph(paragraph)
        doc.save(path)
