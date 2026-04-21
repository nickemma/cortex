from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print("Result for current directory:")
    result = get_files_info("calculator", ".")
    print("\n".join(f"  {line}" for line in result.split("\n")))
    print()

    print("Result for 'pkg' directory:")
    result = get_files_info("calculator", "pkg")
    print("\n".join(f"  {line}" for line in result.split("\n")))
    print()

    print("Result for '/bin' directory:")
    result = get_files_info("calculator", "/bin")
    print("\n".join(f"  {line}" for line in result.split("\n")))
    print()

    print("Result for '../' directory:")
    result = get_files_info("calculator", "../")
    print("\n".join(f"  {line}" for line in result.split("\n")))
