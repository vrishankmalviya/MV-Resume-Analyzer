import gradio as gr
from app import analyze_resume



with gr.Blocks(theme=gr.themes.Soft()) as demo:

    gr.Markdown("## MV Resume Analyzer")

    with gr.Row():
        with gr.Column():
            resume_input = gr.File(label="📄 Upload Resume (PDF)")
            jd_input = gr.Textbox(label="📝 Job Description", lines=10)

            task_input = gr.Radio(
                choices=[
                    "Full Analysis",
                    "Match Score",
                    "Matching Skills",
                    "Missing Skills",
                    "Suggestions"
                ],
                label="Choose Analysis Type",
                value="Full Analysis"
            )

            custom_query = gr.Textbox(
                label="Optional Custom Query",
                placeholder="Ask anything..."
            )

            analyze_btn = gr.Button("🔍 Analyze", variant="primary")

        with gr.Column():
            output = gr.Markdown(
                value="## ⌛Waiting for the analysis....",
                label="📊 Result")
        analyze_btn.click(
            fn=analyze_resume,
            inputs=[resume_input, jd_input, task_input, custom_query],
            outputs=output
)

demo.launch(server_name="0.0.0.0",
            server_port=10000)




