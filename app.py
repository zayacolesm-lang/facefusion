import gradio as gr
from facefusion import core  # presupunând că în facefusion.py e logica principală

def run_facefusion(image_path: str):
    # Aici trebuie să apelezi funcția ta reală de procesare
    # Exemplu: return core.face_swap(image_path)
    return "Procesare în curs..."  # Test temporar

gr.Interface(
    fn=run_facefusion,
    inputs=gr.Textbox(label="Path imagine"),
    outputs="text",
    title="FaceFusion 3.0"
).launch(server_name="0.0.0.0", server_port=7860)
