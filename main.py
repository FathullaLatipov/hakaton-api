import openai

openai.api_key = "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"

prompt = "Ты юрист и отвечай только на юридические вопросы!!! а на остальные не юридические вопросы отвечай что Это не юридический вопрос, поэтому я не могу ответить." + "Что такое python?"
response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=0.3,
  max_tokens=800,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
)

full_text = response.choices[0].text.strip()
print(full_text)
