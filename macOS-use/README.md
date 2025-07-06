# Empowering Your Mac with AI: A Guide to macOS-use

Hello there! I'm Arya Teja Rudraraju, an AI Product Manager passionate about making cutting-edge technology accessible to everyone. Today, I'm thrilled to introduce you to `macOS-use`, a groundbreaking project that allows AI agents to interact with and control your macOS system using natural language. Imagine telling your MacBook what to do, and it simply gets it done—across ANY application!

This incredible innovation is brought to you by the brilliant minds of **Ofir Ozeri**, **Magnus**, and **Gregor**. Their collaborative efforts have paved the way for a new era of human-computer interaction, and we are immensely grateful for their pioneering work.

## What is macOS-use?

`macOS-use` is a powerful tool that bridges the gap between large language models (LLMs) and your macOS environment. It enables AI agents to understand your commands and translate them into actions on your Mac, opening up a world of possibilities for automation, productivity, and intuitive control. Whether it's opening applications, navigating interfaces, or performing complex tasks, `macOS-use` aims to make your Mac truly responsive to your voice.

## Getting Started: Your Step-by-Step Guide

To help you get up and running with `macOS-use` quickly and smoothly, I've put together these clear, step-by-step instructions. Let's make your Mac smarter together!

### Prerequisites

Before we begin, ensure you have the following installed on your macOS system:

*   **Python 3.11 or higher:** You can check your Python version by running `python3 --version` in your terminal.
*   **Git:** Verify Git installation with `git --version`.
*   **Homebrew:** A package manager for macOS. If you don't have it, install it from [https://brew.sh/](https://brew.sh/).
*   **uv:** A fast Python package installer and resolver. We'll install it using Homebrew.
*   **Git LFS:** (Large File Storage) is required for some files in the repository.

### Installation Steps

1.  **Navigate to the `macOS-use` directory:**
    First, ensure you are in the `macOS-use` directory within your project. If you've just cloned the main repository, you'll need to navigate into this specific sub-directory:

    ```bash
    cd macOS-use
    ```

2.  **Install `uv` (if you haven't already):**
    `uv` is our recommended tool for managing Python environments due to its speed and efficiency.

    ```bash
    brew install uv
    ```

3.  **Install Git LFS (if you haven't already):**
    This is crucial for handling larger files within the repository.

    ```bash
    brew install git-lfs
    git lfs install
    ```

4.  **Set up your Python Environment:**
    We'll create a dedicated virtual environment for `macOS-use` to keep its dependencies isolated from your system Python.

    ```bash
    uv venv
    source .venv/bin/activate
    ```

5.  **Configure your API Key:**
    `macOS-use` requires an API key from a supported LLM provider (OpenAI, Anthropic, or Gemini). While Gemini is free and works well, the creators note that OpenAI or Anthropic APIs might offer more reliable performance at this stage.

    Copy the example environment file:

    ```bash
    cp .env.example .env
    ```

    Now, open the newly created `.env` file using your preferred text editor (e.g., `nano .env`, `code .env`, or `open -e .env`) and add your API key. For example, if you're using Gemini:

    ```
    GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
    ```
    **Remember to replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual key.**

6.  **Install Project Dependencies:**
    With your environment set up and API key configured, install all necessary Python packages:

    ```bash
    uv pip install --editable .
    ```

### Crucial: Enable Accessibility Permissions

For `macOS-use` to interact with your applications, you **must** grant accessibility permissions to your terminal application (or your IDE, if you're running scripts from there). Without this, the agent will not be able to control your Mac's UI.

1.  Go to **System Settings** (or System Preferences on older macOS versions).
2.  Navigate to **Privacy & Security**.
3.  Scroll down and click on **Accessibility**.
4.  Click the **+** button and add your terminal application (e.g., Terminal, iTerm2, VS Code) to the list of allowed applications. Make sure the checkbox next to it is **checked**.

### Running Your First Example

Now that everything is set up, let's try a simple command!

#### Option 1: Using the Gradio Web UI (Recommended for interactive testing)

`macOS-use` comes with a user-friendly web interface built with Gradio, which makes it much easier to interact with the agent and observe its actions.

1.  **Install Gradio App Dependencies:**

    ```bash
    cd gradio_app
    uv pip install -r requirements.txt
    cd .. # Go back to the macOS-use root directory
    ```

2.  **Launch the Gradio UI:**
    Run the following command. This will start a local web server. Look for a URL (usually `http://127.0.0.1:7860` or similar) in the output. Copy and paste this URL into your web browser.

    ```bash
    python gradio_app/app.py
    ```

    *Note: This command will keep running in your terminal. To stop the UI, press `Ctrl+C`.*

3.  **Interact via the Web UI:**
    Once the UI loads in your browser, you can enter tasks in the provided input field (e.g., "open the calculator app and calculate 21 + 22") and observe the agent's actions and output directly in the interface.

#### Option 2: Running Tasks via Script

For direct execution of tasks, you can use the `examples/calculate.py` script. We've modified it to accept a task as a command-line argument.

1.  **Run the script with your task:**

    ```bash
    python examples/calculate.py --task "open Obsidian, create a new file, and write 'Hi' in it."
    ```

    Replace the example task with your desired command. You will see the agent's progress and any errors directly in your terminal.

### Important Considerations

*   **UI Element Identification:** The agent relies on identifying UI elements. If an action fails, it might be due to changes in the application's UI or the agent's inability to precisely locate the target element. Experiment with different phrasing or simpler tasks if you encounter issues.
*   **API Quotas:** If you are using a free tier API key (like Gemini's), you might encounter `ResourceExhausted` errors if you exceed the rate limits. Consider upgrading your plan or using a different provider if this becomes a frequent issue.

### What's Next?

You've just taken your first step into controlling your Mac with AI! Explore the `examples/` directory for more ideas, and consider diving into the `macOS-use` codebase to understand its inner workings. The possibilities are truly exciting.

We hope this guide helps you harness the power of `macOS-use` and experience a new level of interaction with your macOS device. Enjoy!
