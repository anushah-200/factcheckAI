# deployment/app.py
import gradio as gr
from feature_extraction import extract_features
from inference import predict_hallucination, category_encoder, type_encoder, model_encoder

def check_fact(question, response, category, question_type, model_name):
    #extracting metadata and numerical features
    raw_features = extract_features(question, response, category, question_type, model_name)
    
    #making prediction
    prediction, confidence = predict_hallucination(raw_features)
    
    #output
    if prediction == 1:
        status = "Hallucination Detected"
        conf_str = f"{confidence * 100:.2f}% Probability of Hallucination"
    else:
        status = "Factual / Safe Response"
        conf_str = f"{(1 - confidence) * 100:.2f}% Probability of Factual Accuracy"
        
    metrics_summary = (
        f"###Summary of extracted features\n"
        f"- **Question Length:** {int(raw_features['QuestionLength'])} words\n"
        f"- **Response Length:** {int(raw_features['ResponseLength'])} words\n"
        f"- **Response Characters:** {int(raw_features['ResponseCharacters'])} characters\n"
        f"- **Average Word Length:** {raw_features['AverageWordLength']:.2f} characters per word"
    )
    
    return status, conf_str, metrics_summary

categories = list(category_encoder.classes_) if hasattr(category_encoder, 'classes_') else ["General"]
types = list(type_encoder.classes_) if hasattr(type_encoder, 'classes_') else ["factual", "adversarial"]
models = list(model_encoder.classes_) if hasattr(model_encoder, 'classes_') else ["OpenAI", "Groq", "DeepSeek"]

#Gradio UI
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🔍 FactCheck AI — Hallucination Detection Interface")
    gr.Markdown(
        "Input the question and the LLM's generated response below. "
        "The classical Random Forest model will evaluate the input metadata and linguistic patterns to detect potential hallucinations.")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### Input Fields")
            question_input = gr.Textbox(label="Question Prompt", placeholder="What was asked?", lines=3)
            response_input = gr.Textbox(label="LLM Response", placeholder="Paste the generated response to check...", lines=4)
            
            with gr.Row():
                category_dropdown = gr.Dropdown(label="Category", choices=categories, value=categories[0] if categories else None)
                type_dropdown = gr.Dropdown(label="Question Type", choices=types, value=types[0] if types else None)
                model_dropdown = gr.Dropdown(label="LLM Model Engine", choices=models, value=models[0] if models else None)
                
            submit_btn = gr.Button("Analyze Response Accuracy", variant="primary")
            
        with gr.Column():
            gr.Markdown("### Analysis Output")
            status_output = gr.Textbox(label="Model Decision", interactive=False)
            confidence_output = gr.Textbox(label="Confidence Score", interactive=False)
            metrics_output = gr.Markdown()

    # Link button click to logic
    submit_btn.click(
        fn=check_fact,
        inputs=[question_input, response_input, category_dropdown, type_dropdown, model_dropdown],
        outputs=[status_output, confidence_output, metrics_output]
    )

if __name__ == "__main__":
    demo.launch(share=False)
