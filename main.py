from gemini_api import GenaiApi

genai_api = GenaiApi()
print(genai_api.get_response(text='Can you build me a menu for a diet cake with a lot of protein?'))