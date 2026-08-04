from pathlib import Path

from app.ai.manager import AIManager
from app.markdown.exporter import MarkdownExporter
from app.utils.slug import slugify
from app.database.repository import ConceptRepository
from app.knowledge.linker import ConceptLinker


ROOT = Path(__file__).resolve().parents[1]

teacher_prompt = (
    ROOT /
    "app" /
    "prompts" /
    "teacher.txt"
).read_text(encoding="utf-8")


question = input("Question : ")

ai = AIManager()

answer = ai.ask(
    role="teacher",
    system_prompt=teacher_prompt,
    user_prompt=question
)

print()
print(answer)

exporter = MarkdownExporter()

linker = ConceptLinker()

related = linker.find_related(question)

path = exporter.save(
    category="japanese",
    filename=slugify(question),
    title=question,
    content=answer,
    related=related
)

repository = ConceptRepository()

slug = slugify(question)

if not repository.exists(slug):

    repository.insert(
        title=question,
        slug=slug,
        category="japanese",
        markdown=path
    )

    print("Concept ajouté à la base.")

else:

    print("Concept déjà existant.")

print()
print(f"Saved : {path}")
