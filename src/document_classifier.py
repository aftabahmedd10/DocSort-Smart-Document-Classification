from euriai import EuriaiClient
import os
from dotenv import load_dotenv

load_dotenv()


def create_prompt(text):

    prompt = f""" 
            You are a document classification assistant.

        Your task is to analyze the following document text and classify it into **one** of the following categories:
        - Receipt
        - Invoice
        - Contract

        Read the text carefully. Consider the structure, keywords, and tone.

        Return only the category name. Do not explain your reasoning.

        ---

        Document Text:
        '''
        {text}
        '''

        ---

        Classification:

    """

    return prompt


def classify_text(text):
    api_key = os.getenv("EURI_API_KEY")
    
    client = EuriaiClient(
        api_key=api_key,
        model="deepseek-r1-distill-llama-70b",
    )

    response = client.generate_completion(
        prompt= create_prompt(text),
        temperature=0.7,
        max_tokens=2000
    )

    #print(response)
    #print(response['choices'][0]['message']['content'])
    return response['choices'][0]['message']['content']







