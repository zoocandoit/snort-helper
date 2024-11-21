# **Snort Helper**

A Python utility powered by OpenAI GPT API for generating and managing Snort intrusion detection rules. Snort Helper streamlines the process of writing Snort rules by leveraging GPT's natural language processing capabilities to dynamically generate rules based on user input.

---

## **Features**
- **GPT-Powered**: Automatically generate Snort rules based on user-provided descriptions or data.
- **Interactive Prompts**: Provide CVE information, patterns, protocols, and other details to dynamically generate rules.
- **Flexible Output**: Save generated rules to customizable `.rules` files.
- **Rule Validation**: Ensures rules are syntactically correct before saving.

---

## **Installation**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/snort-helper.git
   cd snort-helper
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up `.env` for GPT API:
   - Create a `.env` file in the root directory:
     ```plaintext
     OPENAI_API_KEY=your_openai_api_key_here
     ```
   - Ensure `.env` is added to `.gitignore` to keep your API key secure.

---

## **Usage**

1. Run the Snort Helper:
   ```bash
   python main.py
   ```

2. Follow the prompts to input Snort rule details or paste raw data:
   - Example input:
     ```yaml
     CVE ID: CVE-2024-1234
     TITLE: VICIdial RCE
     Protocol: tcp
     Source Port: any
     Destination Port: 80
     Flow: to_server,established
     Pattern: SELECT sleep(
     SID: 250169
     ```

3. GPT will generate a Snort rule based on your input:
   ```plaintext
   alert tcp any any -> any 80 (msg:"CVE-2024-1234 VICIdial RCE"; flow:to_server,established; content:"SELECT sleep("; nocase; classtype:web-application-attack; sid:250169; rev:1;)
   ```

4. Save the rule to a `.rules` file when prompted.

---

## **Example Snort Rule**

```plaintext
alert tcp any any -> any 80 (msg:"CVE-2024-1234 VICIdial RCE"; flow:to_server,established; content:"SELECT sleep("; nocase; classtype:web-application-attack; sid:250169; rev:1;)
```

