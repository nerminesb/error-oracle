The Error Oracle

> **Transforming Terminal Crashes into Solutions.**
> Built for the European Summer Hackathon (Paris 2026).

 The Concept
During a 24-hour hackathon, every second spent copy-pasting errors into a browser is a second wasted. **The Error Oracle** is a terminal-native debugging companion that uses a Unix-style pipe to intercept crashes and provide surgical fixes instantly.



 How it Works
The Oracle uses a **Context-Aware Pipeline**:
1. **Redirection**: It captures `STDERR` (the error text) using the `2>&1` operator.
2. **Context Aggregation**: It scans your local directory to read your actual source code.
3. **LLM Reasoning**: It sends both the crash data AND your code to Gemini.
4. **Resolution**: It outputs the exact file, line number, and corrected code block directly back to your terminal.

 Usage
To debug any Python script, simply pipe it:
```bash
python your_script.py 2>&1 | python oracle.py
