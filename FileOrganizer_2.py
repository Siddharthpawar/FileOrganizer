import os, shutil
from tkinter import *
from tkinter import filedialog

files = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],
    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],
    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],
    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],
    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],
    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],
    "PLAINTEXT": [".txt", ".in", ".out"],
    "PDF": [".pdf"],
    "PYTHON": [".py"],
    "XML": [".xml"],
    "EXE": [".exe"],
    "SHELL": [".sh"]

}
'''files = {
    'Videos': ['.mp4'],
    'Audios': ['.wav', '.mp3'],
    'Images': ['.jpg', '.png'],
    'Documents': ['.doc', '.docx', '.xlsx', '.xls', '.pdf', '.zip', '.rar']
}'''
other_folder = 'OTHERS'

def arrange_file(file):
    main_directory = 'E:\\\python\\pycharm\\test_organize'
    extension = '.' + file.split('.')[-1]
    find = False
    for folder_name in files:
        if extension in files[folder_name]:
            if folder_name not in os.listdir(main_directory):
                os.mkdir(os.path.join(main_directory, folder_name))
            print('Moving', os.path.join(main_directory, file) + '------>' + os.path.join(main_directory, folder_name))
            shutil.move(os.path.join(main_directory, file), os.path.join(main_directory, folder_name))
            find = True
            break
    if not find:
        if other_folder not in os.listdir(main_directory):
            os.mkdir(os.path.join(main_directory, other_folder))
        print('Moving', os.path.join(main_directory, file) + '------>' + os.path.join(main_directory, other_folder))
        shutil.move(os.path.join(main_directory, file), os.path.join(main_directory, other_folder))

def check_folder(directory):
    all_files = os.listdir(directory)
    for file in all_files:
        # print(file, os.listdir(main_directory))
        # print(file not in main_directory)
        main_directory = 'E:\\python\\pycharm\\test_organize'
        if os.path.isfile(os.path.join(directory, file)) and (file not in os.listdir(main_directory)):
            #shutil.move(os.path.join(directory, file), main_directory)
            shutil.copy(os.path.join(directory, file), 'E:\\python\\pycharm\\test_organize')
        elif not os.path.isfile(os.path.join(directory, file)):
            check_folder(os.path.join(directory, file))
            #os.rmdir(os.path.join(directory, file))

def organize(a):
    global main_directory
    main_directory = a
    #main_directory = 'E:\python\pycharm\test_organize'
    print('Checking folders....')
    check_folder(main_directory)

    main_directory = 'E:\\python\\pycharm\\test_organize'
    #all_files = os.listdir(main_directory)
    all_files = os.listdir('E:\\python\\pycharm\\test_organize')
    for file in all_files:
        if os.path.isfile(os.path.join(main_directory, file)):
            arrange_file(file)

def browsefunc():
    filename = filedialog.askdirectory()
    print(filename)
    #pathlabel.config(text=filename)
    organize(filename)


root = Tk()
browsebutton = Button(root, text="Browse", command=browsefunc)
browsebutton.pack()
root.mainloop()
