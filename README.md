# 🎙️ Assistente de Voz Multi-Idiomas

Este projeto foi desenvolvido como parte de um desafio prático da DIO.  
Ele integra **Whisper (OpenAI)**, **ChatGPT (OpenAI)** e **gTTS (Google Text-to-Speech)** para criar um assistente de voz capaz de:

- 🌍 Transcrever áudio em diversos idiomas  
- 🧠 Compreender perguntas via ChatGPT  
- 🔊 Responder com voz sintetizada  

---

## 🚀 Como usar

### 1. Clone este repositório
```bash
git clone https://github.com/seuusuario/assistente-voz-multiidiomas.git
cd assistente-voz-multiidiomas
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure sua chave da OpenAI como variável de ambiente

#### Linux / Mac
```bash
export OPENAI_API_KEY="sua_chave_aqui"
```

#### Windows (PowerShell)
```powershell
setx OPENAI_API_KEY "sua_chave_aqui"
```

### 4. Execute o projeto
```bash
python app.py
```

---

## 🔧 Modificação implementada

- 📌 Adicionado histórico de conversas: todas as perguntas e respostas são salvas automaticamente em `historico_conversas.txt`.

---

## 📂 Estrutura do projeto

```bash
assistente-voz-multiidiomas/
│── app.py                     # Código principal
│── requirements.txt           # Dependências
│── README.md                  # Documentação
│── historico_conversas.txt    # Gerado automaticamente
```

---

## 📸 Demonstração

**Pergunta:** Olá, qual é a capital da França?  
**Resposta:** A capital da França é Paris.

```text
****************************************
```

---

## ⚠️ Observação importante

❌ Nunca compartilhe sua chave da OpenAI diretamente no código público.  
✅ Use variáveis de ambiente para manter o projeto seguro e profissional.
