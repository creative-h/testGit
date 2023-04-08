"""
Your module description

mkdir python-chatgpt
cd python-chatgpt
python3.10 -m venv openai
source /python-chatgpt/openai/bin/activate


pip install -U pip
pip install openai
"""
import openai

# openai.api_key = "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"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a chatbot"},
            {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
        ]
)

result = ''
for choice in response.choices:
    result += choice.message.content

print(result)
