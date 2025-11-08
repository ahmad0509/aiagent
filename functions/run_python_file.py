import os
import subprocess
from google.genai import types




def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path=os.path.abspath(os.path.join(working_directory, file_path))
        working_directory_abs=os.path.abspath(working_directory)

        if not full_path.startswith(working_directory_abs):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'
        if not full_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
        cmd = ["python3", full_path] + list(args)

        completed_process = subprocess.run(
            cmd,
            cwd=working_directory_abs,
            timeout=30,
            capture_output=True,
            text=True
        )
        output_lines = []
        if completed_process.stdout:
            output_lines.append(f"STDOUT: {completed_process.stdout.strip()}")
        if completed_process.stderr:
            output_lines.append(f"STDERR: {completed_process.stderr.strip()}")
        if completed_process.returncode != 0:
            output_lines.append(f"Process exited with code {completed_process.returncode}")

        if not output_lines:
            return "No output produced."

        return "\n".join(output_lines)
    except subprocess.TimeoutExpired as e:
        return f"Error: executing Python file: {e}"
    except Exception as e:
        return f"Error: {e}"