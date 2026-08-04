from pathlib import Path

from app.ai.manager import AIManager
from app.markdown.exporter import MarkdownExporter
from app.utils.slug import slugify
from app.database.repository import ConceptRepository
from app.knowledge.linker import ConceptLinker
from app.core.actions import ActionMenu
from app.database.repository import ConceptRepository


ROOT = Path(__file__).resolve().parents[1]

teacher_prompt = (
    ROOT /
    "app" /
    "prompts" /
    "teacher.txt"
).read_text(encoding="utf-8")


question = input("Question : ")

repository = ConceptRepository()

slug = slugify(question)

concept = repository.find_by_slug(slug)

if concept:

    print()
    print("Titre :", concept[1])
    print("Catégorie :", concept[3])
    print("Markdown :", concept[4])

    menu = ActionMenu()

    choice = menu.show()

    if choice == "1":

        print(open(concept[4], encoding="utf-8").read())

    elif choice == "9":

        exit()

    else:

        print("Fonction bientôt disponible.")

    exit()

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
