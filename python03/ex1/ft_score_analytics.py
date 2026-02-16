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
    print("Scores processed:", scores)


# $> python3 ft_score_analytics.py 1500 2300 1800 2100 1950
# === Player Score Analytics ===
# Scores processed: [1500, 2300, 1800, 2100, 1950]
# Total players: 5
# Total score: 9650
# Average score: 1930.0
# High score: 2300
# Low score: 1500
# Score range: 800
# $> python3 ft_score_analytics.py
# === Player Score Analytics ===
# No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...
