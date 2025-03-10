info_base = ("SELECT CONCAT(firstname, ',' ,lastname) FROM table",
              "SELECT firstname FROM table",
              "SELECT * FROM table")

def sql_info():
    sql_i = "SQL — декларативный язык программирования, применяемый для создания, модификации и управления данными в реляционной базе данных, управляемой соответствующей системой управления базами данных."
    return sql_i

def structura():
    structurs = '''
SELECT ('столбцы или * для выбора всех столбцов; обязательно')
FROM ('таблица; обязательно')
WHERE ('условие/фильтрация, например, city = 'Moscow'; необязательно')
GROUP BY ('столбец, по которому хотим сгруппировать данные; необязательно')
HAVING ('условие/фильтрация на уровне сгруппированных данных; необязательно')
ORDER BY ('столбец, по которому хотим отсортировать вывод; необязательно')
    '''
    return structurs

def testirov():
    func_test = '''
    Тестирование ПО - это проверка соответствия между реальным поведением программы и ее ожидаемым поведением.
    '''
    return func_test