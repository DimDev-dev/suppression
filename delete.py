import os
import hashlib

directory = input("dans quelle dossier vos doublon?")

unique_files = []

files = os.listdir(directory)
if not os.path.isdir(directory):
  print("Le répertoire spécifié n'existe pas")
  exit()

for file in files:
    file_path = os.path.join(directory, file)

    file_path = os.path.join(directory, file)
    with open(file_path, 'rb') as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()

    if file_hash not in unique_files:
        unique_files.append(file_hash)
    else:
        os.remove(file_path)
