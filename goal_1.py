import csv
import os

def get_real_path(abs_path: str, file_path: str)->str:
    mut_path = os.path.join(os.path.commonpath([abs_path, file_path]), "")
    real_path = abs_path.replace(mut_path, "")
    return real_path

def main(annotation_name: str, dataset_folder: str) -> None:



if __name__ == "__main__":
    main()