import os
from openai import OpenAI
from datetime import datetime

client = OpenAI(api_key=os.getenv("AIPROXY_TOKEN"))


async def parse_task_with_llm(task: str):
    prompt = f"""Current date: {datetime.now().strftime('%Y-%m-%d')}
    Analyze task and return JSON structure:
    {{
        "phase": "A|B",
        "task_id": "A1-A10|B1-B10",
        "steps": [{{"action": "...", "parameters": {{...}}}}]
    }}
    Task: {task}"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        response_format={"type": "json_object"}
    )

    return json.loads(response.choices[0].message.content)
