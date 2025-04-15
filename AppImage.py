import os
print("Welcome to .desktop Creator For AppImage!")
lang = int(input("Which Language [1]Turkish, [2]English : "))
if lang == 1:
    name = str(input("Dosya Konumu(.AppImage olmadan"))
    appname = input("Program adı ne olarak gözüksün : ")
    huh = input("Dosya applications'a taşınsın mı?")
    filename = name+".desktop"
    ##Dosyayı executable yapma
    os.system("sudo chmod +x "+filename)
    current_directory = os.getcwd()
    with open(filename,"a"):
        print("dosya oluşturuldu")
    with open(filename, "w") as f:
        f.write("[Desktop Entry]\n")
        f.write("Encoding=UTF-8\n")
        f.write("Type=Application\n")
        f.write("Terminal=false\n")
        f.write("Exec="+current_directory+"/"+name+".AppImage\n")
        f.write("Name="+appname)
    if huh.upper() == "EVET":
        os.system("sudo mv "+filename+" ~/.local/share/applications/")
if lang == 2:
    name = str(input("File directory(without .AppImage): "))
    appname = input("What should the program name appear as: ")
    huh = input("Move file to applications folder? : ")
    filename = name+".desktop"
    ##Dosyayı executable yapma
    os.system("sudo chmod +x "+filename)
    current_directory = os.getcwd()
    with open(filename,"a"):
        print("File Created")
    with open(filename, "w") as f:
        f.write("[Desktop Entry]\n")
        f.write("Encoding=UTF-8\n")
        f.write("Type=Application\n")
        f.write("Terminal=false\n")
        f.write("Exec="+current_directory+"/"+name+".AppImage\n")
        f.write("Name="+appname)
    if huh.upper() == "YES":
        os.system("sudo mv "+filename+" ~/.local/share/applications/")
