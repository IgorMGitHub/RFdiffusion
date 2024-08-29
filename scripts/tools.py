import os
def clear_folder(dir):
    if os.path.exists(dir):
        for the_file in os.listdir(dir):
            file_path = os.path.join(dir, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                else:
                    clear_folder(file_path)
                    os.rmdir(file_path)
            except Exception as e:
                print(e)
pass

def backup_folder(folder):
    folder_old = folder+'_old'
    if os.path.isdir(folder):
        # print('Backup output directory ...')
        try:
            if os.path.isdir(folder_old):
                clear_folder(folder_old)
            os.rename(folder,folder_old)
        except Exception as e:
            print(e)
pass
