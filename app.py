import gradio as gr
import os 
import time 
import asyncio
from agent import PromptEngineer

async def engineer_prompt(input_prompt, api_key, temperature=0.0):
    if not api_key:
        return "Please provide an API key"
    
    try:
        enhancer = PromptEngineer(temperature=temperature, api_key=api_key)
        start_time = time.time()
        result = await enhancer.enhance_prompt(input_prompt, perform_eval=False)
        elapsed_time = time.time() - start_time

        return result["advanced_prompt"]
    except Exception as e:
        return f"Error: {str(e)}"

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
    # Prompt Engineer
    Transform your prompts into powerful, precise instructions using AI-driven optimization
    """)
    
    with gr.Row():
        with gr.Column(scale=1):
            api_key = gr.Textbox(
                label="API Key", 
                placeholder="sk-...", 
                type="password",
                info="Required: Enter your API key"
            )
            temperature = gr.Slider(
                minimum=0.0,
                maximum=1.0,
                value=0.0,
                step=0.1,
                label="Temperature",
                info="Recommended: Temperature=0.0"
            )
            
    with gr.Row():
        with gr.Column(scale=1):
            input_prompt = gr.Textbox(
                lines=10,
                placeholder="Enter your prompt here...",
                label="Input Prompt",
                info="Enter the prompt you want to engineer"
            )
            
        with gr.Column(scale=1):
            output_prompt = gr.Textbox(
                lines=20,
                label="Engineered Prompt",
                show_copy_button=True,
                autoscroll=False,
                info="Your engineered prompt will appear here"
            )
    
    submit_btn = gr.Button("Engineer Prompt", variant="primary")
    submit_btn.click(
        fn=engineer_prompt,
        inputs=[input_prompt, api_key, temperature],
        outputs=output_prompt
    )
    
    gr.Markdown("""
    ### Best Practices
    - Be specific and clear in your input prompt
    - Use temperature 0.0 for consistent, focused results
    - Increase temperature up to 1.0 for more creative variations
    - Review and iterate on engineered prompts for optimal results
    """)

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=True,
        show_error=True
    )
