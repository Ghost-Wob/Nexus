from pathlib import Path

from app.ai.manager import AIManager
from app.markdown.exporter import MarkdownExporter


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

path = exporter.save(
    category="japanese",
    filename="test",
    title=question,
    content=answer
)

print()
print(f"Saved : {path}")
