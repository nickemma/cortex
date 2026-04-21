from functions.run_python_file import run_python_file


def print_result(label, result):
    print(f"\n{label}")
    print(result)


if __name__ == "__main__":

    # 1. Run main.py (usage instructions)
    print_result("main.py", run_python_file("calculator", "main.py"))

    # 2. Run main.py with args
    print_result(
        "main.py with args", run_python_file("calculator", "main.py", ["3 + 5"])
    )

    # 3. Run tests
    print_result("tests.py", run_python_file("calculator", "tests.py"))

    # 4. Path traversal attempt
    print_result("../main.py", run_python_file("calculator", "../main.py"))

    # 5. Missing file
    print_result("nonexistent.py", run_python_file("calculator", "nonexistent.py"))

    # 6. Wrong file type
    print_result("lorem.txt", run_python_file("calculator", "lorem.txt"))
