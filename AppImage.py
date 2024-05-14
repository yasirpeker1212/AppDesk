import os
print("Welcome to .desktop Creator For AppImage!")
lang = int(input("Which Language [1]Turkish, [2]English : "))
if lang == 1:
    print("Dosyanızın Şuanki Konumunuzda olduğundan emin olun,ayrıca dosyanızın program olarak çalıştırılabildiğinden emin olun!")
    name = str(input("Dosya adı(.AppImage olmadan): "))
    appname = input("Program adı ne olarak gözüksün : ")
    huh = input("Dosya applications'a taşınsın mı?")
    filename = name+".desktop"
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
    if huh == "evet" or huh == "Evet":
        os.system("sudo mv "+filename+" ~/.local/share/applications/")
if lang == 2:
    print("Make sure your file is in your Current Location, and also make sure your file can be run as a program!")
    name = str(input("File name(without .AppImage): "))
    appname = input("What should the program name appear as: ")
    huh = input("Move file to applications folder? : ")
    filename = name+".desktop"
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
    if huh == "yes" or huh == "Yes":
        os.system("sudo mv "+filename+" ~/.local/share/applications/")
