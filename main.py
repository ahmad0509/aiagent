import os
import sys
from google import genai
from dotenv import load_dotenv
from google.genai import types
from config import *
from prompts import *
from functions.call_function import *


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    if len(sys.argv) < 2:
        print("Usage: python main.py <your prompt here>")
        sys.exit(1)
    args = sys.argv[1:]

    verbose = False
    if "--verbose" in args:
        verbose = True
        args.remove("--verbose")
    
    user_prompt = " ".join(args)
    messages = [types.Content(
    role='user', parts=[types.Part(text=user_prompt)]
    )]
    max_iterations = 20
    try:
        for i in range(max_iterations):
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions],
                    system_instruction=system_prompt
                )
            )
            for candidate in response.candidates:
                    messages.append(candidate.content)

            if response.function_calls and len(response.function_calls) > 0:
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose=verbose)
                    if not function_call_result.parts or not function_call_result.parts[0].function_response:
                        raise RuntimeError("Function call response missing function_response")
                    messages.append(types.Content(
                                role="tools",
                                parts=[function_call_result.parts[0]]
                            ))
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                    
            else:
                if response.text and response.text.strip() != "":
                    print("Response:")
                    print(response.text)
                    break
        else:
            print("Max iterations reached without final response.")
    except Exception as e:
        print(f"Error during interaction: {e}")




if __name__ == "__main__":
    main()