#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Пользователь:
    def __init__(self, имя, пароль, возраст):
        self.имя = имя
        self.пароль = пароль
        self.возраст = возраст
        self.прогресс = {} # Словарь для хранения прогресса

    def добавить_прогресс(self, тема, значение):
        self.прогресс[тема] = значение

    def получить_прогресс(self, тема):
        return self.прогресс.get(тема)


# In[4]:


class Администратор:
    def __init__(self, имя, пароль):
        self.имя = имя
        self.пароль = пароль


# In[6]:


class Учебник:
    def __init__(self, название, содержание, уровень, раздел):
        self.название = название
        self.содержание = содержание
        self.уровень = уровень
        self.раздел = раздел


# In[8]:


class Видеолекция:
    def __init__(self, название, ссылка, уровень):
        self.название = название
        self.ссылка = ссылка
        self.уровень = уровень


# In[10]:


class Тест:
    def __init__(self, название, вопросы, уровень):
        self.название = название
        self.вопросы = вопросы
        self.уровень = уровень


# In[12]:


class Вопрос:
    def __init__(self, текст, варианты, правильныйОтвет):
        self.текст = текст
        self.варианты = варианты
        self.правильныйОтвет = правильныйОтвет


# In[14]:


class Вариант:
    def __init__(self, текст):
        self.текст = текст


# In[16]:


class Игра:
    def __init__(self, название, описание, уровень):
        self.название = название
        self.описание = описание
        self.уровень = уровень


# In[18]:


class Профиль:
    def __init__(self, пользователь, достижения):
        self.пользователь = пользователь
        self.достижения = достижения


# In[20]:


class Достижение:
    def __init__(self, название, описание):
        self.название = название
        self.описание = описание


# In[22]:


import unittest
from collections import namedtuple
# Тестовые данные в виде кортежей
ПользовательData = namedtuple('ПользовательData', ['имя', 'пароль', 'возраст'])
УчебникData = namedtuple('УчебникData', ['название', 'содержание', 'уровень', 'раздел'])
ВидеолекцияData = namedtuple('ВидеолекцияData', ['название', 'ссылка', 'уровень'])
ТестData = namedtuple('ТестData', ['название', 'уровень'])
ВопросData = namedtuple('ВопросData', ['текст', 'варианты', 'правильныйОтвет'])
ВариантData = namedtuple('ВариантData', ['текст'])
ИграData = namedtuple('ИграData', ['название', 'описание', 'уровень'])
ДостижениеData = namedtuple('ДостижениеData', ['название', 'описание'])

# Пример тестовых данных
test_users = [
    ПользовательData('Иван', '123', 18),
    ПользовательData('Мария', '456', 25)
]
test_учебники = [
    УчебникData('Экология для начинающих', 'Введение в экологические проблемы', 'Начальный', 'Введение'),
    УчебникData('Переработка отходов', 'Практические советы по переработке', 'Средний', 'Практика')
]
test_видеолекции = [
    ВидеолекцияData('Переработка отходов', 'https://www.youtube.com/watch?v=...', 'Средний'),
    ВидеолекцияData('Энергоэффективность', 'https://www.youtube.com/watch?v=...', 'Продвинутый')
]
test_тесты = [
    ТестData('Тест по экологии', 'Продвинутый'),
    ТестData('Тест по энергоэффективности', 'Средний')
]
test_вопросы = [
    ВопросData('Какой самый распространенный вид мусора?', [ВариантData('Пластик'), ВариантData('Бумага'), ВариантData('Стекло')], 0),
    ВопросData('Что такое энергоэффективность?', [ВариантData('Снижение потребления энергии'), ВариантData('Повышение выработки энергии'), ВариантData('Использование возобновляемых источников энергии')], 0)
]
test_игры = [
    ИграData('Сортировка мусора', 'Сортируй мусор по категориям', 'Начальный'),
    ИграData('Энергосберегающая викторина', 'Проверь свои знания об энергосбережении', 'Средний')
]
test_достижения = [
    ДостижениеData('Эко-новичок', 'Завершил(а) первый раздел учебника'),
    ДостижениеData('Эко-гуру', 'Прошел(а) все тесты на отлично')
]


# In[43]:


class Тесты(unittest.TestCase):
    def test_создание_пользователя(self):
        for user_data in test_users:
            пользователь = Пользователь(user_data.имя, user_data.пароль, user_data.возраст)
            self.assertEqual(пользователь.имя, user_data.имя)
            self.assertEqual(пользователь.пароль, user_data.пароль)
            self.assertEqual(пользователь.возраст, user_data.возраст)

    def test_добавление_прогресса_пользователя(self):
        пользователь = Пользователь('Иван', '123', 18)
        пользователь.добавить_прогресс('Учебник 1', 50)
        self.assertEqual(пользователь.получить_прогресс('Учебник 1'), 50)

    def test_создание_учебника(self):
        for учебник_data in test_учебники:
            учебник = Учебник(учебник_data.название, учебник_data.содержание, учебник_data.уровень, учебник_data.раздел)
            self.assertEqual(учебник.название, учебник_data.название)
            self.assertEqual(учебник.содержание, учебник_data.содержание)
            self.assertEqual(учебник.уровень, учебник_data.уровень)
            self.assertEqual(учебник.раздел, учебник_data.раздел)

    def test_создание_профиля(self):
        пользователь = Пользователь('Иван', '123', 18)
        достижения = [Достижение(d.название, d.описание) for d in test_достижения]
        профиль = Профиль(пользователь, достижения)
        self.assertEqual(профиль.пользователь.имя, 'Иван')
        self.assertEqual(len(профиль.достижения), len(test_достижения))

    def test_создание_достижения(self):
        for достижение_data in test_достижения:
            достижение = Достижение(достижение_data.название, достижение_data.описание)
            self.assertEqual(достижение.название, достижение_data.название)
            self.assertEqual(достижение.описание, достижение_data.описание)


# In[44]:


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[48]:


class Тесты(unittest.TestCase):
    def test_создание_пользователя(self):
        for user_data in test_users:
            пользователь = Пользователь(user_data.имя, user_data.пароль, user_data.возраст)
            self.assertEqual(пользователь.имя, user_data.имя)
            self.assertEqual(пользователь.пароль, user_data.пароль)
            self.assertEqual(пользователь.возраст, user_data.возраст)

    def test_добавление_прогресса_пользователя(self):
        пользователь = Пользователь('Иван', '123', 18)
        пользователь.добавить_прогресс('Учебник 1', 50)
        self.assertEqual(пользователь.получить_прогресс('Учебник 1'), 50)

    def test_создание_учебника(self):
        for учебник_data in test_учебники:
            учебник = Учебник(учебник_data.название, учебник_data.содержание, учебник_data.уровень, учебник_data.раздел)
            self.assertEqual(учебник.название, учебник_data.название)
            self.assertEqual(учебник.содержание, учебник_data.содержание)
            self.assertEqual(учебник.уровень, учебник_data.уровень)
            self.assertEqual(учебник.раздел, учебник_data.раздел)

    def test_создание_профиля(self):
        пользователь = Пользователь('Иван', '123', 18)
        достижения = [Достижение(d.название, d.описание) for d in test_достижения]
        профиль = Профиль(пользователь, достижения)
        self.assertEqual(профиль.пользователь.имя, 'Иван')
        self.assertEqual(len(профиль.достижения), len(test_достижения))

    def test_создание_достижения(self):
        for достижение_data in test_достижения:
            достижение = Достижение(достижение_data.название, достижение_data.описание)
            self.assertEqual(достижение.название, достижение_data.название)
            self.assertEqual(достижение.описание, достижение_data.описание)
            
    def test_создание_администратора(self):
        администратор = Администратор('Админ', 'admin123')
        self.assertEqual(администратор.имя, 'Админ')
        self.assertEqual(администратор.пароль, 'admin123')

    def test_создание_видеолекции(self):
        for видеолекция_data in test_видеолекции:
            видеолекция = Видеолекция(видеолекция_data.название, видеолекция_data.ссылка, видеолекция_data.уровень)
            self.assertEqual(видеолекция.название, видеолекция_data.название)
            self.assertEqual(видеолекция.ссылка, видеолекция_data.ссылка)
            self.assertEqual(видеолекция.уровень, видеолекция_data.уровень)

    def test_создание_теста(self):
        for тест_data in test_тесты:
            вопросы = [Вопрос(q.текст, [Вариант(v.текст) for v in q.варианты], q.правильныйОтвет) for q in test_вопросы]
            тест = Тест(тест_data.название, вопросы, тест_data.уровень)
            self.assertEqual(тест.название, тест_data.название)
            self.assertEqual(тест.уровень, тест_data.уровень)
            self.assertEqual(len(тест.вопросы), len(test_вопросы))

    def test_создание_вопроса(self):
        for вопрос_data in test_вопросы:
            вопрос = Вопрос(вопрос_data.текст, [Вариант(v.текст) for v in вопрос_data.варианты], вопрос_data.правильныйОтвет)
            self.assertEqual(вопрос.текст, вопрос_data.текст)
            self.assertEqual(len(вопрос.варианты), len(вопрос_data.варианты))
            self.assertEqual(вопрос.правильныйОтвет, вопрос_data.правильныйОтвет)

    def test_создание_игры(self):
        for игра_data in test_игры:
            игра = Игра(игра_data.название, игра_data.описание, игра_data.уровень)
            self.assertEqual(игра.название, игра_data.название)
            self.assertEqual(игра.описание, игра_data.описание)
            self.assertEqual(игра.уровень, игра_data.уровень)


# In[49]:


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[30]:


import cProfile

def run_code():
    # Пример кода для профилирования
    users = [Пользователь(u.имя, u.пароль, u.возраст) for u in test_users]
    for user in users:
        user.добавить_прогресс('Учебник 1', 50)
        user.добавить_прогресс('Учебник 2', 75)

cProfile.run('run_code()', 'profile_results')


# In[33]:


def test_создание_игры(self):
        for игра_data in test_игры:
            игра = Игра(игра_data.название, игра_data.описание, игра_data.уровень)
            self.assertEqual(игра.название, игра_data.название)
            self.assertEqual(игра.описание, игра_data.описание)
            self.assertEqual(игра.уровень, игра_data.уровень)

get_ipython().run_line_magic('prun', 'test_создание_игры(self)')


# In[35]:


import pstats
def run_code():
    # Пример кода для профилирования
    users = [Пользователь(u.имя, u.пароль, u.возраст) for u in test_users]
    for user in users:
        user.добавить_прогресс('Учебник 1', 50)
        user.добавить_прогресс('Учебник 2', 75)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 

    # Запуск профилирования
    profiler = cProfile.Profile()
    profiler.enable() # Включаем профилирование
    run_code()
    profiler.disable() # Выключаем профилирование

    # Анализ результатов профилирования
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative') # Сортировка по общему времени выполнения
    stats.print_stats(20) # Вывод 20 самых медленных функций

    # Дополнительные магические команды:
    stats.sort_stats('time') # Сортировка по среднему времени выполнения
    stats.print_stats(10) # Вывод 10 самых медленных функций

    stats.sort_stats('calls') # Сортировка по количеству вызовов
    stats.print_stats(5) # Вывод 5 функций, которые были вызваны чаще всего

    stats.sort_stats('cumulative').print_callers() # Вывод вызывающих функций 
    stats.sort_stats('cumulative').print_callees() # Вывод вызываемых функций 

    stats.dump_stats('profile_results.pstat') # Сохранение данных профилирования в файл
    stats = pstats.Stats('profile_results.pstat') # Загрузка данных профилирования из файла 
    stats.print_stats() # Вывод данных профилирования 


# In[51]:


import unittest
from collections import namedtuple
import cProfile
import pstats
import time
import tracemalloc # Импорт для анализа использования памяти
import psutil # Импорт для мониторинга использования процессора

def run_code():
    # Пример кода для профилирования
    users = [Пользователь(u.имя, u.пароль, u.возраст) for u in test_users]
    for user in users:
        user.добавить_прогресс('Учебник 1', 50)
        user.добавить_прогресс('Учебник 2', 75)

if __name__ == '__main__':
    # Запуск тестов
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 

    # Запуск профилирования
    profiler = cProfile.Profile()
    profiler.enable() # Включаем профилирование

    # Мониторинг использования памяти
    tracemalloc.start() # Начало отслеживания
    start_time = time.time() # Запоминаем начальное время
    run_code()
    end_time = time.time() # Запоминаем конечное время
    total_time = end_time - start_time # Вычисляем время выполнения

    # Анализ использования памяти
    snapshot = tracemalloc.take_snapshot() # Создание моментального снимка
    top_stats = snapshot.statistics('lineno') # Получение статистики по строкам кода
    print("[Память]")
    for stat in top_stats[:3]:
        print(stat)

    # Анализ использования процессора
    process = psutil.Process() # Получение информации о текущем процессе
    cpu_usage = process.cpu_percent() # Процент использования процессора

    # Анализ результатов профилирования
    profiler.disable() # Выключаем профилирование
    stats = pstats.Stats(profiler)
    stats.sort_stats('cumulative') # Сортировка по общему времени выполнения
    stats.print_stats(20) # Вывод 20 самых медленных функций

    # Вывод результатов
    print(f"\n[Время]: {total_time:.4f} сек.")
    print(f"[Процессор]: {cpu_usage}%")

   # Дополнительные магические команды:
    stats.sort_stats('time') # Сортировка по среднему времени выполнения
    stats.print_stats(10) # Вывод 10 самых медленных функций

    stats.sort_stats('calls') # Сортировка по количеству вызовов
    stats.print_stats(5) # Вывод 5 функций, которые были вызваны чаще всего

    stats.sort_stats('cumulative').print_callers() # Вывод вызывающих функций 
    stats.sort_stats('cumulative').print_callees() # Вывод вызываемых функций 

    stats.dump_stats('profile_results.pstat') # Сохранение данных профилирования в файл
    stats = pstats.Stats('profile_results.pstat') # Загрузка данных профилирования из файла 
    stats.print_stats() # Вывод данных профилирования 


# In[ ]:


'''class Пользователь:
    def __init__(self, имя, пароль, возраст):
        self.имя = имя
        self.пароль = пароль
        self.возраст = возраст
        self.прогресс = {} # Словарь для хранения прогресса

    def добавить_прогресс(self, тема, значение):
        self.прогресс[тема] = значение

    def получить_прогресс(self, тема):
        return self.прогресс.get(тема)'''

