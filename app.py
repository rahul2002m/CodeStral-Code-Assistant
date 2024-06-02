"""
Code-Bot is a chatbot that can help you with code related questions.
"""

import json
import os

import requests
import streamlit as st

os.environ["MISTRAL_API_KEY"] = "" #TODO: Insert Mistral codestral API key
api_key = os.environ["MISTRAL_API_KEY"]

def get_response(question):
    """
    Get the response from the Codestral API
    """
    output = {
        "prefix": "A description of the code solution",
        "programming_language": "The programming language",
        "imports": "The imports",
        "code": "The functioning code block. Write the whole code in single line and use \t and \n for tab and new line",
        "sample_io": "Generate the sample input and output for the code generated {'input': '', 'output': ''}"
    }

    model = "codestral-latest"
    messages = [{
                "role": "system",
                "content": f"""You're a coding assistant. Ensure any code you provided can be executed with all required imports and variables defined. \n
                Structure your answer in the JSON format: {output}

                Here's the question: """
            }, {"role": "user", "content": question}]


    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    res = requests.post(
        "https://codestral.mistral.ai/v1/chat/completions",
        headers=headers,
        json ={
            "model": model,
            "messages": messages,
            "response_format": {"type": "json_object"}
        }
    )
    res = res.json()
    response = res["choices"][0]["message"]["content"]
    response = response.replace("```python", "")
    response = response.replace("```", "")
    print(response)
    response = json.loads(response)
    return response

def main():
    """
    Main function to run the app
    """
    st.set_page_config(page_title="Code-Bot", page_icon=":robot:")
    st.title("Dobby - Code Assistant")
    st.session_state.api_key = "lakksd"
    st.subheader("Ask a question")
    if st.session_state.api_key:
        user_input = st.text_input("Enter your question here:")
        print("user input: ", user_input)
        if user_input:
            response = get_response(user_input)
            with st.chat_message("user"):
                st.write(user_input)
            with st.chat_message("assistant"):
                if response.get("prefix") and response["prefix"]!= "None":
                    st.write("Description")
                    st.write(response["prefix"])
                if response.get("imports") and response["imports"]!= "None":
                    st.write("Imports")
                    st.code(response["imports"], language=response["programming_language"])
                if response.get("code") and response["code"]!= "None":
                    st.write("Code")
                    st.code(response["code"], language=response["programming_language"])
                if response.get("sample_io") and response["sample_io"]!= "None":
                    if response["sample_io"].get("input") and response["sample_io"]["input"]!= "None":
                        st.write("Sample Input")
                        st.code(response["sample_io"]["input"], language=response["programming_language"])
                    if response["sample_io"].get("output") and response["sample_io"]["output"]!= "None":
                        st.write("Sample Output")
                        st.code(response["sample_io"]["output"], language=response["programming_language"])


if __name__ == "__main__":
    main()
