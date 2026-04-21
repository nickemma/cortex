from functions.get_file_content import get_file_content


def print_result(label, result):
    print(f"\n{label}")
    if isinstance(result, str):
        print(result)
    else:
        print(result)


if __name__ == "__main__":

    # 1. Truncation test
    result = get_file_content("calculator", "lorem.txt")
    print("\nTest: lorem.txt (truncation check)")
    print("Length:", len(result))
    print("Truncated message present:", "[...File" in result)

    # 2. Normal file
    print_result("main.py", get_file_content("calculator", "main.py"))

    # 3. Nested file
    print_result(
        "pkg/calculator.py", get_file_content("calculator", "pkg/calculator.py")
    )

    # 4. Forbidden path
    print_result("/bin/cat", get_file_content("calculator", "/bin/cat"))

    # 5. Missing file
    print_result(
        "pkg/does_not_exist.py", get_file_content("calculator", "pkg/does_not_exist.py")
    )
