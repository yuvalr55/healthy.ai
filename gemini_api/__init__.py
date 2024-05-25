import google.generativeai as genai

API_KEY = 'AIzaSyAirR4zcoWk5XeUQdKcAqbfPpLxKywzUrM'


class GenaiApi:
    def __init__(self,):
        genai.configure(api_key=API_KEY)
        self._model = genai.GenerativeModel('gemini-pro')

    def get_response(self, text=''):
        return self._model.generate_content(text).text

