from constants import TOKEN
from transifex import check_for_input, main


if __name__ == "__main__":
    languages = check_for_input()
    main(languages)
