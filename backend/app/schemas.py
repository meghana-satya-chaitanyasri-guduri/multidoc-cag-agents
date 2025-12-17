from dataclasses import dataclass
from typing import List

@dataclass
class PageReference:
    page_number: int
    image_uri: str
    text_snippet: str

@dataclass
class DocumentAgentResponse:
    document_name: str
    summary: str
    references: List[PageReference]

