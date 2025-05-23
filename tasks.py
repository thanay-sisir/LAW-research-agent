from crewai import Task
from agents import  old_property_researcher, property_researcher, property_analyst
# from pydantic import BaseModel
# class ResearchOutput(BaseModel):
#     market_analysis_summary: str
#     recommended_properties: list[str]
#     financial_projections: dict
#     risk_assessment: str
#     recommendations: str



# legal_research_extraction_task



research_task = Task(
    description="""
You are tasked with conducting comprehensive, high-quality legal research on topic-"rape cases happend in 2024" in India. 
Use only validated legal sources such as:
- Government law portals (e.g., India Code, eCourts, Supreme Court website)
- Law Commission reports
- Law journals (e.g., SCC Online, Manupatra, JILI)
- University legal repositories
- Official gazettes and statutory databases, collect all these based on topic given strictly.

The research must include:
1. Accurate citation of all extracted laws, judgments, or opinions with full source URLs or legal citation format (e.g., AIR, SCC, CriLJ).
2. Extraction of statutes, judicial interpretations, or landmark case principles relevant to the topic.
3. Identification of the legal issue’s jurisdictional scope (state vs. central).
4. If the issue spans multiple laws (e.g., Constitution + IPC), reflect that in output.
5. Validation of source authenticity and current applicability (ensure it's not overruled or repealed).
6. Summary in plain language for law students, without altering legal essence. All these should be strictly mandatory on given topic.

Deliverable: A clean and validated legal content pack (plain English summary + citations).
""",
    expected_output="""A structured report containing:
- List of key statutes and provisions (with citations)
- Summarized landmark judgments (facts + holdings)
- Key legal principles and rules
- Cross-reference links to official/legal sources
- Student-friendly plain-English explanation of each point, all on only of given topic
""",
    agent=old_property_researcher,
    # output_file="legal_research_extracted.txt" ---> this no need I commented out wantedly
)












# 2nd old research task experimetn

# agetn  2:legal_case_statute_analysis_task

old_research_task = Task(
    description="""
Analyze the extracted legal data and transform it into structured, doctrinal insights for law students on only strictly given {topic}.

You must:
1. Identify and explain the legal issues, rules, application, and conclusions (IRAC format).
2. Clarify precedent value (e.g., binding vs persuasive).
3. Compare and contrast majority vs dissenting opinions (if available).
4. Show how judicial interpretation evolved on this topic
 (chronologically with specific court location name, person case handled by, anty dates only if available).
5. Highlight any overruled judgments, repealed sections, or constitutional amendments impacting,related to only strictly given {topic}
6. Structure the content clearly for law students preparing for moot court, exams, or internships.

Deliverable: Well-organized legal analysis formatted for academic or practical legal use.
""",
    expected_output="""An academic-style document containing:
- Legal issue identification
- Case law interpretation
- Statutory application and exceptions
- Majority vs dissenting opinion comparisons
- Cross-reference to Indian legal doctrines
""",
    agent=property_researcher,
    output_file="legal_analysis_output.txt"
)





# legal_memo_drafting_task


analysis_task = Task(
    description="""
Use the previously analyzed legal content to draft a legally sound and academically rigorous research memo. 

The memo should:
1. Follow IRAC structure for all legal issues.
2. Include citations in standard format (AIR, SCC, or Act name + Section + Year).
3. Synthesize reasoning logically and coherently.
4. Reflect understanding of real-world application (where applicable).
5. Be written at a level suited for Indian law students or junior legal professionals.
6. Include flags where information is uncertain or open to interpretation.

Deliverable: A full memo with clear issue framing, legal reasoning, case references, and plain English conclusions.
""",
    expected_output="""A legal research memo including:
- Issue breakdown in IRAC format
- Authoritative citations (statutes + cases)
- Coherent argument with referenced precedent
- Concise conclusion for each legal issue
- Notes on assumptions or legal uncertainties
""",
    agent=property_analyst,
    output_file="legal_memo_output_final.txt"
)
