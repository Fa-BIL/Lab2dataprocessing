import os

def get_next(class_mark: str, dataset_dir: str, num: int) -> str:

    #Функция возвращает следующий абсолютный путь в 'dataset_dir' с классом 'class_mark'.

    for subfolder in os.listdir(dataset_dir):
        if subfolder == class_mark:
            abs_subfolder = os.path.abspath(os.path.join(dataset_dir, subfolder))
            files = os.listdir(abs_subfolder)
            return os.path.join(abs_subfolder, files[num])
    return None