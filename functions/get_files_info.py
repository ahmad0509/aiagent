import os
from google import genai
from google.genai import types




def get_files_info(working_directory, directory="."):
    
    try:
        full_path=os.path.abspath(os.path.join(working_directory, directory))
        working_directory_abs=os.path.abspath(working_directory)

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'
        result = []
        for entry_name in os.listdir(full_path):
            entry_path = os.path.join(full_path, entry_name)
            is_dir = os.path.isdir(entry_path)
            file_size = os.stat(entry_path).st_size
            result.append({
                'name': entry_name,
                'file_size': file_size,
                'is_dir': is_dir
            })
        return result
    except Exception as e:
        return f"Error: {e}"

    
    
