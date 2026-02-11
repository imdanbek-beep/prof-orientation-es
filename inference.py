from questions import QUESTIONS

def calculate_scores(answers_dict):
    scores = {'R': 0, 'I': 0, 'A': 0, 'S': 0, 'E': 0, 'C': 0}
    for i in range(len(QUESTIONS)):
        qkey = f'q{i+1}'
        if qkey in answers_dict:
            add = answers_dict[qkey]
            for cat in QUESTIONS[i]['cats']:
                scores[cat] += add
    return scores

RULES = [
    {
        "prof": "Аналитик данных / Data Scientist / Специалист по бизнес-аналитике",
        "cond": lambda s: s['I'] >= 12,
        "expl": "У вас заметный интерес к аналитике и работе с информацией (I)."
    },
    {
        "prof": "Программист / Тестировщик / Специалист по IT",
        "cond": lambda s: s['I'] >= 10 or s['R'] >= 10,
        "expl": "Есть интерес к технике, логике и созданию систем (I + R)."
    },
    {
        "prof": "Инженер / Технический специалист / Мастер на все руки",
        "cond": lambda s: s['R'] >= 10,
        "expl": "Вы имеете склонность к работе руками и техникой (R)."
    },
    {
        "prof": "Дизайнер / Художник / Контент-креатор / SMM",
        "cond": lambda s: s['A'] >= 12,
        "expl": "У вас есть творческий потенциал и интерес к созданию визуального контента (A)."
    },
    {
        "prof": "Психолог / Социальный работник / Консультант / Коуч",
        "cond": lambda s: s['S'] >= 12,
        "expl": "Вы склонны к работе с людьми, помощи, поддержке (S)."
    },
    {
        "prof": "Учитель / Тренер / Воспитатель / Инструктор",
        "cond": lambda s: s['S'] >= 10 or s['E'] >= 12,
        "expl": "Есть желание помогать, учить, развивать других (S + E)."
    },
    {
        "prof": "Маркетолог / Менеджер по продажам / PR / SMM-менеджер",
        "cond": lambda s: s['E'] >= 12,
        "expl": "У вас есть лидерские качества, предприимчивость, умение общаться и убеждать (E)."
    },
    {
        "prof": "Бухгалтер / Специалист по кадрам / Администратор / Офис-менеджер",
        "cond": lambda s: s['C'] >= 10,
        "expl": "Вы имеете склонность к порядку, документам, точности (C)."
    },
    {
        "prof": "HR-специалист / Рекрутер / Организатор мероприятий",
        "cond": lambda s: s['S'] >= 10 and s['E'] >= 10,
        "expl": "Работа с людьми + организаторские качества (S + E)."
    },
]

def get_recommendations(answers_dict):
    scores = calculate_scores(answers_dict)
    recs = []

    for rule in RULES:
        if rule["cond"](scores):
            explanation = rule["expl"]

            strong_points = []
            if scores['I'] >= 10: strong_points.append(f"аналитика / исследования ({scores['I']})")
            if scores['R'] >= 10: strong_points.append(f"техника / руки ({scores['R']})")
            if scores['A'] >= 10: strong_points.append(f"творчество / дизайн ({scores['A']})")
            if scores['S'] >= 10: strong_points.append(f"работа с людьми ({scores['S']})")
            if scores['E'] >= 10: strong_points.append(f"лидерство / инициатива ({scores['E']})")
            if scores['C'] >= 10: strong_points.append(f"порядок / точность ({scores['C']})")

            if strong_points:
                explanation += "\n\nСильные стороны: " + ", ".join(strong_points)

            recs.append({
                "name": rule["prof"],
                "explanation": explanation,
                "scores": scores
            })

    # Если ничего не нашлось (крайне маловероятно с такими низкими порогами)
    if not recs:
        recs.append({
            "name": "Ищи себя дальше — у тебя мягкий профиль",
            "explanation": "Ответы очень умеренные. Попробуй ответить более контрастно: 5 на то, что нравится, 1 на то, что не нравится.\n\nТвои баллы:\n"
                           f"R: {scores['R']}, I: {scores['I']}, A: {scores['A']}, S: {scores['S']}, E: {scores['E']}, C: {scores['C']}",
            "scores": scores
        })

    # Сортируем по максимальному баллу
    recs.sort(key=lambda x: max(x["scores"].values()), reverse=True)

    return recs[:3]