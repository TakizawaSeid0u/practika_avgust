import laba5 as inspection

expected_columns = ["Участники гражданского оборота",
                    "Тип операции",
                    "Сумма операции",
                    "Вид расчета",
                    "Место оплаты",
                    "Терминал оплаты",
                    "Дата оплаты",
                    "Время оплаты",
                    "Результат операции",
                    "Cash-back",
                    "Сумма cash-back"]

validator = inspection.Inspector(
    source_location="var1.csv",  # Исправлено с file_path на source_location
    anticipated_fields=expected_columns  # Исправлено с expected_columns на anticipated_fields
)

try:
    df = validator.inspect()  # Исправлено с validate() на inspect()
    print("Чтение датафрейма успешно завершено")
    print(df.head())
except Exception as e:
    print(f"Программа завершена с ошибкой: {e}")