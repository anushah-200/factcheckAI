# Phase 1 -Creating Project Structure

Completed:
- Created GitHub repository
- Added README
- Added requirements.txt
- Created project structure

Next steps:-
- Download TruthfulQA dataset
  

# Phase 2 – Dataset Preparation

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


# Phase 3 – Response Generation Pipeline Setup

## Objectives
- Configure APIs.
- Design response generation workflow.
- Standardize prompting.
  
## Tasks Completed
- ### Finalized evaluation models:
  - ChatGPT-4.1-mini
  - Llama 3.3 (Groq)
  - DeepSeek
- Installed required Python libraries.
- Created the response generation notebook.
- Implemented initial API testing for the selected models.
- Designed a unified response generation pipeline.
- Standardized the evaluation prompt.
- Planned checkpointing and retry mechanisms for long-running experiments.
- DeepSeek API requires a prepaid balance for full evaluation
  
## Decisions
- Store generated responses in a long-format dataset for downstream ML tasks.
  
## Next Steps
- Validate pipeline robustness before running the complete dataset.

# Phase 4-Response Generation Pipeline(OpenAI)

- ## API Verification

The team successfully verified:

 - OpenAI API access
 - Groq API access
 - DeepSeek API access (paid credits available)


- ## Prompt Standardization

To ensure fair comparison across all models, a common prompt template was finalized.

The prompt instructs each model to:

- answer factually,
- avoid speculation,
- explicitly acknowledge uncertainty,
- remain concise.

Identical prompt settings will be used for every model.

- ## Response Generation Pipeline

The team designed a reusable response generation workflow consisting of:

 - dataset loading
 - API wrapper
 - standardized prompting
 - automatic retries
 - checkpoint saving
 - resume capability

This pipeline will be reused for all three models with minimal modifications.

- ## Project Architecture Improvement

To improve maintainability and reproducibility, the project structure was revised.

Reusable functionality will gradually be moved into a dedicated src/ directory.

Planned modules include:

 - prompt management
 - checkpoint management
 - API wrappers
 - evaluation utilities
 - feature engineering

This reduces duplicated notebook code and aligns the repository with software engineering best practices.

- ## Checkpoint Strategy

The team decided that responses will be automatically saved after every successful API call.

Separate checkpoint files will be maintained for each model:

- openai_responses.csv
- groq_responses.csv
- deepseek_responses.csv

This prevents data loss due to Colab session termination or API interruptions.

- ## GitHub Workflow

The team agreed to continue using GitHub for version control.

Major notebook milestones and structural changes will be committed individually with descriptive commit messages.

## Decisions Taken
- Finalized OpenAI, Groq, and DeepSeek as benchmark models.
- Dropped Gemini from the experimental setup.
- Standardized prompting across all models.
- Adopted automatic checkpointing and resume functionality.
- Planned migration of reusable code into a dedicated src/ directory.
- Maintained Google Colab as the primary development environment.

## Tasks Completed  
- Finalized benchmark model selection.
- Designed the OpenAI response generation pipeline.
- Defined standardized prompt template.
- Planned reusable project modules.
- Designed checkpoint and recovery mechanism.
- Updated project architecture.
  
## Tasks for Phase 5
- Implement 02_generate_openai.ipynb.
- Generate responses using the OpenAI model.
- Verify checkpoint recovery.
- Validate generated outputs.
- Prepare equivalent notebooks for Groq and DeepSeek.
