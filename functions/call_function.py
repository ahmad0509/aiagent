working_directory = "./calculator"
from google.genai import types
from prompts import *
from functions.get_file_contents import *
from functions.get_files_info import *
from functions.run_python_file import *
from functions.write_file_contents import *


def call_function(function_call_part, verbose=False):
    name = function_call_part.name
    args = function_call_part.args or {}

    args['working_directory'] = working_directory

    if verbose:
        print(f"Calling function: {name}({args})")
    else:
        print(f" - Calling function: {name}")

    function_map = {
        'get_files_info': get_files_info,
        'get_file_content': get_file_content,  
        'run_python_file': run_python_file,
        'write_file_contents': write_file_contents,
    }

    if name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=name,
                    response={"error": f"Unknown function: {name}"},
                )
            ],
        )

    result = function_map[name](**args)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=name,
                response={"result": result},
            )
        ],
    )
