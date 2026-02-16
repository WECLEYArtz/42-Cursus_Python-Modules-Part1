import sys

no_arg_message = "\
No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ..."

if __name__ == "__main__":
    scores = [arg for arg in sys.argv[1:] if arg]
    print("=== Player Score Analytics ===")
    if not len(scores):
        exit(no_arg_message)

    i = 0
    scores_tmp: list[int] = []
    while i < len(scores):
        try:
            scores_tmp += [int(scores[i])]
        except ValueError:
            print(F"<X Can't convert '{scores[i]}' to integer, skipping... X>")
        i += 1
    scores = scores_tmp
    print("Scores processed::", scores)
    print("Total players:", len(scores))
    print("Total score:", sum(scores))
    print("Average score:", sum(scores) / len(scores))
    print("High score:", max(scores))
    print("Low score:", min(scores))
    print("Score range:", max(scores) - min(scores))
