import os


def delete_files_with_keyword_in_name(directory_path, keyword):
    if not os.path.isdir(directory_path):
        print(f"{directory_path} не является директорией или не существует.")
        return

    try:
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                if keyword in file_name:
                    file_path = os.path.join(root, file_name)
                    try:
                        os.remove(file_path)
                        print(f"Файл {file_path} удалён, так как его имя содержит ключевое слово '{keyword}'.")
                    except Exception as e:
                        print(f"Ошибка при удалении файла {file_path}: {e}")
                else:
                    print(f"Файл {file_name} не содержит ключевое слово '{keyword}' в имени.")
    except Exception as e:
        print(f"Ошибка при обработке директории {directory_path}: {e}")


directory_to_check = "./media"
key_word = input("Keyword: ")

delete_files_with_keyword_in_name(directory_to_check, key_word)
