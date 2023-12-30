from docx.opc.constants import RELATIONSHIP_TYPE
from docx.oxml import OxmlElement
from docx.oxml.shared import qn
from docx.text.run import Run

from .element import Element


class Hyperlink(Element):
    __slots__ = ("to", "content", "_frozen")

    def __init__(self, to: str, text: str) -> None:
        self.to = to
        self.text = text
        self._frozen = True
    
    def _add_to_paragraph(self, paragraph):
        part = paragraph.part
        r_id = part.relate_to(self.to, RELATIONSHIP_TYPE.HYPERLINK, is_external=True)  # type: ignore
        hyperlink = OxmlElement('w:hyperlink')
        hyperlink.set(qn('r:id'), r_id)
        new_run = Run(OxmlElement('w:r'), paragraph)  # type: ignore
        new_run.add_text(self.text)
        hyperlink.append(new_run._element)
        paragraph._p.append(hyperlink)

