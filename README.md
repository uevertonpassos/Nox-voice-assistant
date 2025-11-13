# Projeto de Speech Recognition

Projeto em Python para transcrever áudio em tempo real usando a biblioteca SpeechRecognition.

## 📋 Requisitos

- Python 3.7 ou superior
- Microfone funcionando
- Conexão com internet (para usar Google Speech Recognition)

## 🚀 Instalação!

1. Clone ou baixe este projeto

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

**Nota para Windows:** Se tiver problemas ao instalar `pyaudio`, você pode precisar instalar usando:
```bash
pip install pipwin
pipwin install pyaudio
```

Ou baixar o wheel apropriado de: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

## 🎤 Como Usar

Execute o script principal:
```bash
python transcriber.py
```

O programa irá:
1. Ajustar o microfone para o ruído ambiente
2. Escutar o que você falar
3. Transcrever para texto em português brasileiro
4. Exibir o resultado na tela

Pressione `Ctrl+C` para sair.

## 📝 Funcionalidades

- ✅ Captura de áudio em tempo real do microfone
- ✅ Transcrição para texto usando Google Speech Recognition
- ✅ Suporte para português brasileiro (pt-BR)
- ✅ Tratamento de erros e mensagens informativas

## 🔧 Configurações

Você pode modificar o arquivo `transcriber.py` para:
- Alterar o idioma (mudar `language='pt-BR'` para outro idioma)
- Ajustar o tempo de escuta (`phrase_time_limit`)
- Usar outros serviços de reconhecimento (Sphinx, Azure, etc.)

## 📚 Bibliotecas Utilizadas

- **SpeechRecognition**: Biblioteca principal para reconhecimento de voz
- **PyAudio**: Para captura de áudio do microfone

## ⚠️ Observações

- É necessário conexão com internet para usar o Google Speech Recognition
- O microfone precisa estar funcionando corretamente
- Em ambientes muito ruidosos, a precisão pode diminuir

