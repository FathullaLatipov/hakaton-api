from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai

openai.api_key = "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"


@api_view(['GET', 'POST'])
def get_api(request):
    if request.method == 'GET':
        # Обработка GET-запроса
        prompt = request.GET.get('prompt', '')
    elif request.method == 'POST':
        # Обработка POST-запроса
        prompt = request.data.get('prompt', '')
    else:
        # Возвращаем ошибку для других методов запроса
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    prompt = "Ты юрист и отвечай только на юридические вопросы!!! а на остальные не юридические вопросы отвечай что Это не юридический вопрос, поэтому я не могу ответить." + prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,  # Увеличим температуру для более разнообразных ответов
        max_tokens=2000,  # Увеличим максимальное количество токенов для получения более полного текста
        top_p=0.9,  # Увеличим значение top_p для более релевантных ответов
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    full_text = response.choices[0].text.strip()

    if "Это не юридический вопрос" in full_text:
        full_text = "Это не юридический вопрос, поэтому я не могу ответить."

    full_text = full_text.replace('\n', '\n\n')


    return Response({'result': full_text}, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def get_new_api(request):
    if request.method == 'GET':
        # Обработка GET-запроса
        prompt = request.GET.get('prompt', '')
    elif request.method == 'POST':
        # Обработка POST-запроса
        prompt = request.data.get('prompt', '')
    else:
        # Возвращаем ошибку для других методов запроса
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.5,  # Увеличим температуру для более разнообразных ответов
        max_tokens=2000,  # Увеличим максимальное количество токенов для получения более полного текста
        top_p=0.9,  # Увеличим значение top_p для более релевантных ответов
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )

    full_text = response.choices[0].text.strip()

    full_text = full_text.replace('\n', '\n\n')


    return Response({'result': full_text}, status=status.HTTP_200_OK)
