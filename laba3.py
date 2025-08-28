from datetime import datetime
import pandas as pd
import os
import getpass


def log(function):
    def skibidi(*args, **kwargs):
        orig = function(*args, **kwargs)

        user_name = getpass.getuser()
        function_name = function.__name__
        formatted_date = datetime.now().strftime("%d-%m-%Y")
        formatted_time = datetime.now().time().strftime("%H:%M:%S")

        if os.path.isfile("logs.csv"):
            print("Файл существует")
            file_df = pd.read_csv("logs.csv")
            new_id = len(file_df)
            df = pd.DataFrame([[new_id, user_name, function_name, formatted_date, formatted_time]],
                              columns=['id', "user_name", 'function_name', 'formatted_date', 'formatted_time'])
            df.to_csv('logs.csv', mode='a', header=False, index=False)
        else:
            print("Файл не существует")
            df = pd.DataFrame([[0, user_name, function_name, formatted_date, formatted_time]],
                              columns=['id', "user_name", 'function_name', 'formatted_date', 'formatted_time'])
            df.to_csv('logs.csv', index=False)

        return orig
    return skibidi