import streamlit as st
import torch
import torch.nn as nn
from transformers import BertTokenizer,AutoModelForSequenceClassification
from components import plotClassDistribution,tokenizedText,apiYouTube

bertModel =AutoModelForSequenceClassification.from_pretrained(r"models\bertModel")
# tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
tokenizer = tokenizedText()

st.markdown("#### Youtube comment sentiments analysis 🏃‍♂️🏃‍♀️📹📺🎥📽️🎮")

def MainFrame():
    url = st.text_input(label = 'Enter a Youtube Video Complete URL')
    try:
        id_vid = url.split("=")[1]
        max_res = 'https://img.youtube.com/vi/'+id_vid+'/maxresdefault.jpg'
        st.image(max_res)
    except:
        pass
    api_call = apiYouTube()
    global data_store
    data_store = {"0":0,"1":0}
    try:
        api_output = api_call.findInputVideo(url)
        for text in api_output:
            # with col1:
                st.markdown("#### Comment")
                st.write(text)

                
            # with col2:
                st.markdown("#### Predicted Logits")
                output = bertModel(**tokenizer.generateToken(text))
                st.write(output.logits)
                st.write(torch.argmax(output.logits))


            # with col3:
                st.markdown("#### Predicted outcomes")
                if torch.argmax(output.logits):
                    st.write("The predicted output belongs to : Postive class")
                    data_store["1"] += 1

                else:
                    st.write("The predicted output belongs to : Negetive class")
                    data_store["0"] += 1

                st.write("-----------------------------------------------------------------------------------------")
               

    except:
        st.write("No URL provided")

def plotFrame():
    
    st.bar_chart(data_store)

if __name__ == "__main__":
    MainFrame()
    btn1 = st.button("Want to see visually ??")
    if btn1:
        plotFrame()
