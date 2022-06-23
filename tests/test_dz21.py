import unittest

# указываем пути к нашему тестируемому модулю
import sys, os
sys.path.append(os.path.abspath(os.path.pardir))
sys.path.append(os.path.abspath(os.path.curdir))

# тестируемый модуль
import dz21

#
# Глобальные переменные модуля
#

#
# Классы и процедуры модуля
#

class TestDZ21(unittest.TestCase):
    
    # инициализируем тестовое окружение
    @classmethod
    def setUpClass(cls):
        # задаем тестовые значения для списка документов
        cls.document = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}   
        cls.directories = {'1': ['2207 876234', '11-2', '5455 028765']}   
    # end setUpClass
    
    # тестируем функцию поиска человека по номеру документа
    def test_find_people(self):
        self.assertEqual(dz21.find_people(self.document.get('number')), self.document.get('name'))
    # end test_find_people
    
    # тестируем функцию поиска расположения документа
    def test_find_dir(self):
        self.assertEqual(dz21.find_dir(self.document.get('number')), list(self.directories.keys())[0])
    # end test_find_dir
    
    # тестируем функцию удаления документа
    # функция так названа т.к. исполнение тестов идет по алфавиту
    def test_xdel_document(self):
        # проверяем, что процесс удаления прошел без ошибок
        self.assertWarns(dz21.del_document(self.document.get('number')))
        # удаленные элементы не должны быть найдены ни на полках
        self.assertNotEqual(dz21.find_dir(self.document.get('number')), list(self.directories.keys())[0])
        # ни в списке документов
        self.assertNotEqual(dz21.find_people(self.document.get('number')), self.document.get('name'))
    # end test_del_document

    # тестируем функцию перемещения документа
    def test_mov_document(self):
        # проверяем, что процесс перемещения прошел без ошибок
        self.assertWarns(dz21.mov_document(self.document.get('number'), '3'))
        # проверяем, что перемещение на полку №3 прошло успешно
        self.assertEqual(dz21.find_dir(self.document.get('number')), '3')
    # end test_mov_document

# end class TestDZ21

#
# Основная программа модуля
#

if __name__ == '__main__':
    unittest.main()
    