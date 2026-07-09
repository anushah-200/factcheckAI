# Day 1

Completed:
- Created GitHub repository
- Added README
- Added requirements.txt
- Created project structure

Next steps:-
- Download TruthfulQA dataset
  

# Day 2 – Dataset Preparation

## Objectives
- Finalize benchmark dataset.
- Prepare project dataset.
- Organize project structure.

Tasks Completed
- Selected TruthfulQA as the benchmark dataset.
- Explored dataset structure and verified the available columns.
- Analyzed category and question type distributions.
  
- ## Created a processed dataset containing:
- Type
- Category 
- Question
- Ground_Truth
- Saved both raw and processed datasets.
- Set up the project directory structure on Google Drive and GitHub.
  
## Decisions
- Use the processed dataset for all future experiments.
- Use Google Colab for development and GitHub for version control.
  
## Next Steps
-Obtain API keys.
-Begin response generation pipeline.


# Day 3 – Response Generation Pipeline Setup

## Objectives
- Configure APIs.
- Design response generation workflow.
- Standardize prompting.
  
## Tasks Completed
- ### Finalized evaluation models:
  - Google Gemini
  - Llama 3.3 (Groq)
  - DeepSeek
- Installed required Python libraries.
- Created the response generation notebook.
- Implemented initial API testing for the selected models.
- Designed a unified response generation pipeline.
- Standardized the evaluation prompt.
- Planned checkpointing and retry mechanisms for long-running experiments.
- OpenAI API was unavailable due to lack of API credits.
- DeepSeek API requires a prepaid balance for full evaluation
  
## Decisions
- Continue using Gemini and Groq immediately.
- Store generated responses in a long-format dataset for downstream ML tasks.
  
## Next Steps
- Generate responses for the first 100 benchmark questions.
- Validate pipeline robustness before running the complete dataset.
