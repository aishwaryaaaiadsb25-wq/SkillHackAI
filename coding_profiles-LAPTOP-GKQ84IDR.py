import requests


def get_leetcode_profile(username):

    username = username.strip()

    if not username:
        return None

    url = "https://leetcode.com/graphql/"

    query = """
    query userStats($username: String!) {

        allQuestionsCount {
            difficulty
            count
        }

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

    variables = {
        "username": username
    }

    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Referer": "https://leetcode.com/"
    }

    try:

        response = requests.post(
            url,
            json={
                "query": query,
                "variables": variables
            },
            headers=headers,
            timeout=20
        )

        if response.status_code != 200:
            return None

        data = response.json()
        print("LEETCODE RAW DATA:")
        print(data)

        if data.get("errors"):
            return None

        root = data.get("data", {})

        user = root.get("matchedUser")

        if not user:
            return None


        # ============================================
        # SOLVED PROBLEMS
        # ============================================

        easy = 0
        medium = 0
        hard = 0
        total = 0

        stats_data = (
            user
            .get("submitStatsGlobal", {})
            .get("acSubmissionNum", [])
        )

        for item in stats_data:

            difficulty = item.get("difficulty")
            count = item.get("count", 0)

            if difficulty == "All":
                total = int(count)

            elif difficulty == "Easy":
                easy = int(count)

            elif difficulty == "Medium":
                medium = int(count)

            elif difficulty == "Hard":
                hard = int(count)


        # If "All" is missing, calculate total
        if total == 0:

            total = easy + medium + hard


        # ============================================
        # LEETCODE TOTAL AVAILABLE QUESTIONS
        # ============================================

        all_questions = root.get(
            "allQuestionsCount",
            []
        )

        total_available = 0
        easy_available = 0
        medium_available = 0
        hard_available = 0

        for item in all_questions:

            difficulty = item.get("difficulty")
            count = int(item.get("count", 0))

            if difficulty == "All":
                total_available = count

            elif difficulty == "Easy":
                easy_available = count

            elif difficulty == "Medium":
                medium_available = count

            elif difficulty == "Hard":
                hard_available = count


        # ============================================
        # CONTEST INFORMATION
        # ============================================

        contest = root.get(
            "userContestRanking"
        )

        rating = "N/A"
        contest_rank = "N/A"
        top_percentage = "N/A"
        contests = 0

        if contest:

            rating = contest.get(
                "rating",
                "N/A"
            )

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


        # ============================================
        # PROFILE
        # ============================================

        profile = user.get(
            "profile",
            {}
        )

        ranking = profile.get(
            "ranking",
            "N/A"
        )

        reputation = profile.get(
            "reputation",
            0
        )


        # ============================================
        # LANGUAGES
        # ============================================

        languages = []

        language_data = user.get(
            "languageProblemCount",
            []
        )

        for item in language_data:

            language = item.get(
                "languageName"
            )

            problems = item.get(
                "problemsSolved",
                0
            )

            if language:

                languages.append(
                    {
                        "language": language,
                        "problems": int(problems)
                    }
                )


        languages.sort(
            key=lambda x: x["problems"],
            reverse=True
        )


        # ============================================
        # BADGES
        # ============================================

        badges = []

        for badge in user.get(
            "badges",
            []
        ):

            badge_name = badge.get(
                "name"
            )

            if badge_name:

                badges.append(
                    badge_name
                )


        # ============================================
        # FINAL DATA
        # ============================================

        return {

            "username":
                user.get(
                    "username",
                    username
                ),

            "ranking":
                ranking,

            "reputation":
                reputation,

            "total":
                total,

            "easy":
                easy,

            "medium":
                medium,

            "hard":
                hard,

            "total_available":
                total_available,

            "easy_available":
                easy_available,

            "medium_available":
                medium_available,

            "hard_available":
                hard_available,

            "rating":
                rating,

            "contest_rank":
                contest_rank,

            "top_percentage":
                top_percentage,

            "contests":
                contests,

            "languages":
                languages,

            "badges":
                badges
        }


    except Exception as e:

        print(
            "LeetCode API Error:",
            e
        )

        return None



# =========================================================
# CODEFORCES
# =========================================================

def get_codeforces_profile(username):

    username = username.strip()

    if not username:
        return None

    url = (
        "https://codeforces.com/api/user.info"
        f"?handles={username}"
    )

    try:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
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

        return {

            "username":
                user.get(
                    "handle",
                    username
                ),

            "rating":
                user.get(
                    "rating",
                    "N/A"
                ),

            "max_rating":
                user.get(
                    "maxRating",
                    "N/A"
                ),

            "rank":
                user.get(
                    "rank",
                    "N/A"
                ),

            "max_rank":
                user.get(
                    "maxRank",
                    "N/A"
                )
        }


    except Exception:

        return None



# =========================================================
# CODECHEF
# =========================================================

def get_codechef_profile(username):

    username = username.strip()

    if not username:
        return None

    return {

        "username":
            username,

        "profile_url":
            f"https://www.codechef.com/users/{username}"
    }