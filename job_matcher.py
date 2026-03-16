from semantic_search import search
from scoring import compute_score
from config import TOP_K_RESULTS


def match_job(job_description):

    results = search(job_description, TOP_K_RESULTS)

    matches = []

    for doc, meta in zip(results["documents"][0], results["metadatas"][0]):

        score = compute_score(doc, job_description)

        matches.append({
            "candidate_name": meta.get("file"),
            "resume_path": meta.get("file"),
            "match_score": score,
            "matched_skills": meta.get("skills").split(","),
            "relevant_excerpts": [doc[:200]],
            "reasoning": "Skill overlap and semantic similarity"
        })

    matches = sorted(matches, key=lambda x: x["match_score"], reverse=True)

    return {
        "job_description": job_description,
        "top_matches": matches[:10]
    }
