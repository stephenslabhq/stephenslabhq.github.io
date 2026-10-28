
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent

HTML_FILE = PROJECT_ROOT / "index.html"
CSS_FILE = PROJECT_ROOT / "style.css"


def check(condition, success_message, failure_message):
    if condition:
        print(f"PASS: {success_message}")
        return True

    print(f"FAIL: {failure_message}")
    return False


def main():
    results = []

    results.append(
        check(
            HTML_FILE.is_file(),
            "index.html exists",
            "index.html is missing",
        )
    )

    results.append(
        check(
            CSS_FILE.is_file(),
            "style.css exists",
            "style.css is missing",
        )
    )

    if HTML_FILE.is_file():
        html = HTML_FILE.read_text(encoding="utf-8")

        results.append(
            check(
                'href="style.css"' in html,
                "HTML references style.css",
                "HTML does not reference style.css correctly",
            )
        )

        results.append(
            check(
                "<title>" in html and "</title>" in html,
                "HTML contains a title element",
                "HTML title element is missing",
            )
        )

        results.append(
            check(
                'name="viewport"' in html,
                "HTML contains a viewport declaration",
                "HTML viewport declaration is missing",
            )
        )

    print(f"\nResults: {sum(results)}/{len(results)} checks passed")

    if not all(results):
        sys.exit(1)


if __name__ == "__main__":
    main()
