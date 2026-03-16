import re

skills_list = [
    "python","sql","machine learning",
    "aws","docker","kubernetes"
]


def extract_metadata(text):

    skills = []

    for skill in skills_list:
        if skill in text.lower():
            skills.append(skill)

    experience_match = re.findall(r"(\d+)\+?\s+years", text.lower())

    experience = max([int(x) for x in experience_match], default=0)

    return {
        "skills": skills,
        "experience": experience
    }
