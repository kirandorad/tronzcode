import tkinter as tk
from tkinter import scrolledtext, messagebox
import openai

# Function to generate AI code using GPT-3.5
def generate_code(input_code):
    # Replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key
    openai.api_key = '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'
    
    # Parameters for generating code
    temperature = 0.7
    max_tokens = 500
    
    try:
        # Generating code using GPT-3.5
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=input_code,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        # Extracting the generated code from the response
        generated_code = response.choices[0].text.strip()
        return generated_code
    except Exception as e:
        # Error handling in case of API issues
        messagebox.showerror("Error", str(e))
        return None

# Function to handle the button click event
def generate_button_click():
    input_code = input_text.get("1.0", tk.END)
    generated_code = generate_code(input_code)
    if generated_code is not None:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, generated_code)

# Create the main application window
app = tk.Tk()
app.title("AI Code Generator")

# Create input text box
input_text = scrolledtext.ScrolledText(app, width=100, height=15, wrap=tk.WORD)
input_text.grid(row=0, column=0, padx=10, pady=10)

# Create output text box
output_text = scrolledtext.ScrolledText(app, width=100, height=15, wrap=tk.WORD)
output_text.grid(row=1, column=0, padx=10, pady=10)

# Create generate button
generate_button = tk.Button(app, text="Generate Code", command=generate_button_click)
generate_button.grid(row=2, column=0, padx=10, pady=10)

# Start the main event loop
app.mainloop()
