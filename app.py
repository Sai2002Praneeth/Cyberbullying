import gradio as gr
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

# Load the saved vectorizer and model from the .pkl files
with open('vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

with open('model.pkl', 'rb') as f:
    classifier = pickle.load(f)

# Create the prediction function
def predict_comment(comment):
    transformed_comment = vectorizer.transform([comment])
    prediction = classifier.predict(transformed_comment)[0]

    if prediction == 0:
        return "Non-Bullying"
    else:
        return "Bullying"

# Create and launch the Gradio interface
iface = gr.Interface(
    fn=predict_comment,
    inputs=gr.Textbox(lines=2, placeholder="Enter a message here..."),
    outputs=gr.Label(),
    title="Cyberbullying Detector",
    description="Enter a message to see if it is bullying or not.",
    theme="soft"
)

iface.launch()