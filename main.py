from gpt_helper import GptHelper
from dotenv import load_dotenv
import os

load_dotenv()

class SnortHelper:
    def __init__(self, gpt_helper):
        self.gpt_helper = gpt_helper

    def save_rule(self, rule, sid):
        filename = f"{sid}.txt"
        try:
            with open(filename, 'w') as f:
                f.write(rule + '\n')
            print(f"\n✅ Rule successfully saved to **{filename}**\n")
        except Exception as e:
            print(f"❌ Error saving rule: {e}")

    def run(self):
        print("=" * 50)
        print("Welcome to Snort Helper with GPT!".center(50))
        print("=" * 50)

        while True:
            print("\n🔹 Enter Snort Rule Information:")
            try:
                data = input("Paste the data for rule generation:\n").strip()
                sid = input("  ➤ SID: ").strip()

                if not (data and sid.isdigit()):
                    print("\n❌ Invalid input. Please provide all required fields correctly.")
                    continue

                print("\n🔄 Generating Snort Rule with GPT...")
                rule = self.gpt_helper.generate_rule(data)

                if rule:
                    print("\n✨ Generated Snort Rule:")
                    print("=" * 50)
                    print(rule)
                    print("=" * 50)

                    save_option = input("\n💾 Do you want to save this rule? (y/n): ").strip().lower()
                    if save_option == 'y':
                        self.save_rule(rule, sid)
                    else:
                        print("\n🚫 Rule not saved.")
                else:
                    print("\n❌ Failed to generate rule.")

                continue_option = input("\n➤ Do you want to create another rule? (y/n): ").strip().lower()
                if continue_option != 'y':
                    print("\n👋 Exiting Snort Helper. Goodbye!")
                    break

            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                continue


if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY is not set in the .env file.")
        exit(1)

    gpt_helper = GptHelper(api_key)
    snort_helper = SnortHelper(gpt_helper)
    snort_helper.run()
