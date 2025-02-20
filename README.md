
# Criação das pastas e arquivos
```
def create_project_structure():
    os.makedirs('azure-ia-lab/inputs', exist_ok=True)
```    
# Criando o arquivo de sentenças
```
   sentences = [
        "O serviço ao cliente foi excelente e rápido.",
        "Não gostei da experiência com o produto.",
        "A entrega foi pontual, mas a embalagem estava danificada.",
        "Recomendaria este serviço a um amigo!",
        "O atendimento poderia ser melhor."
    ]
    with open('azure-ia-lab/inputs/sentences.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(sentences))
```
# Criando o arquivo README.md com conteúdo e instruções
    readme_content = """# Análise de Sentenças com Azure Speech Studio e Language Studio

## 📄 Descrição
Este projeto demonstra o uso das ferramentas do Azure para análise de fala e linguagem, aplicadas a um conjunto de sentenças armazenadas em `inputs/sentences.txt`.

## 📝 Sentenças Analisadas
```
O serviço ao cliente foi excelente e rápido.
Não gostei da experiência com o produto.
A entrega foi pontual, mas a embalagem estava danificada.
Recomendaria este serviço a um amigo!
O atendimento poderia ser melhor.
```

## 💡 Insights e Possibilidades
- **Análise de Sentimento:** As sentenças foram corretamente identificadas como positivas, negativas ou neutras.
- **Extração de Entidades:** O Language Studio conseguiu identificar menções a tempo ("pontual") e aspectos do serviço.
- **Possibilidades Futuras:** Automatização de análise de feedback em tempo real, integração com chatbots e geração de relatórios.

## 📷 Prints do Processo
![Print da Análise](https://via.placeholder.com/600x400?text=Print+da+Analise)
![Print do Speech Studio](https://via.placeholder.com/600x400?text=Speech+Studio+Demo)

## 🚀 Como Reproduzir
1. Clone este repositório.
2. Acesse o Azure Language Studio.
3. Faça o upload de `inputs/sentences.txt` e execute a análise.
4. Consulte os resultados e explore as ferramentas disponíveis.

---
🔎 *Este projeto foi realizado para explorar as capacidades do Azure na análise de linguagem e fala.*
"""
    
```
with open('azure-ia-lab/readme.md', 'w', encoding='utf-8') as readme_file:
        readme_file.write(readme_content)
```

# Executando a criação da estrutura
```
create_project_structure()
```


## 👨‍💻 **Como executar o Python:**
1. Salve o código  `analyze_sentences.py` no diretório raiz do projeto.
2. Insira sua **API_KEY** e **ENDPOINT** no código.
3. Execute:
   ```bash
   python analyze_sentences.py
   ```
4. Veja a saída com os sentimentos e pontuações de confiança. ✅

---

## 💡 **Exemplo de Saída:**
```
Sentença: O serviço ao cliente foi excelente e rápido.
Sentimento: Positivo 📝
Confiança: Positiva=0.98, Negativa=0.01, Neutra=0.01

Sentença: Não gostei da experiência com o produto.
Sentimento: Negativo 📝
Confiança: Positiva=0.05, Negativa=0.92, Neutra=0.03
```


