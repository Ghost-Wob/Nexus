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
        content: str
    ):

        folder = KNOWLEDGE_PATH / category

        folder.mkdir(parents=True, exist_ok=True)

        file = folder / f"{filename}.md"

        markdown = f"""---
title: "{title}"
created: "{datetime.now().isoformat()}"
---

# {title}

{content}
"""

        file.write_text(markdown, encoding="utf-8")

        return str(file)
