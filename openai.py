import openai

# Ganti dengan API key Anda
api_key = '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'

# Inisialisasi klien OpenAI
openai.api_key = api_key

# Fungsi untuk mengirim permintaan ke model GPT-3.5
def chat_with_model(prompts):
    responses = []
    
    for prompt in prompts:
        response = openai.Completion.create(
            engine="text-davinci-002",  # Gunakan engine yang sesuai
            prompt=prompt,
            max_tokens=50,  # Sesuaikan dengan panjang respons yang diinginkan
            n=1,  # Jumlah respons yang diinginkan
            stop=None  # Karakter untuk mengakhiri respons jika diperlukan
        )
        
        responses.append(response.choices[0].text.strip())
    
    return responses

# Contoh penggunaan dengan beberapa opsi prompt
user_prompts = [
    "Ceritakan saya tentang cuaca hari ini.",
    "Berikan saya rekomendasi buku yang bagus.",
    "Apa pendapat Anda tentang teknologi terbaru?"
]

responses = chat_with_model(user_prompts)

for i, response in enumerate(responses):
    print(f"Prompt {i + 1}: {response}")
