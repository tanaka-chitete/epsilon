from modes import run_in_command_line_mode, run_in_interactive_mode
import sys


def main():
    args = sys.argv
    if not len(args):
        run_in_interactive_mode()
    else:
        source_language = args[1]
        target_language = args[2]
        word_to_translate = args[3]

        run_in_command_line_mode(source_language, target_language, word_to_translate)


if __name__ == "__main__":
    main()
