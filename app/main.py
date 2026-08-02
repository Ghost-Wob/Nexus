import ollama


question = input("Question : ")

response = ollama.chat(
    model="qwen3:8b",
    messages=[
        {
            "role": "system",
            "content": open(
                "app/prompts/teacher.txt"
            ).read()
        },
        {
            "role": "user",
            "content": question
        }
    ]
)

print(response["message"]["content"])
