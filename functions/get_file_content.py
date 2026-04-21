import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        # Absolute working directory
        working_dir_abs = os.path.abspath(working_directory)

        # Resolve and normalize target path
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Security check: must stay inside working directory
        valid_path = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not valid_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Must be a real file
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file content safely (up to MAX_CHARS)
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read(MAX_CHARS)

            # Check if truncated
            extra = f.read(1)
            if extra:
                content += (
                    f'\n[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )

        return content

    except Exception as e:
        return f"Error: {str(e)}"
