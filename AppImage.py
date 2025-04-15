import os

def create_desktop_file(name, appname, move_to_applications, language="en"):
    filename = f"{name}.desktop"
    current_directory = os.getcwd()
    filepath = os.path.join(current_directory, filename)
    
    with open(filepath, "w") as f:
        f.write("[Desktop Entry]\n")
        f.write("Encoding=UTF-8\n")
        f.write("Type=Application\n")
        f.write("Terminal=false\n")
        f.write(f"Exec={current_directory}/{name}.AppImage\n")
        f.write(f"Name={appname}\n")

    # Dosyayı çalıştırılabilir yap
    os.system(f"chmod +x \"{filepath}\"")

    if move_to_applications:
        target_path = os.path.expanduser("~/.local/share/applications/")
        os.makedirs(target_path, exist_ok=True)
        os.system(f"mv \"{filepath}\" \"{target_path}\"")

    print("✔️", "Dosya oluşturuldu ve taşındı!" if language == "tr" else "File created and moved!")

print("Welcome to .desktop Creator for AppImage!")
print("AppImage için .desktop dosyası oluşturucuya hoş geldiniz!")

try:
    lang = int(input("Select Language / Dil Seçin [1] Türkçe, [2] English: "))
except ValueError:
    print("Invalid input. Please enter 1 or 2.")
    exit()

if lang == 1:
    name = input("Dosya adı (uzantısız .AppImage): ").strip()
    appname = input("Program adı ne olarak gözüksün?: ").strip()
    huh = input("Dosya applications klasörüne taşınsın mı? (evet/hayır): ").strip().lower()
    move = huh == "evet"
    create_desktop_file(name, appname, move, language="tr")

elif lang == 2:
    name = input("File name (without .AppImage): ").strip()
    appname = input("How should the program name appear?: ").strip()
    huh = input("Move file to applications folder? (yes/no): ").strip().lower()
    move = huh == "yes"
    create_desktop_file(name, appname, move, language="en")

else:
    print("Invalid selection. Please choose 1 or 2.")
