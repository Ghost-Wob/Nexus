from difflib import SequenceMatcher

from app.database.repository import ConceptRepository


class ConceptLinker:

    def __init__(self):
        self.repository = ConceptRepository()

    def find_related(self, title: str, threshold: float = 0.35):

        related = []

        for concept in self.repository.all():

            ratio = SequenceMatcher(
                None,
                title.lower(),
                concept[1].lower()
            ).ratio()

            if ratio >= threshold and concept[1] != title:
                related.append(concept[1])

        return related
