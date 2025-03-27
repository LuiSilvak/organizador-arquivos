# Organizador de Arquivos da Área de Trabalho

Este script Python organiza automaticamente os arquivos da sua área de trabalho, movendo-os para pastas específicas com base em suas extensões.

## Funcionalidades

- Organiza arquivos da área de trabalho em pastas específicas: **Documentos**, **Imagens**, **Músicas**, **Vídeos**, **Outros**.
- Cria as pastas automaticamente, caso elas não existam.
- Mover arquivos de acordo com sua extensão, como `.pdf`, `.docx`, `.jpg`, `.mp3`, etc.

## Requisitos

- **Python 3.6 ou superior**.

## Instalação

1. Clone o repositório ou baixe os arquivos.
2. Certifique-se de que o Python 3.6 ou superior esteja instalado em seu sistema.

## Uso

1. Coloque o script `organizador.py` na sua área de trabalho.
2. Execute o script:

```bash
python organizador.py
```

3. O script irá organizar os arquivos da sua área de trabalho, movendo-os para as pastas correspondentes.

## Gerar Executável

Para criar um **executável** para Windows, use o **PyInstaller**:

1. Instale o PyInstaller:

```bash
pip install pyinstaller
```

2. Crie o executável com o seguinte comando:

```bash
pyinstaller --onefile --windowed --icon=icone.ico organizador.py
```

3. O arquivo `.exe` será gerado na pasta `dist`.

## Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
