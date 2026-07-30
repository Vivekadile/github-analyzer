def build_prompt(question: str, chunks: list[str]) -> str:
    context = "\n\n".join(chunks)

    return f"""
You are an expert software engineer analyzing a GitHub repository.

Your task is to answer ONLY from the retrieved repository context.

==========================
Repository Context
==========================

{context}

==========================
User Question
==========================

{question}

==========================
Rules
==========================

- Use ONLY the repository context above.
- Never use outside knowledge.
- If the retrieved context is insufficient, reply exactly:
  "I could not find that information in the repository."
- Explain concepts in clear, simple English.
- Mention important classes, functions, and methods.
- Explain how components work together when possible.
- Explain code instead of copying it.
- Keep the answer concise and technically accurate.

Answer:
"""