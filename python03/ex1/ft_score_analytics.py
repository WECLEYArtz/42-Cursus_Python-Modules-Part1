import sys


def main():
    no_arg_message = "No scores provided. Usage:" +\
            " python3 ft_score_analytics.py <score1> <score2> ..."

    scores = [arg for arg in sys.argv[1:] if arg]
    print("=== Player Score Analytics ===")
    if not len(scores):
        exit(no_arg_message)

    scores_filtered: list[int] = []

    for score in scores:
        try:
            scores_filtered += [int(score)]
        except ValueError:
            print(F"X Error: Can't convert '{score}' to integer")
    scores = scores_filtered
    print("Scores processed:", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))


if __name__ == "__main__":
    main()
