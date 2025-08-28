import os
import pandas as pd


class Inspector:

    def __init__(self, source_location, anticipated_fields=None, anticipated_types=None):
        self.source_location = source_location
        self.anticipated_fields = anticipated_fields
        self.anticipated_types = anticipated_types or {}

    def inspect(self):
        try:
            self._verify_source_presence()
            dataset = self._import_table()
            self._verify_non_blank(dataset)

            if self.anticipated_fields is not None:
                self._verify_fields(dataset)

            if self.anticipated_types:
                self._verify_types(dataset)

            print("Проверка таблицы завершена успешно.")
            return dataset

        except Exception as error:
            print(f"Возникла следующая ошибка: {error}")
            raise

    def _verify_source_presence(self):
        if not os.path.exists(self.source_location):
            raise FileNotFoundError(f"Файл не найден: '{self.source_location}'")

    def _import_table(self):
        try:
            if self.source_location.endswith('.csv'):
                dataset = pd.read_csv(self.source_location)
                
                # Дополнительная проверка на пустой CSV
                if dataset.empty and os.path.getsize(self.source_location) == 0:
                    raise ValueError("Таблица пуста.")
                
                return dataset
            else:
                raise ValueError("Неподдерживаемый формат файла. Используйте CSV файл.")
                
        except pd.errors.EmptyDataError:
            raise ValueError("Таблица пуста.")
        except Exception as error:
            raise ValueError(f"Ошибка при чтении файла: {error}")

    def _verify_non_blank(self, dataset):
        if dataset.empty:
            raise ValueError("Таблица пуста")

    def _verify_fields(self, dataset):
        absent_fields = [field for field in self.anticipated_fields 
                          if field not in dataset.columns]
        additional_fields = [field for field in dataset.columns 
                        if field not in self.anticipated_fields]

        if absent_fields or additional_fields:
            error_message = (
                "Структура таблицы НЕ совпадает с ожидаемой:\n"
                f"- Названия полей не совпадают.\n"
                f"  Ожидаемые: {self.anticipated_fields}\n"
                f"  Фактические: {list(dataset.columns)}"
            )
            raise ValueError(error_message)

    def _verify_types(self, dataset):
        issues = []
        
        for field, expected_type in self.anticipated_types.items():
            if field not in dataset.columns:
                continue

            actual_type = dataset[field].dtype
            
            if actual_type != expected_type:
                issues.append(
                    f"- В поле '{field}' тип данных не соответствует ожидаемому.\n"
                    f"  Ожидается: {expected_type}, фактически: {actual_type}"
                )