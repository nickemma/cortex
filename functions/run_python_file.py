import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Resolve target file path
        absolute_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # 1. Security check: must stay inside working directory
        if os.path.commonpath([working_dir_abs, absolute_file_path]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # 2. Must exist and be a file
        if not os.path.isfile(absolute_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # 3. Must be a Python file
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # 4. Build command
        command = ["python", absolute_file_path]

        if args:
            command.extend(args)

        # 5. Run subprocess safely
        result = subprocess.run(
            command, cwd=working_dir_abs, capture_output=True, text=True, timeout=30
        )

        # 6. Build output string
        output_parts = []

        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not result.stdout.strip() and not result.stderr.strip():
            output_parts.append("No output produced")
        else:
            if result.stdout.strip():
                output_parts.append(f"STDOUT:\n{result.stdout.strip()}")
            if result.stderr.strip():
                output_parts.append(f"STDERR:\n{result.stderr.strip()}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"
