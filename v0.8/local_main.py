class SnortHelper:
    def __init__(self):
        pass

    def generate_rule(self, cve_id, title, date, pattern, sid):
        rule_template = (
            f'alert tcp any any -> any any '
            f'(msg:"{cve_id} {title}"; '
            f'flow:to_server,established; '
            f'content:"{pattern.split()[0]}"; http_method; '
            f'content:"{pattern.split()[1]}"; http_uri; '
            f'classtype:web-application-attack; '
            f'reference:cve,{cve_id}; '
            f'sid:{sid}; rev:1;)'
        )
        return rule_template

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
        print("Welcome to Snort Helper!".center(50))
        print("=" * 50)

        while True:
            print("\n Enter CVE information to generate a Snort Rule:")
            try:
                cve_id = input("  ➤ CVE ID: ").strip()
                title = input("  ➤ TITLE: ").strip()
                date = input("  ➤ DATE: ").strip()
                pattern = input("  ➤ PATTERN: ").strip()
                sid = input("  ➤ SID: ").strip()

                if not (cve_id and title and date and pattern and sid.isdigit()):
                    print("\n❌ Invalid input. Please provide all required fields correctly.")
                    continue

                rule = self.generate_rule(cve_id, title, date, pattern, sid)
                print("\n✨ Generated Snort Rule:")
                print("=" * 50)
                print(rule)
                print("=" * 50)

                save_option = input("\n💾 Do you want to save this rule? (y/n): ").strip().lower()
                if save_option == 'y':
                    self.save_rule(rule, sid)
                else:
                    print("\n🚫 Rule not saved.")

                continue_option = input("\n➤ Do you want to create another rule? (y/n): ").strip().lower()
                if continue_option != 'y':
                    print("\n👋 Exiting Snort Helper. Goodbye!")
                    break

            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                continue


if __name__ == "__main__":
    helper = SnortHelper()
    helper.run()
