import sys


def main() -> None:
    no_arg_message = "No scores provided. Usage:" +\
            " python3 ft_score_analytics.py <score1> <score2> ..."

    scores = [arg for arg in sys.argv[1:] if arg]
    print("=== Player Score Analytics ===")
    if not len(scores):
        exit(no_arg_message)

    scores_filtered: list[int] = []

    for score in scores:
        try:
            value = int(score)
            if value < 0:
                print("Niggatives not allowed, rejecting", value)
                continue
            scores_filtered += [int(score)]
        except ValueError:
            print(F"X Error: Can't convert '{score}' to integer")
        except Exception as e:
            print("Unexcpecetd error", e)

    if not len(scores_filtered):
        return (print("\nNo valid values to make statistics of"))

    print("scores_filtered processed:", scores_filtered)
    print("Total players:", len(scores_filtered))
    print("Total score:", sum(scores_filtered))
    print(F"Average score: { sum(scores_filtered) / len(scores_filtered):.1f}")
    print("High score:", max(scores_filtered))
    print("Low score:", min(scores_filtered))
    print("Score range:", max(scores_filtered) - min(scores_filtered))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Unexcpecetd error", e)
