#!/usr/bin/env python3

import pandas


def load_file():
    try:
        df = pandas.read_csv("/usr/local/grewords/words.csv")
        df = df.sample(frac=1).reset_index(drop=True)
        return df
    except IOError:
        print("Please make sure the file exists")
        exit
    except Exception as exp:
        print(repr(exp))


def main():
    df = load_file()
    if df is not None:
        for index, row in df.iterrows():
            print(f"\nWord: {row['word']}\nMeaning: {row['meaning']}")
            input("\nEnter any key to continue...")
        print("You have reached the end of the file :)")


if __name__ == "__main__":
    main()
