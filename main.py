def count_words(self):
    words = self.split()
    return len(words)


def count_letters(self):
    letter_count = {}
    for letter in self.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count


def print_report(self):
    report = []
    report.append(f" --- Begin report of {f.name} ---")
    word_count = count_words(self)
    report.append(f"{word_count} words found in the document")
    report.append("")
    report.append("")
    letter_count = count_letters(self)
    letters_list = list(letter_count)
    letters_list.sort()
    for letter in letters_list:
        if letter.isalpha():
            report.append(
                    f"The '{letter}' character was found {letter_count[letter]} times")
    report.append("--- End report ---")
    for line in report:
        print(line)


with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    print_report(file_contents)
