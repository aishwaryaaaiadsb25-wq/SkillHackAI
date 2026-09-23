import requests
import re
from bs4 import BeautifulSoup


# ============================================================
# LEETCODE PROFILE
# ============================================================

def get_leetcode_profile(username):

    username = username.strip()

    if not username:
        return None

    solved_url = (
        "https://leetpulse-api.vercel.app/api/leetcode/solved/"
        + username
    )

    total = 0
    easy = 0
    medium = 0
    hard = 0

    try:
        response = requests.get(
            solved_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )

        if response.status_code == 200:
            data = response.json()

            total = data.get("solvedProblem", 0)
            easy = data.get("easySolved", 0)
            medium = data.get("mediumSolved", 0)
            hard = data.get("hardSolved", 0)

    except Exception:
        pass

    graphql_url = "https://leetcode.com/graphql/"

    query = """
    query getUserProfile($username: String!) {

        matchedUser(username: $username) {

            username

            profile {
                ranking
                reputation
            }

            submitStatsGlobal {
                acSubmissionNum {
                    difficulty
                    count
                    submissions
                }
            }

            languageProblemCount {
                languageName
                problemsSolved
            }

            badges {
                id
                name
            }
        }

        userContestRanking(username: $username) {
            attendedContestsCount
            rating
            globalRanking
            topPercentage
        }
    }
    """

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com/"
    }

    try:

        response = requests.post(
            graphql_url,
            json={
                "query": query,
                "variables": {"username": username}
            },
            headers=headers,
            timeout=20
        )

        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("errors"):
            return None

        root = data.get("data", {})
        user = root.get("matchedUser")

        if not user:
            return None

        if total == 0:

            stats = (
                user
                .get("submitStatsGlobal", {})
                .get("acSubmissionNum", [])
            )

            for item in stats:

                difficulty = item.get("difficulty")
                count = item.get("count", 0)

                if difficulty == "All":
                    total = count

                elif difficulty == "Easy":
                    easy = count

                elif difficulty == "Medium":
                    medium = count

                elif difficulty == "Hard":
                    hard = count

        contest = root.get("userContestRanking")

        rating = "N/A"
        contest_rank = "N/A"
        top_percentage = "N/A"
        contests = 0

        if contest:

            rating = contest.get("rating", "N/A")
            contest_rank = contest.get(
                "globalRanking",
                "N/A"
            )
            top_percentage = contest.get(
                "topPercentage",
                "N/A"
            )
            contests = contest.get(
                "attendedContestsCount",
                0
            )

        ranking = user.get(
            "profile",
            {}
        ).get(
            "ranking",
            "N/A"
        )

        reputation = user.get(
            "profile",
            {}
        ).get(
            "reputation",
            0
        )

        languages = []

        for item in user.get(
            "languageProblemCount",
            []
        ):

            language = item.get(
                "languageName"
            )

            problems = item.get(
                "problemsSolved",
                0
            )

            if language:

                languages.append({
                    "language": language,
                    "problems": problems
                })

        languages.sort(
            key=lambda x: x["problems"],
            reverse=True
        )

        badges = []

        for badge in user.get(
            "badges",
            []
        ):

            name = badge.get("name")

            if name:
                badges.append(name)

        language_names = [item["language"] for item in languages]

        return {
            "username": user.get("username", username),
            "ranking": ranking,
            "reputation": reputation,
            "total": total,
            "easy": easy,
            "medium": medium,
            "hard": hard,
            "rating": rating,
            "contest_rank": contest_rank,
            "top_percentage": top_percentage,
            "contests": contests,
            "total_solved": total,
            "easy_solved": easy,
            "medium_solved": medium,
            "hard_solved": hard,
            "contest_rating": rating,
            "contest_ranking": contest_rank,
            "languages": language_names,
            "language_details": languages,
            "badges": badges
        }

    except Exception:
        return None


# ============================================================
# CODEFORCES PROFILE
# ============================================================

def get_codeforces_profile(username):

    username = username.strip()

    if not username:
        return None

    info_url = (
        "https://codeforces.com/api/user.info"
        f"?handles={username}"
    )

    try:

        response = requests.get(
            info_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=20
        )

        if response.status_code != 200:
            return None

        data = response.json()

        if data.get("status") != "OK":
            return None

        users = data.get(
            "result",
            []
        )

        if not users:
            return None

        user = users[0]

    except Exception:
        return None

    solved_problems = set()

    status_url = (
        "https://codeforces.com/api/user.status"
        f"?handle={username}"
        "&from=1&count=10000"
    )

    try:

        response = requests.get(
            status_url,
            headers={"User-Agent": "Mozilla/5.0"},
            timeout=30
        )

        if response.status_code == 200:

            data = response.json()

            if data.get("status") == "OK":

                submissions = data.get(
                    "result",
                    []
                )

                for submission in submissions:

                    if submission.get(
                        "verdict"
                    ) != "OK":
                        continue

                    problem = submission.get(
                        "problem",
                        {}
                    )

                    contest_id = problem.get(
                        "contestId"
                    )

                    problem_index = problem.get(
                        "index"
                    )

                    if (
                        contest_id is not None
                        and problem_index
                    ):

                        solved_problems.add(
                            (
                                contest_id,
                                problem_index
                            )
                        )

    except Exception:
        pass

    total_solved = len(
        solved_problems
    )

    return {
        "username": user.get(
            "handle",
            username
        ),
        "rating": user.get(
            "rating",
            "N/A"
        ),
        "max_rating": user.get(
            "maxRating",
            "N/A"
        ),
        "rank": user.get(
            "rank",
            "N/A"
        ),
        "max_rank": user.get(
            "maxRank",
            "N/A"
        ),
        "total_solved": total_solved
    }


# ============================================================
# CODECHEF PROFILE
# ============================================================

def get_codechef_profile(username):

    username = username.strip()

    if not username:
        return None

    url = (
        "https://www.codechef.com/users/"
        + username
    )

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/153.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        if response.status_code != 200:
            return None

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

    except Exception:

        return None

    text = soup.get_text(
        " ",
        strip=True
    )

    # --------------------------------------------------------
    # Default values
    # --------------------------------------------------------

    rating = "N/A"
    highest_rating = "N/A"
    global_rank = "N/A"
    country_rank = "N/A"
    total_solved = "N/A"

    # --------------------------------------------------------
    # Rating
    # --------------------------------------------------------

    patterns = [

        r"CodeChef Rating\s*[:\-]?\s*(\d+)",

        r"Rating\s*[:\-]?\s*(\d{3,5})",

        r"Current Rating\s*[:\-]?\s*(\d{3,5})"
    ]

    for pattern in patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            rating = int(
                match.group(1)
            )

            break

    # --------------------------------------------------------
    # Highest rating
    # --------------------------------------------------------

    highest_patterns = [

        r"Highest Rating\s*[:\-]?\s*(\d{3,5})",

        r"highest rating\s*(\d{3,5})"
    ]

    for pattern in highest_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            highest_rating = int(
                match.group(1)
            )

            break

    # --------------------------------------------------------
    # Global rank
    # --------------------------------------------------------

    global_patterns = [

        r"Global Rank\s*[:\-]?\s*([\d,]+)",

        r"Global\s+Rank\s*([\d,]+)"
    ]

    for pattern in global_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            global_rank = int(
                match.group(1).replace(
                    ",",
                    ""
                )
            )

            break

    # --------------------------------------------------------
    # Country rank
    # --------------------------------------------------------

    country_patterns = [

        r"Country Rank\s*[:\-]?\s*([\d,]+)",

        r"Country\s+Rank\s*([\d,]+)"
    ]

    for pattern in country_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            country_rank = int(
                match.group(1).replace(
                    ",",
                    ""
                )
            )

            break

    # --------------------------------------------------------
    # Problems solved
    # --------------------------------------------------------

    solved_patterns = [

        r"Total\s+Problems\s+Solved\s*[:\-]?\s*(\d+)",
        r"Total\s+Problems\s+Solved\s*(\d+)",
        r"Problems\s+Solved\s*[:\-]?\s*(\d+)",
        r"Total\s+Solved\s*[:\-]?\s*(\d+)",
        r"Fully\s+Solved\s*[:\-]?\s*(\d+)",
        r"Fully\s+Solved\s*\(?\s*(\d+)\s*\)?"
    ]
    for pattern in solved_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:

            total_solved = int(
                match.group(1)
            )

            break

    # --------------------------------------------------------
    # Badge extraction
    # --------------------------------------------------------

    badges = []

    badge_patterns = [

        r"(\d+\s*Star\s*Badge)",

        r"([A-Za-z]+\s*Badge)",

        r"(Problem\s*Solver\s*Badge)"
    ]

    for pattern in badge_patterns:

        matches = re.findall(
            pattern,
            text,
            re.IGNORECASE
        )

        for badge in matches:

            badge = badge.strip()

            if (
                badge
                and badge not in badges
                and len(badge) < 80
            ):

                badges.append(
                    badge
                )

    # --------------------------------------------------------
    # Return complete profile
    # --------------------------------------------------------

    return {

        "username": username,

        "profile_url": url,

        "total_solved": total_solved,

        "problems_solved": total_solved,
        "total_problems_solved": total_solved,
        "problem_solved": total_solved,
        "fully_solved": total_solved,
        "solved": total_solved,

        "rating": rating,

        "highest_rating": highest_rating,

        "global_rank": global_rank,

        "country_rank": country_rank,

        "badges": badges
    }