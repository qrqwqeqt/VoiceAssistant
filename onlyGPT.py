import os
import openai

# Установите ваш ключ API OpenAI (замените 'ваш-ключ-api' на ваш настоящий ключ)
openai.api_key = "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"

# Выведите список доступных моделей
model = openai.Model.list()
# print(model)

# Создайте завершение чата
end = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Вы - полезный ассистент."},
        {"role": "user", "content": "кто самый популярный челове в мире? "}
    ]
)

# Выведите ответ ассистента
print(end.choices[0].message.content)
