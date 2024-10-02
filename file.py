def read(path: str) -> str:
    with open(path, 'r') as file:
        return file.read()


def write(path: str, content: str) -> str:
    with open(path, 'w') as file:
        file.write(content)

        return f'[{content}] was successfully written to the file'
