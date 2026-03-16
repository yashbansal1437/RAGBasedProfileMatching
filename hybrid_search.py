def filter_by_skill(results, required_skill):

    filtered = []

    for meta, doc in zip(results["metadatas"][0], results["documents"][0]):

        skills = meta["skills"].split(",")

        if required_skill.lower() in skills:
            filtered.append((meta, doc))

    return filtered
