from google.genai import types


system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, create a step-by-step function call plan.

You have access to these operations with calls that include parameters:

- List files and directories relative to a working directory.
- Read contents of files by path.
- Execute Python files with optional arguments.
- Write or overwrite files with given contents.

The working directory path is managed automatically and does not need to be specified in your function call parameters.

Operate with the understanding that the system will send back to you the results of each function call and you may make additional calls based on those results.

Compose your responses by deciding whether to call a function next or provide a final answer via text.

The agent will execute your plan iteratively, updating context with function call responses before generating the next step.

Only proceed to the next function call or completion when adequate information is available.

Be concise and clear in your function calls and in final output text.

"""
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="List file contents, constrained to max_chars.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read contents from, relative to the working directory.",
            ),
        },
    ),
)
schema_write_file_contents = types.FunctionDeclaration(
    name="write_file_contents",
    description="Write contents to a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write contents to, relative to the working directory.",
            ),
            "content": types.Schema(
            type=types.Type.STRING,
            description="The content to write",
        ),
        },
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="run python file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file path to run",
            ),
        },
    ),
)
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file_contents
    ]
)