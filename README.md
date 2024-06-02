<p align="center">
  <img src="https://w7.pngwing.com/pngs/567/444/png-transparent-robotics-chatbot-technology-robot-education-electronics-computer-program-humanoid-robot-thumbnail.png" width="100" />
</p>
<p align="center">
    <h1 align="center">CodeStral Code Assistant</h1>
</p>
<p align="center">
    Code-Bot is a chatbot designed to assist users with code-related questions. It interacts with the Codestral API to provide code solutions, including descriptions, programming language details, imports, functional code blocks, and sample input/output.
</p>
<p align="center">
		Developed with the software and tools below.
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/-streamlit-05122A?style=flat&logo=streamlit&logoColor=FFA518" alt="StreamLit">
</p>
<hr>

## Coming Soon

### Self-Correcting Code Agent
In the upcoming update, I am implementing a self-correcting code agent. This feature will allow the agent to self-execute and evaluate the code before presenting it to the user, ensuring higher accuracy and reliability.

### Streamlit Frontend Updates
I am also planning to update the Streamlit frontend to improve user experience and add new interactive features.

---

## 🔗 Quick Links

> - [📍 Overview](#-overview)
> - [🔑 Obtaining Codestral API Key](#-obtaining-codestral-api-key)
> - [📦 Features](#-features)
> - [📂 Repository Structure](#-repository-structure)
> - [🚀 Getting Started](#-getting-started)
>   - [⚙️ Installation](#️-installation)
>   - [⚙️ Configuration](#-configuration)
>   - [🤖 Running CodeStral-Code-Assistant](#-running-CodeStral-Code-Assistant)
> - [🤝 Contributing](#-contributing)

---

## 📍 Overview

Code-Bot is an interactive chatbot designed to assist users with programming-related queries. By leveraging the Codestral API, Code-Bot provides comprehensive code solutions that include:

- Descriptions of the code solutions.
- Programming language specifics.
- Necessary import statements.
- Fully functional code blocks.
- Sample input and output for the provided code.

The application is built using Streamlit for the web interface and integrates seamlessly with external APIs to generate accurate and executable code snippets. Whether you need help with sorting algorithms, API calls, or any other programming task, Code-Bot is here to help streamline your coding process.

---

## 🔑 Obtaining Codestral API Key

To use Code-Bot, you need to obtain an API key from Codestral. Follow these steps to get your API key:

1. **Visit the Codestral Official Website**:
   - Go to [Codestral official website](https://console.mistral.ai/codestral).

2. **Login or Sign Up**:
   - If you already have an account, log in.
   - If you are new to Codestral, sign up for a new account.

3. **Request Access**:
   - Once logged in, click on the **Request Access** button.

4. **Verify Your Phone Number**:
   - You will be prompted to verify your phone number. Follow the instructions to complete the verification process.

5. **Wait for Approval**:
   - After verifying your phone number, you will receive a request granted email. (In my case, it took 2 hours)

6. **Generate Your API Key**:
   - Once you receive the approval email, return to the [Codestral official website](https://console.mistral.ai/codestral).
   - Follow the instructions to generate your API key.

> **Note:** The Codestral API is free to use until August 1st, 2024.

By following these steps, you will be able to obtain and set up your Codestral API key to start using Code-Bot.

---

## 📦 Features

Code-Bot comes with a variety of features designed to make it a robust and versatile tool for programmers:

### Code Solutions
- **Comprehensive Descriptions**: Provides detailed explanations of the code solutions to help users understand the logic and implementation.
- **Multi-Language Support**: Capable of generating code in multiple programming languages based on user queries.

### Import Statements
- **Automatic Import Detection**: Identifies and includes necessary import statements for the generated code, ensuring it runs without additional configuration.

### Functional Code Blocks
- **Executable Code**: Generates fully functional code snippets that can be executed directly, saving users time on debugging and syntax errors.
- **Formatted Output**: Ensures the generated code is well-formatted and readable, using appropriate indentation and line breaks.

### Sample Input/Output
- **Example Scenarios**: Provides sample input and output for the generated code, helping users test and understand the code better.

### API Integration
- **Codestral API**: Integrates with the Codestral API to leverage powerful code generation capabilities.
- **Real-Time Responses**: Fetches and returns code solutions in real-time, providing quick assistance to user queries.

### User-Friendly Interface
- **Streamlit Integration**: Built using Streamlit to provide an intuitive and interactive web interface, making it easy for users to input their queries and receive responses.
- **Customizable**: Allows users to configure the API key and other settings to suit their specific needs.

These features make Code-Bot a comprehensive tool for programmers, whether they are beginners seeking guidance or experienced developers looking for quick code snippets.

---

## 📂 Repository Structure

```sh
└── CodeStral-Code-Assistant/
    ├── README.md
    └── app.py
```

---

## 🚀 Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

```
pip install requests
```
```
pip install streamlit
```

### ⚙️ Installation

1. Clone the CodeStral-Code-Assistant repository:

```sh
git clone https://github.com/rahul2002m/CodeStral-Code-Assistant
```

2. Change to the project directory:

```sh
cd CodeStral-Code-Assistant
```

3. Install the dependencies:

```sh
pip install -r requirements.txt
```


### ⚙️ Configuration

Before running the application, you need to set up your Mistral Codestral API key.

- Open the app.py file
- Replace the placeholder in the following line with your actual API key:

```
os.environ["MISTRAL_API_KEY"] = "your_api_key_here"
```


### 🤖 Running CodeStral-Code-Assistant

Use the following command to run CodeStral-Code-Assistant:

```sh
streamlit run app.py
```

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Submit Pull Requests](https://github.com/rahul2002m/CodeStral-Code-Assistant/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/rahul2002m/CodeStral-Code-Assistant/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/rahul2002m/CodeStral-Code-Assistant/issues)**: Submit bugs found or log feature requests for Code-assistant.

<details>
    <summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a Git client.
   ```sh
   git clone https://github.com/rahul2002m/CodeStral-Code-Assistant
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.

Once your PR is reviewed and approved, it will be merged into the main branch.

</details>

---
