import pandas as pd
import matplotlib.pyplot as plt
from laba3 import log  




class lol:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = self.load_data()

    @log
    def load_data(self):
        df = pd.read_csv(self.file_path)
        df['Date'] = pd.to_datetime(df['Date'])
        return df

    @log
    def plot_average_price(self):
        self.df['month'] = self.df['Date'].dt.to_period('M')
        df_filtered_monthly = self.df.groupby('month')['AveragePrice'].mean().reset_index()
        
        plt.figure(figsize=(12, 6))
        plt.plot(df_filtered_monthly['month'].dt.to_timestamp(), df_filtered_monthly['AveragePrice'])
        plt.title('Стоимость авокадо')
        plt.xlabel('Дата')
        plt.ylabel('Цена')
        plt.xticks(rotation=45)
        plt.grid()
        plt.tight_layout()
        plt.show()


plotter = lol('avocado (1).csv')
plotter.plot_average_price()