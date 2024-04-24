import streamlit as st
from sentence_transformers import SentenceTransformer
import chromadb
import preprocessing as prp

model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path= r"C:\Users\nishk\Desktop\Innomatics\Search_Engine_Project")
collection = client.get_collection("final_search_engine")

st.title("Subtitle Search Engine")

user_input = st.text_area("Enter your text: ", height=10)

st.button("Search")

# creating a fuction to test the model on custom user input
def match(user_input):
    data = user_input
    data = prp.normalization(data)
    data = prp.remove_punctuation(data)
    data = prp.remove_digit(data)
    data = prp.contraction_fixing(data)
    data = prp.accented_fixing(data)
    data = model.encode(data).tolist()

    results = collection.query(
    query_embeddings=[data],
    n_results=10
)
    return results['documents'][0]

if user_input:
    results = match(user_input)
    st.write(results)
    