import os
from openai import OpenAI

# Configure sua chave da OpenAI como variável de ambiente
os.environ["OPENAI_API_KEY"] = "sua_chave_aqui"  # substitua pela sua chave real

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Exemplo de transcrição (para teste)
transcription = "Olá, qual é a capital da França?"

# Chamada ao modelo GPT-4
response = client.chat.completions.create(
    model="gpt-4",
    messages=[{"role": "user", "content": transcription}]
)

chatgpt_response = response.choices[0].message.content
print(chatgpt_response)

# Modificação: salvar histórico
with open("historico_conversas.txt", "a", encoding="utf-8") as f:
    f.write(f"Pergunta: {transcription}\n")
    f.write(f"Resposta: {chatgpt_response}\n")
    f.write("*" * 40 + "\n")
