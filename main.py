import openai
import random

# Ganti dengan API key Anda
api_key = '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'

# Inisialisasi klien OpenAI
openai.api_key = api_key

# Daftar beberapa prompt
prompts = [
    "Ceritakan saya tentang cuaca hari ini.",
    "Bagaimana perkembangan berita terkini?",
    "Beri saya rekomendasi buku yang bagus.",
    "Apakah Anda tahu fakta menarik?",
]

# Fungsi untuk mengirim permintaan ke model GPT-3.5 dengan prompt acak
def chat_with_model(prompts):
    prompt = random.choice(prompts)  # Memilih prompt secara acak
    response = openai.Chat.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=50,
        n=1,
        stop=None
    )
    
    return response.choices[0].text.strip()

# Contoh penggunaan
response = chat_with_model(prompts)
print(response)
