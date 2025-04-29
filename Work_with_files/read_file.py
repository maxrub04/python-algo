def read_file_safe(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"ERROR: file '{file_path}' is not found.")
        return None
    except Exception as e:
        print("UNKNOWN ERROR:", e)
        return None