import json
from openai import OpenAI

# GPT-5 client
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# MCP client simulation (config.json'daki serverlar)
with open("config.json", "r") as f:
    mcp_config = json.load(f)

def run_agent(user_prompt: str):
    """User prompt -> GPT-5 -> hangi MCP tool çağrılacak?"""
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Sen bir AI agentsin. Araçlar: PostgreSQL, Git, Slack. Kullanıcının isteğine göre uygun aracı seç."},
            {"role": "user", "content": user_prompt}
        ],
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "postgres_query",
                    "description": "PostgreSQL veritabanına SQL sorgusu gönder",
                    "parameters": {"type": "object","properties":{"query":{"type":"string"}},"required":["query"]}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "git_command",
                    "description": "Git komutu çalıştır",
                    "parameters": {"type": "object","properties":{"command":{"type":"string"}},"required":["command"]}
                }
            },
            {
                "type": "function",
                "function": {
                    "name": "slack_notify",
                    "description": "Slack kanalına mesaj gönder",
                    "parameters": {"type":"object","properties":{"message":{"type":"string"}},"required":["message"]}
                }
            }
        ]
    )

    return response

if __name__ == "__main__":
    while True:
        prompt = input("Kullanıcı: ")
        if prompt.lower() in ["exit", "quit"]:
            break
        output = run_agent(prompt)
        print("Agent:", output.choices[0].message)
