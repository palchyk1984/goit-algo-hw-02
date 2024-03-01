import queue
import uuid
import random

def generate_request(q, requests_dict):
    """Створює нову заявку, додає її до черги і записує в словник"""
    request_id = str(uuid.uuid4())
    print(f"Генеруємо нову заявку: {request_id}")
    q.put(request_id)
    requests_dict[request_id] = "очікує на обробку"

def process_request(q, requests_dict):
    """Видаляє заявку з черги, обробляє її і видаляє зі словника, показуючи кількість заявок у черзі"""
    if not q.empty():
        request_id = q.get()
        print(f"Обробляємо заявку: {request_id}. Залишилося заявок у черзі: {q.qsize()}")
        if request_id in requests_dict:
            del requests_dict[request_id]
    else:
        print("Черга пуста")

request_queue = queue.Queue()
requests_dict = {}

# Симуляція роботи програми з випадковістю
for _ in range(10):
    # Вирішуємо, чи генерувати нову заявку
    if random.random() < 0.7:  # 70% ймовірність генерації нової заявки
        generate_request(request_queue, requests_dict)
    
    # Вирішуємо, скільки заявок обробити
    requests_to_process = random.randint(0, 2)  # Від 0 до 2 заявок на ітерацію
    for _ in range(requests_to_process):
        process_request(request_queue, requests_dict)

# Обробка всіх залишених заявок в кінці
while not request_queue.empty():
    process_request(request_queue, requests_dict)

if len(requests_dict) == 0:
    print("Усі заявки оброблені, в словнику 0 заявок.")
else:
    print(f"В черзі залишилося {len(requests_dict)} заявок.")
