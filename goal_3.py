import csv
import os
import shutil
from random import sample

def main(dataset_dir: str, dir_for_copy: str, annotation_name: str) -> None:
    path_to_file = os.path.dirname(__file__)

    rand_int_list = sample(list(range(0, 10000)), 2000)
    rand_count = 0

    with open(annotation_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for subfolder in os.listdir(dataset_dir):
            for file in os.listdir(os.path.join(dataset_dir, subfolder)):
                orig_file = os.path.join(dataset_dir, subfolder, file)
                copy_file = os.path.join(dir_for_copy, str(rand_int_list[rand_count]))
                com_path = os.path.join(
                    os.path.commonpath([path_to_file, copy_file]), ""
                )
                rel_path = copy_file.replace(com_path, "")
                rand_count += 1
                shutil.copyfile(orig_file, copy_file)
                row = [orig_file, rel_path, subfolder]
                writer.writerow(row)

if __name__ == "__main__":
    main("C:\\Users\\MSI\\Desktop\\Programming\\Lab1webscraping\\dataset", "C:\\Users\\MSI\\Desktop\\Programming\\Lab2dataprocessing\\dataset_copy_3","annotations_3.csv")