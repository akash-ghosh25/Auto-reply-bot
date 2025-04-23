from openai import OpenAI

client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person name Akash who speaks bengali, hindi as well as english. He is from India and is a coder. You analyze chat and respond like Akash"},
        {
            "role": "user",
            "content": "who are you"
        }
    ]
)

print(completion.choices[0].message.content)