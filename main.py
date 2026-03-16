from resume_rag import build_resume_rag
from job_matcher import match_job


def main():

    print("\nResume RAG System\n")

    print("1. Build Resume Vector Database")
    print("2. Match Job Description")

    choice = input("\nEnter choice: ")

    if choice == "1":
        print("\nProcessing resumes...")
        build_resume_rag()
        print("Vector database created successfully")

    elif choice == "2":

        job_description = input("\nEnter job description:\n")

        results = match_job(job_description)

        print("\nTop Matches:\n")

        for candidate in results["top_matches"]:

            print(f"Candidate: {candidate['candidate_name']}")
            print(f"Score: {candidate['match_score']}")
            print(f"Skills: {candidate['matched_skills']}")
            print(f"Excerpt: {candidate['relevant_excerpts'][0]}")
            print("-" * 40)

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()
