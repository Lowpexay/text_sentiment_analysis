import streamlit as st
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
 
def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']
    score = result['score']
    print(f"Label: {label}, Score: {score}") 
    if label == "5 stars":
        return "Muito Positivo"
    elif label == "4 stars":
        return "Positivo"
    elif label == "3 stars":
        return "Neutro"
    elif label == "2 stars":
        return "Negativo"
    elif label == "1 star":
        return "Muito Negativo"
    else:
        return "Neutro"

def analyse():
    st.title("Análise de Sentimentos")
    text = st.text_area("Digite o texto que deseja analisar:")
    if st.button("Analisar"):
        result = analyze_sentiment(text)
        st.write(f"Resultado: {result}")

if __name__ == "__main__":
    analyse()