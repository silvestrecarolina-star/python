def main():
    # Pede o nome do ficheiro e converte para minúsculas
    file_name = input("File name: ").strip().lower()

    # Separa o nome pelos pontos
    parts = file_name.split('.')

    # Dicionário: extensão -> tipo MIME
    types = {
        "gif": "image/gif",
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip"
    }

    # Se houver mais de uma parte existe extensão
    if len(parts) > 1:
        ext = parts[-1]
        print(types.get(ext, "application/octet-stream"))
    else:
        print("application/octet-stream")

main()
