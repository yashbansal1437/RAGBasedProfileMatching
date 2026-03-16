def compute_score(resume_text, job_description):

    jd_words = set(job_description.lower().split())
    resume_words = set(resume_text.lower().split())

    overlap = len(jd_words.intersection(resume_words))

    score = min(100, overlap * 2)

    return score
