import os
import platform
if platform.system() =="Windows":
    labels_dir = 'c:\\tmp\\labels'
else:
    labels_dir = "/tmp/labels"

metafile_ext = "json"

class meta_class_configure():

    def __init__(self, init_folders_files: list):
        self.folders_files_dict = init_folders_files


    def meta_name_create(self, filename: str) -> str:
        """Создание имени метаинформации для файла"""
        return ".".join([filename.split(".")[0], metafile_ext])

    def meta_exists(self, filename: str, filelist: str) -> bool:
        """Проверка существования мета информации у файла"""
        lower_filearr = [file.lower() for file in filelist]
        meta_name = self.meta_name_create(filename)
        if meta_name.lower() in lower_filearr and not filename.lower().endswith(f".{metafile_ext}"):
            return True


    def meta_get(self, filename:str, filelist: str) -> list:
        """Возврат имени существующего метафайла"""
        meta_name_lowercase = self.meta_name_create(filename)
        for file in filelist:
            if meta_name_lowercase == file.lower():
                return file


    def meta_dict(self) -> dict:
        """Генерация словаря "папка": [["имя файла","его мета"]...]."""
        meta_dict_out = {}
        for folder, files in self.folders_files_dict.items():
            key = folder.split(os.sep)[-1]
            meta_dict_out[key] = []
            for file in files:
                if self.meta_exists(file, files):
                    if file:
                        meta_dict_out[key].append(
                        [
                        os.path.join(folder, file),
                        os.path.join(folder, self.meta_get(file, files))
                        ])

        #Новый словарь без пустых полей
        metadata_no_empty = {key: value for key, value in meta_dict_out.items() if value}

        return metadata_no_empty


def get_file_structure(folders_to_check: list) -> dict:
    """Получение словаря с файлами по переданному функции листу с именами папок."""
    labels = {}
    for label in folders_to_check:
        labels[label] = []
        for name in os.listdir(label):
            labels[label].append(name)

    return labels

if __name__ == "__main__":
    labels_list = ["label1", "label2", "label3", "label4"]
    path_list = [os.path.join(labels_dir, label) for label in labels_list]

    folders_files_dict = get_file_structure(path_list)

    meta_obj = meta_class_configure(folders_files_dict)
    meta_pairs_dict = meta_obj.meta_dict()


    for key, value in meta_pairs_dict.items():
        print(key, value)
