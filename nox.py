"""
Projeto de Speech Recognition - Transcrição de Áudio em Tempo Real
"""

import os
import sys
import threading
import speech_recognition as sr

if sys.platform == "win32":
    os.system("chcp 65001 > nul 2>&1")
    sys.stdout.reconfigure(encoding="utf-8") if hasattr(
        sys.stdout, "reconfigure"
    ) else None


class VoiceAssistant:
    def __init__(self, on_text_callback=None, on_status_callback=None):
        self.r = sr.Recognizer()
        self.is_running = False
        self.on_text_callback = on_text_callback
        self.on_status_callback = on_status_callback
        self.thread = None

    def _log(self, message):
        print(message)
        if self.on_status_callback:
            self.on_status_callback(message)

    def start(self):
        if self.is_running:
            return
        self.is_running = True
        self.thread = threading.Thread(target=self._listen_loop)
        self.thread.daemon = True
        self.thread.start()

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join(timeout=1)
            self.thread = None
        self._log("Parando assistente...")

    def _listen_loop(self):
        try:
            mic_list = sr.Microphone.list_microphone_names()
            if not mic_list:
                self._log("ERRO: Nenhum microfone encontrado!")
                self.is_running = False
                return

            self._log(f"Microfone detectado: {mic_list[0]}")
            with sr.Microphone() as source:
                self._log("Ajustando ruido ambiente... Aguarde.")
                self.r.adjust_for_ambient_noise(source, duration=1)
                self._log("Microfone pronto! Pode falar...")
                
                while self.is_running:
                    self._log("Escutando...")
                    try:
                        # Reduced timeout to allow checking self.is_running more often
                        audio = self.r.listen(source, timeout=2, phrase_time_limit=10)
                    except sr.WaitTimeoutError:
                        continue

                    if not self.is_running:
                        break

                    self._log("Processando...")

                    try:
                        texto = self.r.recognize_google(audio, language="pt-BR")
                        self._log(f"[OK] Voce disse: {texto}")
                        if self.on_text_callback:
                            self.on_text_callback(texto)

                    except sr.UnknownValueError:
                        self._log("[ERRO] Nao foi possivel entender o audio")

                    except sr.RequestError as e:
                        self._log(f"[ERRO] Erro ao processar: {e}")
                        
        except OSError as e:
            self._log(f"ERRO: Problema ao acessar o microfone: {e}")
            self.is_running = False
        except Exception as e:
            self._log(f"ERRO inesperado: {e}")
            self.is_running = False

def transcrever_audio():
    # Compatibility function for old usage
    assistant = VoiceAssistant()
    assistant.start()
    try:
        while True:
            import time
            time.sleep(0.1)
    except KeyboardInterrupt:
        assistant.stop()

if __name__ == "__main__":
    print("=" * 50)
    print("  PROJETO DE SPEECH RECOGNITION")
    print("  Transcricao de Audio em Tempo Real")
    print("=" * 50)
    print("\nPressione Ctrl+C para sair\n")

    transcrever_audio()
