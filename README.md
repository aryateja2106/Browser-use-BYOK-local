# Browser-Use Web UI

This project provides a web-based user interface for interacting with and controlling a browser automation agent. It allows you to give natural language commands to a large language model (LLM) which then translates those commands into browser actions.

## Features

*   **Web-based UI:** A simple and intuitive web interface for controlling the browser agent.
*   **LLM Integration:**  Supports various LLMs including Google Gemini, OpenAI, and Anthropic.
*   **Browser Control:**  Automates browser actions based on your commands.
*   **Customizable:**  Allows you to configure the LLM provider, model, and other settings.

## Setup Instructions (macOS)

These instructions will guide you through setting up the `browser-use-web-ui` on your macOS machine.

### Prerequisites

*   **Python 3.11 or higher:** You can check your Python version by running `python3 --version`.
*   **Git:** You can check if Git is installed by running `git --version`.

### 1. Clone the Repository

Open your terminal and clone this repository:

```bash
git clone https://github.com/aryateja2106/browser-use-web-UI.git
cd browser-use-web-UI
```

### 2. Set Up the Python Environment

We'll use `uv` to create a virtual environment and install the necessary dependencies.

```bash
# Create the virtual environment
uv venv --python 3.11

# Activate the virtual environment
source .venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages and Playwright browsers:

```bash
uv pip install -r requirements.txt
playwright install
```

### 4. Configure Your Environment

Create a `.env` file by copying the example file:

```bash
cp .env.example .env
```

Now, open the `.env` file in a text editor (e.g., `nano .env` or `code .env`) and add the following configuration:

```
# Your Google Gemini API Key
GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"

# Set the default LLM to Google
DEFAULT_LLM="google"

# --- Mac-Specific Browser Settings ---
# Path to your Chrome browser
CHROME_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Path to your Chrome user data
CHROME_USER_DATA="/Users/YourUsername/Library/Application Support/Google/Chrome"

# Keep the browser open between tasks
CHROME_PERSISTENT_SESSION=true
```

**Important:**

*   Replace `"YOUR_GEMINI_API_KEY"` with your actual Gemini API key.
*   Replace `YourUsername` with your macOS username.

### 5. Run the Application

To run the application, you first need to start Google Chrome in debug mode.

**Step 1: Start Chrome in Debug Mode**

Open a new terminal window and run the following command:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222
```

This will launch a new Chrome window that is ready for automation.

**Step 2: Start the Web UI**

In your original terminal window (where you activated the virtual environment), start the web UI:

```bash
python webui.py --ip 127.0.0.1 --port 7788
```

### 6. Access the Web Interface

Open a **different browser** (like Firefox or Safari) and navigate to:

[http://127.0.0.1:7788](http://127.0.0.1:7788)

You should now see the web UI. Make sure to check the **"Use Own Browser"** option in the **Browser Settings** section.

You are now ready to start giving commands to the browser agent!