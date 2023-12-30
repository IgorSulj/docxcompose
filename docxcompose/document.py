from typing import IO, Union

import docx
from docx import document

from docxcompose.elements import Element


class Document:

    def __init__(self, *elems: Element.Into) -> None:
        self._document: document.Document = docx.Document()
        for elem in elems:
            paragraph = self._document.add_paragraph()
            Element.create(elem)._add_to_paragraph(paragraph)

    def save(self, path: Union[str, IO[bytes]]) -> None:
        self._document.save(path)
