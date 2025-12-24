# Organizer Bot 🗂️

Um script em Python que organiza automaticamente os arquivos da pasta **Downloads** em subpastas específicas de acordo com a extensão.

## 🚀 Como funciona
- Lê todos os arquivos da pasta `Downloads` do usuário.
- Identifica a extensão de cada arquivo (`.pdf`, `.docx`, `.jpg`, etc).
- Move o arquivo para a pasta correspondente:
  - PDFs → `Documents/PDFs`
  - Word → `Documents/WordDocs`
  - Excel → `Documents/ExcelSheets`
  - Imagens (`.jpg`, `.png`) → `Pictures/Images`
  - Vídeos (`.mp4`) → `Videos`
  - Músicas (`.mp3`) → `Music`

Se a pasta de destino não existir, o script cria automaticamente.

## 📦 Requisitos
- Python 3.10 ou superior
- Bibliotecas padrão (`os`, `shutil`)

## ▶️ Como usar
1. Clone ou copie este projeto para sua máquina.
2. Execute o script:
   ```bash
   python main.py
