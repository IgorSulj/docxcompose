from typing import IO, Union

import docx
from docx import document

from docxcompose.elements import Element, IntoElement


class Document:

    def __init__(self, *elems: IntoElement) -> None:
        self._document: document.Document = docx.Document()
        for elem in elems:
            run = self._document.add_paragraph().add_run()
            Element.coerced(elem)._add_to_run(run)

    def save(self, path: Union[str, IO[bytes]]) -> None:
        self._document.save(path)
