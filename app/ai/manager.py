from pathlib import Path

import ollama
import yaml


ROOT = Path(__file__).resolve().parents[2]

CONFIG_PATH = ROOT / "config" / "config.yaml"


with open(CONFIG_PATH, "r", encoding="utf-8") as file:
    CONFIG = yaml.safe_load(file)


class AIManager:

    def __init__(self):
        self.models = CONFIG["models"]

    def ask(self, role: str, system_prompt: str, user_prompt: str):

        model = self.models.get(role)

        if model is None:
            raise ValueError(f"Unknown role: {role}")

        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ]
        )

        return response["message"]["content"]
