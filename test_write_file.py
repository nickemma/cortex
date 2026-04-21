from functions.write_file import write_file


def print_result(label, result):
    print(f"\n{label}")
    print(result)


if __name__ == "__main__":

    # 1. Overwrite existing file
    print_result(
        "write_file: overwrite lorem.txt",
        write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    )

    # 2. Write to nested new file
    print_result(
        "write_file: new nested file",
        write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    )

    # 3. Forbidden path (outside working directory)
    print_result(
        "write_file: forbidden path",
        write_file("calculator", "/tmp/temp.txt", "this should not be allowed"),
    )
