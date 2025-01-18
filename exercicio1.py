import os

def organize_files():
    types = ['wmv', 'csv','jpg', 'pdf', 'png']

    # 1 - Diretório raiz 
    base_path = os.path.expanduser('~')

    # 2 - Navega no diretório Downloads
    path = os.path.join(base_path, 'downloads-teste')

    cwd = os.chdir(path)

    # 3 - Lista arquivos do diretório
    list_files = os.listdir(cwd)
    print(list_files)

    # 4 - Organizando arquivos
    for t in types:
        if t not in os.listdir():
            os.mkdir(t)
            
    for file in list_files:
        for t in types:
            if '.' + t in file:
                old_path = os.path.join(path, file)
                new_path = os.path.join(path, t, file)
                os.replace(old_path, new_path)

if __name__ == "__main__":
    organize_files()