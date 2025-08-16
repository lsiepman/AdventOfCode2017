# IMPORTS
import re

# DATA
file = open("Data - Day09.txt")
data = file.read().strip()


# ANSWER 1
without_cancel = re.sub(r"!.{1}", "", data)
without_garbage = re.sub(r"<[^>]*>", "", without_cancel)


def get_score(text):
    score = 0

    current_level = 0
    for i in text:
        if i == "{":
            current_level += 1
        elif i == "}":
            score += current_level
            current_level -= 1
        else:
            pass

    return score


print(f"Answer 9a: {get_score(without_garbage)}")


garbage = re.findall(r"<([^>]*)>", without_cancel)
garbage_text = "".join(garbage)

print(f"Answer 9b: {len(garbage_text)}")
