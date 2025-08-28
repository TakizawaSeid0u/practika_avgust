from laba4 import data

if __name__ == "__main__":
    gg = data("var7.csv")
    
    if gg.validate_and_load():
        ~gg  
        gg.show_removed_count()
        
        gg.split_by_date()
    else:
        print("Не удалось загрузить данные. Проверьте ошибки выше.")