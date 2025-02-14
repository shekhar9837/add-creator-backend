from config import Config
import google.generativeai as genai

# Configure the Gemini API
genai.configure(api_key=Config.GEMINI_API_KEY)

async def generate_script(prompt: str) -> str:
    # Create model instance
    model = genai.GenerativeModel('gemini-1.5-pro')
    
    # Generate response
    response = model.generate_content(prompt)
    
    # Return the generated text
    return response.text