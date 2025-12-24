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

## ⏰ Método 2: Executar automaticamente com o Agendador de Tarefas do Windows

Você pode configurar o script para rodar automaticamente sempre que o computador for iniciado:

### 🛠️ Passo a passo

1. Abra o **Agendador de Tarefas** do Windows.
2. Clique em **Criar Tarefa**.
3. Vá até a aba **Disparadores (Triggers)**:
   - Clique em **Novo**.
   - Selecione **Ao iniciar** (At startup).
4. Vá até a aba **Ações (Actions)**:
   - Clique em **Novo**.
   - Em **Programa/script**, insira o caminho do executável do Python.  
     Exemplo:
     ```
     C:\Users\SeuUsuario\AppData\Local\Programs\Python\Python312\python.exe
     ```
   - Em **Adicionar argumentos**, insira o caminho completo do seu script.  
     Exemplo:
     ```
     C:\Users\SeuUsuario\Desktop\organizer\main.py
     ```
5. Clique em **OK** para salvar a tarefa.

