    # if verbose:
    #     print (f"User prompt: {user_prompt}")
    #     print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    #     print("Response tokens:", response.usage_metadata.candidates_token_count)
    # if response.function_calls and len(response.function_calls) > 0:
    #     for function_call_part in response.function_calls:
    #         print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    # else:
    #     print("Response:")
    #     print(response.text)