import gradio as gr
import onnxruntime as rt
from transformers import AutoTokenizer
import torch, json

tokenizer = AutoTokenizer.from_pretrained("distilroberta-base")
with open("label_types_encoded.json", "r") as fp:
    encode_genre_types = json.load(fp)

genres = list(encode_genre_types.keys())

# LOAD THE ONNX MODEL
inf_session = rt.InferenceSession("news-classifier-final-version.onnx")
input_name = inf_session.get_inputs()[0].name
output_name = inf_session.get_outputs()[0].name

def classify_news_category(description):
    inputs = tokenizer(
        description,
        truncation=True,
        max_length=512,
        return_tensors="np"
    )
    logits = inf_session.run(
        [output_name],
        {input_name: inputs["input_ids"]}
    )[0]
    probs = torch.sigmoid(torch.tensor(logits))[0]
    return dict(zip(genres, map(float, probs)))

# --- UPDATED INTERFACE ---
iface = gr.Interface(
    fn=classify_news_category,
    # Use gr.Textbox with lines=10 for a larger input area
    inputs=gr.Textbox(lines=10, placeholder="Paste your news article here...", label="Article Description"),
    outputs=gr.Label(num_top_classes=5),
    title="Multi-Label News Article Classifier"
)

# Use share=True (not sharable) to generate a public .gradio.live link
iface.launch(share=True)
