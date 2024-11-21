import openai

class GptHelper:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_rule(self, data):
        prompt = f"""
        Generate a Snort rule based on the following data:
        {data}
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert in Snort rule writing."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=200
            )
            rule = response['choices'][0]['message']['content'].strip()
            return rule
        except Exception as e:
            print(f"❌ Error generating rule: {e}")
            return None
