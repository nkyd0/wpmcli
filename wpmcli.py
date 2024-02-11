#!/usr/bin/env python

import random
import time

def get_word_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def get_random_words(word_list, num_words=10):
    return " ".join(random.sample(word_list, num_words))

def calculate_wpm(start_time, end_time, typed_words):
    total_time = end_time - start_time
    words_typed = len(typed_words.split())
    wpm = (words_typed / total_time) * 60
    return wpm

def main():
    word_list = get_word_list('wordlist.txt')
    print("wpmcli - test your typing speed")
    input("press enter to start...")

    words = get_random_words(word_list)
    print("\ngenerated words:")
    print(words)

    start_time = time.time()
    typed_words = input("\ntype: ")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed_words)

    typed_words_list = typed_words.split()
    correct_words = sum(1 for typed, actual in zip(typed_words_list, words.split()) if typed == actual)
    accuracy = (correct_words / len(words.split())) * 100

    print("\nresults:")
    print(f"your typing speed: {wpm:.2f} words per minute")
    print(f"your accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()

