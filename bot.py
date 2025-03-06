import os

def load_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def simulate_response(user_input):
    user_input_lower = user_input.lower()
    if "привет" in user_input_lower or "здравствуйте" in user_input_lower:
        return "Добрый день! Меня зовут AI-Менеджер, я готов помочь вам с выбором бурового оборудования."
    elif "технические характеристики" in user_input_lower or "характеристики" in user_input_lower:
        return ("Модель X100 имеет максимальную глубину бурения 3000 метров, систему автоматического контроля процесса "
                "и энергоэффективность до 95%.")
    elif "цена" in user_input_lower:
        return ("Стоимость модели X100 оправдана высоким качеством материалов и передовыми технологиями. "
                "Мы также предлагаем гибкие условия оплаты.")
    elif "доставка" in user_input_lower or "гарантия" in user_input_lower:
        return ("Мы осуществляем доставку по всему миру и предоставляем гарантийный срок в 24 месяца с полным сервисным обслуживанием.")
    elif "заказать" in user_input_lower or "оформить" in user_input_lower:
        return ("Для оформления заказа, пожалуйста, оставьте ваши контактные данные, и наш специалист свяжется с вами в ближайшее время.")
    else:
        return "Можете уточнить ваш вопрос? Я постараюсь предоставить всю необходимую информацию."

def main():
    system_prompt = load_file('prompts/system_prompt.md')
    info_base = load_file('prompts/information_base.md')
    dialogue_examples = load_file('prompts/dialogue_examples.md')
    test_scenarios = load_file('prompts/test_scenarios.md')
    
    print("AI-Менеджер по продажам бурового оборудования")
    print("Введите 'выход' для завершения работы.\n")
    
    while True:
        user_input = input("Клиент: ")
        if user_input.lower() in ['выход', 'exit']:
            print("AI-Менеджер: Спасибо за обращение, до свидания!")
            break
        response = simulate_response(user_input)
        print("AI-Менеджер:", response)


if __name__ == "__main__":
    main()
