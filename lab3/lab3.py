import os
print("Hello!")
while True:
    k=int(input("\n файл(1) или папка(2)?"))
    path=os.getcwd()
    if k==1:
        oldname=input("Name of your файл(с форматом)?")
        path=os.getcwd()+"\\"+oldname
        num=int(input("""
      Что ты хочешь сделать с этим файлом?
      1) Удалить файл
      2) Переименовать файл
      3) Добавить контент к этому файлу
      4) Перезаписать контент файла
      0) Показать родительские папки
    """))
        if num==1:
               os.remove(oldname)
               print("Готово!")
        
        elif num==2:
                newname=input("Как ты хочешь переименовать файл: ")
                os.rename(path,newname)
                print("Готово!")

        elif num==3:
                text=input("Вводи текст: ")
                file1=open(path,'a')
                file1.write(text)
                file1.close()
                print("Готово!")

        elif num==4:
            text=input("Вводи текст: ")
            file1=open(path,'w')
            file1.write(text)
            file1.close()
            print("Готово!")
        
        elif num==0:
            path=os.path.join(os.getcwd(),oldname)
            print("файл находится в папка папка папка")
            print(os.path.dirname(path))
    elif k==2:
        num=int(input("""
       Что ты хочешь сделать с этой папкой?
       1) Переименовать папку(которая лежит в этой директорий)
       2) Узнать сколько файлов в этой папке
       3) Узнать сколько папок в этой папке :-)
       4) Узнать содержимое папки
       5) Создать новый файл
       6) Создать новую папку в этой папке
    """))
        if num==1:
           oldname=input("Какую папку ты хочешь переименовать?")
           path=os.getcwd()+"\\"+oldname
           newname=input("Как ты хочешь переименовать папку: ")
           os.rename(path,newname)
           print("Готово!")

        elif num==2:
            num_files = len([f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))])
            print("У нас здесь "+str(num_files)+" файлов")
        elif num==3:
            dir_files = len([f for f in os.listdir(os.getcwd()) if os.path.isdir(os.path.join(os.getcwd(), f))])
            print("У нас здесь "+str(dir_files)+" папок")

        elif num==4:
            print("Это все файлы и папки: ")
            for i in range(len(os.listdir())):
                print(os.listdir()[i])
        

        elif num==5:
           text=input("Как ты хочешь его назвать? Пиши вместо с форматом: ")
           newfile=open(text,'w',encoding='utf-8')
           newfile.close()
           print("Готово!")

        elif num==6:
            text=input("""Как ты хочешь его назвать? 
Если хочешь создать папки в папке,
тогда между папками пиши \" \\\\ \": """)
            os.makedirs(text)
            print("Готово!")        