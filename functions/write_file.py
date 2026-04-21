import os


def write_file(working_directory, file_path, content):
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Normalize and resolve target path
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Security check: must stay inside working directory
        valid_path = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not valid_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

        # If path is an existing directory, reject
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        # Ensure parent directories exist
        parent_dir = os.path.dirname(target_path)
        os.makedirs(parent_dir, exist_ok=True)

        # Write file (overwrite mode)
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"
