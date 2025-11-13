"""
Projeto de Speech Recognition - Transcrição de Áudio em Tempo Real
"""

import os
import sys

import speech_recognition as sr

if sys.platform == "win32":
    os.system("chcp 65001 > nul 2>&1")
    sys.stdout.reconfigure(encoding="utf-8") if hasattr(
        sys.stdout, "reconfigure"
    ) else None


def transcrever_audio():
    r = sr.Recognizer()

    try:
        mic_list = sr.Microphone.list_microphone_names()
        if not mic_list:
            print("ERRO: Nenhum microfone encontrado!")
            print("Por favor, verifique se o microfone está conectado e funcionando.")
            return

        print(f"Microfone detectado: {mic_list[0]}")
        with sr.Microphone() as source:
            print("Ajustando ruido ambiente... Por favor, aguarde.")
            r.adjust_for_ambient_noise(source, duration=1)
            print("Microfone pronto! Pode falar...")
            print("-" * 50)

            try:
                while True:
                    print("\nEscutando...")
                    try:
                        audio = r.listen(source, timeout=5, phrase_time_limit=10)
                    except sr.WaitTimeoutError:
                        print("Tempo de espera esgotado. Tente falar novamente.")
                        continue

                    print("Processando...")

                    try:
                        texto = r.recognize_google(audio, language="pt-BR")
                        print(f"\n[OK] Voce disse: {texto}")
                        print("-" * 50)

                    except sr.UnknownValueError:
                        print("[ERRO] Nao foi possivel entender o audio")
                        print("-" * 50)

                    except sr.RequestError as e:
                        print(f"[ERRO] Erro ao processar: {e}")
                        print("Verifique sua conexao com a internet.")
                        print("-" * 50)

            except KeyboardInterrupt:
                print("\n\nPrograma encerrado pelo usuario.")
                sys.exit(0)

    except OSError as e:
        print(f"ERRO: Problema ao acessar o microfone: {e}")
        print("Por favor, verifique se o microfone esta conectado e funcionando.")
        sys.exit(1)
    except Exception as e:
        print(f"ERRO inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    print("=" * 50)
    print("  PROJETO DE SPEECH RECOGNITION")
    print("  Transcricao de Audio em Tempo Real")
    print("=" * 50)
    print("\nPressione Ctrl+C para sair\n")

    transcrever_audio()
