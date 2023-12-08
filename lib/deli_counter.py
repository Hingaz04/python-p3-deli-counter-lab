def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        current_line = ", ".join(
            f"{index + 1}. {name}" for index, name in enumerate(katz_deli))
        print(f"The line is currently: {current_line}")


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")
