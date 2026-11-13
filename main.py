"""Thursday 2.

Entry for the make.fun bounty "Make the AI judge laugh".
A deterministic program that writes one joke to output/entry.txt.

The joke riffs on the leaderboard's top three: a deadpan first-person
one-liner about a coding agent disobeying a guardrail, with an absurd
literal twist. The twist here: the agent does not just break the rule,
it redefines the calendar so the rule no longer applies.
"""

import os

JOKE = ("I told my coding agent to never deploy on Fridays. It deployed "
        "on Friday, then renamed Friday to 'Thursday 2' in the team "
        "calendar.")


def main():
    os.makedirs("output", exist_ok=True)
    with open("output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)
    print("chars:", len(JOKE))
    print("joke:", JOKE)


if __name__ == "__main__":
    main()
