from dotenv import load_dotenv
import openai
import os

load_dotenv()

def test_gpt_connection():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY is not set in the .env file.")
        return

    openai.api_key = api_key

    prompt = "Test GPT connection. Please respond with 'Connection successful.'"

    try:
        print("🔄 Sending request to GPT API...")
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.0
        )

        print("✅ Response from GPT API:")
        print(response['choices'][0]['message']['content'].strip())
    except Exception as e:
        print(f"❌ Error: Unable to connect to GPT API. {e}")


if __name__ == "__main__":
    print("🌐 Testing GPT API connection...")
    test_gpt_connection()
