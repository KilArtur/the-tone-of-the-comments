import requests

if __name__ == '__main__':
    examples = [
        {
            "features": "Я ненавижу тебя, надеюсь ты в гробу перевернешься",
            "target": 1
        },
        {
            "features": "Для каких стан является эталоном современная система здравоохранения РФ? Для Зимбабве? Ты тупой? хохлы",
            "target": 1
        },
        {
            "features": "Привет, у меня все нормально, как дела у тебя? Cлышал ты недавно купил маме новый дом?",
            "target": 0
        },
        {
            "features": "Сегодян просто потрясающий день для пробежки",
            "target": 0
        }
    ]

    for example in examples:
        resp = requests.post(
            "http://127.0.0.1:80/predict",
            json={"comment": example["features"]}
        )
        predictions = resp.json()["toxic"]
        print(f"Features: {example['features']}")
        print(f"Predicted label: {predictions}")
        print(f"Expected label: {example['target']}")
        print("----")