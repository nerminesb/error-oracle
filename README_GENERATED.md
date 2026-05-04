# Error Oracle ðŸ”®

Error Oracle is a set of intelligent CLI tools designed to streamline the debugging and documentation process for Python projects. By leveraging the power of Gemini AI, it transforms cryptic terminal errors into actionable fixes and automates the creation of professional project documentation.

## Features

- **Automated Debugging**: Instantly diagnose crashes by piping terminal errors directly into the AI Oracle.
- **Context-Aware Analysis**: The Oracle automatically scans your local project files to provide Gemini with the necessary context for precise error resolution.
- **Smart Fixes**: Receive pinpointed line numbers and corrected code blocks for rapid iteration.
- **Documentation Automation**: Generate professional `README.md` files based on your project's actual source code using the included `architect.py`.

## Installation

Ensure you have the [Gemini CLI](https://github.com/google/gemini-cli) installed and configured in your environment.

```bash
# Clone the repository
git clone https://github.com/your-username/error-oracle.git
cd error-oracle
```

## Usage

### 1. The Oracle (Debugging)
The Oracle listens to your terminal output. When a command fails, pipe the error output (including `stderr`) into `oracle.py`.

```bash
# Example: Debugging a script that crashes
python broken_code.py 2>&1 | python oracle.py
```

The Oracle will analyze the traceback, review your project files, and output a senior-level debugging report including the exact cause and the fix.

### 2. The Architect (README Generation)
Use the Architect to maintain your project's documentation. It scans all `.py` files in the directory and uses Gemini to write a professional summary.

```bash
python architect.py
```
*The output will be saved as `README_GENERATED.md`.*

## Example Project Structure

- `oracle.py`: The core debugging engine.
- `architect.py`: The documentation generator.
- `broken_code.py`: A sample script provided for testing the Oracle's debugging capabilities.

## License

This project is open-source and available under the [MIT License](LICENSE).