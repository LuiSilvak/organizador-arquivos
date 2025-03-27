import os
import shutil

# Caminho da área de trabalho (ajuste conforme necessário, dependendo do sistema operacional)
desktop_path = os.path.expanduser("~/Desktop")  # Para sistemas baseados em Unix (Linux/Mac)
# desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")  # Para sistemas Windows

# Definição de pastas de destino
folders = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Músicas": [".mp3", ".wav", ".flac"],
    "Vídeos": [".mp4", ".mkv", ".avi", ".mov"],
    "Outros": []  # Qualquer outro arquivo será movido para a pasta "Outros"
}

def organize_files():
    # Obter todos os arquivos na área de trabalho
    files = os.listdir(desktop_path)

    # Criar pastas de destino se não existirem
    for folder in folders.keys():
        folder_path = os.path.join(desktop_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Organizar arquivos
    for file in files:
        file_path = os.path.join(desktop_path, file)
        
        # Ignorar pastas e arquivos ocultos
        if os.path.isdir(file_path) or file.startswith('.'):
            continue
        
        # Verificar a extensão do arquivo
        file_extension = os.path.splitext(file)[1].lower()

        # Encontrar o tipo de pasta para o arquivo
        destination_folder = "Outros"  # Se não encontrar, será movido para "Outros"
        for folder, extensions in folders.items():
            if file_extension in extensions:
                destination_folder = folder
                break

        # Mover o arquivo para a pasta correta
        destination_path = os.path.join(desktop_path, destination_folder, file)
        shutil.move(file_path, destination_path)
        print(f"{file} foi movido para {destination_folder}")

if __name__ == "__main__":
    organize_files()
