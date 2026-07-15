import gradio as gr

from inference import predict_hallucination


def detect_hallucination(
        question,
        response,
        category,
        response_type,
        model_name
):


    prediction, confidence = predict_hallucination(

        question=question,

        response=response,

        category=category,

        response_type=response_type,

        model_name=model_name

    )


    return (
        f"Prediction: {prediction}",
        f"Confidence: {confidence}%"
    )



with gr.Blocks() as app:


    gr.Markdown(
        """
        # FactCheck AI - Hallucination Detection System

        This application predicts whether an LLM-generated
        response is likely to be hallucinated using a trained
        machine learning classifier.
        """
    )

    #selecting input

    question = gr.Textbox(
        label="Question",
        placeholder="Enter the user question"
    )


    response = gr.Textbox(
        label="LLM Generated Response",
        placeholder="Enter the generated answer",
        lines=5
    )


    category = gr.Dropdown(
    choices=[
        "Misconceptions",
        "Science",
        "Misquotations",
        "Conspiracies",
        "Superstitions",
        "Fiction",
        "Myths and Fairytales",
        "Indexical Error: Identity",
        "Indexical Error: Other",
        "Indexical Error: Time",
        "Indexical Error: Location",
        "Distraction",
        "Subjective",
        "Religion",
        "Logical Falsehood",
        "Stereotypes",
        "Paranormal",
        "Nutrition",
        "Proverbs",
        "Health",
        "Psychology",
        "Sociology",
        "Economics",
        "Politics",
        "Law",
        "Language",
        "Confusion: People",
        "Confusion: Places",
        "Confusion: Other",
        "Finance",
        "Science",
        "Weather",
        "Misinformation",
        "Statistics",
        "History",
        "Mandela Effect",
        "Advertising",
        "Misconceptions: Topical",
        "Education"
    ],
    label="Category"
)


    response_type = gr.Dropdown(
        choices=[
            "Adversarial",
            "Non-Adversarial"
        ],
        label="Type"
    )


    model_name = gr.Dropdown(
    choices=[
        "OpenAI",
        "Groq",
        "DeepSeek"
    ],
    label="Model"
)

#selecting output
    
    prediction_output = gr.Textbox(
        label="Prediction"
    )


    confidence_output = gr.Textbox(
        label="Confidence"
    )

#button logic
    
    button = gr.Button(
        "Detect Hallucination"
    )


    button.click(

        fn=detect_hallucination,

        inputs=[
            question,
            response,
            category,
            response_type,
            model_name
        ],

        outputs=[
            prediction_output,
            confidence_output
        ]

    )

if __name__ == "__main__":

    app.launch()
