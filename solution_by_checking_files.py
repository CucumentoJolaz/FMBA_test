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
        """Создание имени метаинформации для файла у которого есть метаинформация"""
        return ".".join([filename.split(".")[0], metafile_ext])

    def meta_exists(self, filename: str, filelist: str) -> bool:
        """Проверка существования мета информации у файла"""
        lower_filearr = [file.lower() for file in filelist]
        meta_name = self.meta_name_create(filename)
        if meta_name.lower() in lower_filearr and not filename.endswith(f".{metafile_ext}"):
            return True

    def meta_pair(self, filename:str) -> list:
        """Проверка есть ли у файла метаинформация"""
        meta_name = self.meta_name_create(filename)
        return [filename, meta_name]
        

    def meta_dict(self, only_folders_names = True) -> dict:
        """Генерация словаря "папка": ["имя файла","его мета"]. если флаг onle_folders_names==False то в качестве ключа указывается полный путь к папке"""
        meta_dict_out = {}
        if only_folders_names:
            for folder, files in self.folders_files_dict.items():
                key = folder.split(os.sep)[-1]
                meta_dict_out[key] = []
                for file in files:
                    if self.meta_exists(file, files):
                        meta_dict_out[key].append(self.meta_pair(file))
        else:
            for folder, files in self.folders_files_dict.items():
                meta_dict_out[folder] = []
                for file in files:
                    if self.meta_exists(file, files):
                        meta_dict_out[folder].append(self.meta_pair(file))

                    
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
