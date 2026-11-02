from typing import List, Tuple

MATCHING_BRACKETS = {
    ")": "(",
    "}": "{",
    ">": "<",
}
OPENING_BRACKETS = set(MATCHING_BRACKETS.values())
CLOSING_BRACKETS = set(MATCHING_BRACKETS.keys())


def validate_brackets(text: str) -> None:
    stack: List[Tuple[str, int]] = []
    error_positions: List[int] = []

    for index, char in enumerate(text):
        if char in OPENING_BRACKETS:
            stack.append((char, index))
        elif char in CLOSING_BRACKETS:
            expected_open = MATCHING_BRACKETS[char]
            if stack and stack[-1][0] == expected_open:
                stack.pop()
            else:
                error_positions.append(index)
                if stack:
                    _, unmatched_idx = stack.pop()
                    error_positions.append(unmatched_idx)

    while stack:
        _, idx = stack.pop()
        error_positions.append(idx)

    if error_positions:
        sorted_errors = sorted(set(error_positions))
        positions_str = ", ".join(map(str, sorted_errors))

        pointer_line = [" "] * len(text)
        for pos in sorted_errors:
            if pos < len(pointer_line):
                pointer_line[pos] = "^"
        visual_indicator = "".join(pointer_line)

        error_message = (
            f"Дужки незбалансовані на позиціях {positions_str}\n"
            f"{text}\n"
            f"{visual_indicator}"
        )
        raise ValueError(error_message)


def main() -> None:
    try:
        user_input = input("Введіть строку: ")
        validate_brackets(user_input)
        print("Строка валідна")
    except ValueError as exc:
        print(f"Помилка: {exc}")


if __name__ == "__main__":
    main()