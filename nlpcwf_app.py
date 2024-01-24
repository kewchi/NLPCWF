# -*- coding: utf-8 -*-
"""NLPCWF_app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jEhqaVaEV2fv3Lg06URTjWMQq-IpAg9y
"""

# Commented out IPython magic to ensure Python compatibility.

import streamlit as st
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

def load_model():
    # Load DistilBERT model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-cased-distilled-squad")
    model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-cased-distilled-squad", return_dict=True).half()

    # Question answering pipeline
    qa_pipe = pipeline("question-answering", model=model, tokenizer=tokenizer)
    return qa_pipe

qa_pipe = load_model()

# Streamlit app
def main():
    st.title("Red Panda Q&A")

    # User input
    context = st.text_area("Context", value="The red panda (Ailurus fulgens), also known as the lesser panda, is a small mammal native to the eastern Himalayas and southwestern China. It has dense reddish-brown fur with a black belly and legs, white-lined ears, a mostly white muzzle and a ringed tail. Its head-to-body length is 51–63.5 cm (20.1–25.0 in) with a 28–48.5 cm (11.0–19.1 in) tail, and it weighs between 3.2 and 15 kg (7.1 and 33.1 lb). It is well adapted to climbing due to its flexible joints and curved semi-retractile claws. The red panda inhabits coniferous forests as well as temperate broadleaf and mixed forests, favouring steep slopes with dense bamboo cover close to water sources. It is solitary and largely arboreal. It feeds mainly on bamboo shoots and leaves, but also on fruits and blossoms.")
    question = st.text_area("Question", value="What is the answer to...")

    # Answer button
    if st.button("Get Answer"):
        # If input is not empty
        if question.strip() != "" and context.strip() != "":
            
            # Get the answer using the pipeline
            answer = qa_pipe(question=question, context=context)

            # Display the answer
            st.markdown(f"Answer: {answer['answer']}")
            st.info(f"Confidence: {answer['score']}")

if __name__ == "__main__":
    main()


