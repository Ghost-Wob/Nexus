from pathlib import Path
from datetime import datetime


ROOT = Path(__file__).resolve().parents[2]

KNOWLEDGE_PATH = ROOT / "knowledge"


class MarkdownExporter:

    def save(
        self,
        category: str,
        filename: str,
        title: str,
        content: str,
        related=None
    ):

        folder = KNOWLEDGE_PATH / category

        folder.mkdir(
            parents=True,
            exist_ok=True
        )

        file = folder / f"{filename}.md"

        related = related or []

        links = ""

        if related:

            links = "\n## Concepts liés\n\n"

            for concept in related:
                links += f"- [[{concept}]]\n"

        markdown = f"""---
title: "{title}"
created: "{datetime.now().isoformat()}"
---

# {title}

{content}

{links}
"""

        file.write_text(
            markdown,
            encoding="utf-8"
        )

        return str(file)
