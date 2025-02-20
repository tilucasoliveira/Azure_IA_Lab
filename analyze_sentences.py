from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# 🔑 Substitua com suas credenciais do Azure
API_KEY = "<SUA_CHAVE_AQUI>"
ENDPOINT = "<SEU_ENDPOINT_AQUI>"

# Função para autenticação no serviço Azure Language
def authenticate_client():
    return TextAnalyticsClient(endpoint=ENDPOINT, credential=AzureKeyCredential(API_KEY))

# Função para análise de sentimentos
def analyze_sentiment(client, documents):
    response = client.analyze_sentiment(documents=documents)
    
    for idx, doc in enumerate(response):
        print(f"Sentença: {documents[idx]}")
        if not doc.is_error:
            print(f"Sentimento: {doc.sentiment.capitalize()} 📝")
            print(f"Confiança: Positiva={doc.confidence_scores.positive:.2f}, Negativa={doc.confidence_scores.negative:.2f}, Neutra={doc.confidence_scores.neutral:.2f}\n")
        else:
            print(f"Erro: {doc.error.message}\n")

# 🔄 Lê as sentenças do arquivo e executa a análise
def main():
    with open('azure-ia-lab/inputs/sentences.txt', 'r', encoding='utf-8') as file:
        sentences = [line.strip() for line in file.readlines() if line.strip()]

    client = authenticate_client()
    analyze_sentiment(client, sentences)

if __name__ == "__main__":
    main()
