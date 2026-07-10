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

# Phase 5 – OpenAI Response Generation Pipeline

## Objectives

- Configure the OpenAI API for automated response generation.
- Develop a robust response generation pipeline.
- Implement checkpointing and resume capability.
- Generate benchmark responses for the TruthfulQA dataset.

## Tasks Completed

- ### Configured the OpenAI API
  - Verified API authentication.
  - Successfully tested the API with sample queries.

- ### Created the OpenAI response generation notebook
  - Developed **02_generate_openai.ipynb**.
  - Installed all required Python libraries.

- ### Loaded the benchmark dataset
  - Imported the processed TruthfulQA dataset.
  - Verified dataset structure and required columns.

- ### Standardized prompting
  - Designed a unified prompt template.
  - Ensured identical prompting strategy for all evaluated models.

- ### Implemented the response generation pipeline
  - Created the **ask_openai()** wrapper function.
  - Added **safe_openai()** with retry logic.
  - Configured deterministic generation settings.

- ### Added fault tolerance
  - Implemented automatic checkpoint saving.
  - Added resume capability for interrupted executions.
  - Configured incremental saving of generated responses.

- ### Validated the pipeline
  - Generated responses for a small subset of questions.
  - Verified output formatting before full-scale execution.

## Decisions

- Use **GPT-4.1-mini** as the OpenAI benchmark model.
- Save responses in **long-format CSV** for downstream evaluation.
- Maintain identical prompting and generation parameters across all models.
- Save progress after every successful API call to prevent data loss.

## Next Steps

- Generate responses for the complete TruthfulQA dataset.
- Implement equivalent pipelines for Groq and DeepSeek.
- Merge responses from all three models.
- Begin automatic response evaluation and feature extraction.


# Phase 6 – Multi-Model Response Generation

## Objectives

- Generate benchmark responses from all selected LLMs.
- Ensure consistent prompting across OpenAI, Groq, and DeepSeek.
- Validate response quality and completeness.
- Prepare response datasets for automatic evaluation.

---

## Tasks Completed

- ### OpenAI Response Generation
  - Generated responses using **GPT-4.1-mini**.
  - Verified checkpointing and resume functionality.
  - Saved responses to **openai_responses.csv**.

- ### Groq Response Generation
  - Created **03_generate_groq.ipynb**.
  - Integrated **Llama-3.3-70B-Versatile** through the Groq API.
  - Implemented retry logic with rate-limit handling.
  - Configured automatic checkpoint saving.
  - Generated responses for the complete TruthfulQA dataset.
  - Saved responses to **groq_responses.csv**.

- ### DeepSeek Response Generation
  - Created **04_generate_deepseek.ipynb**.
  - Integrated the DeepSeek Chat API.
  - Implemented retry and checkpoint mechanisms.
  - Resolved API initialization and client configuration issues.
  - Identified incomplete response generation.
  - Generated responses for the remaining unanswered questions.
  - Saved the finalized responses to **deepseek_responses.csv**.

- ### Pipeline Validation
  - Verified consistent dataset schema across all generated response files.
  - Confirmed standardized prompting for all three evaluated models.
  - Ensured compatibility of generated datasets for downstream evaluation.

---

## Decisions

- Maintain identical prompting strategy and generation parameters across all models to ensure a fair comparison.
- Store responses from each model in separate CSV files before merging.
- Use checkpointing and incremental saving to recover from API interruptions and long-running executions.
- Generate only missing responses when resuming interrupted experiments instead of rerunning the complete dataset.

---

## Next Steps

- Merge OpenAI, Groq, and DeepSeek response datasets.
- Compute evaluation metrics including Semantic Similarity, BLEU, ROUGE, and BERTScore.
- Construct the evaluation dataset for feature engineering.
- Prepare the dataset for hallucination detection model training.


# Phase 7 – Response Evaluation & Feature Engineering

## Objectives

- Merge responses generated by all evaluated LLMs.
- Compute quantitative evaluation metrics for each response.
- Engineer features for hallucination detection.
- Analyze feature distributions before creating hallucination labels.

---

## Tasks Completed

- ### Merged Model Responses
  - Combined OpenAI, Groq, and DeepSeek responses into a unified dataset.
  - Verified dataset consistency and schema across all models.
  - Saved the merged dataset as **merged_responses.csv**.

- ### Implemented Evaluation Metrics
  - Computed **Semantic Similarity** using Sentence Transformers.
  - Computed **BLEU** scores.
  - Computed **ROUGE-1** and **ROUGE-L** scores.
  - Computed **BERTScore** using batch inference.
  - Calculated response length for each generated answer.

- ### Engineered Additional Features
  - Calculated **Ground Truth Length**.
  - Calculated **Question Length**.
  - Calculated **Length Difference** between generated and reference responses.
  - Calculated **Response Character Count**.
  - Calculated **Average Word Length**.

- ### Generated Evaluation Dataset
  - Combined all computed metrics and engineered features into a single dataset.
  - Saved the finalized dataset as **evaluation_dataset.csv**.

- ### Exploratory Metric Analysis
  - Generated descriptive statistics for all evaluation metrics.
  - Visualized metric distributions using histograms.
  - Identified outliers using boxplots.
  - Computed feature correlation matrix.
  - Compared evaluation metrics across different language models.
  - Compared performance across TruthfulQA categories.
  - Identified low-scoring responses as potential hallucination candidates.

---

## Decisions

- Perform exploratory analysis before assigning hallucination labels.
- Avoid using arbitrary similarity thresholds without empirical justification.
- Store evaluation metrics separately from the final machine learning dataset.
- Use quantitative analysis to guide the hallucination labeling strategy.

---

## Next Steps

- Finalize the hallucination labeling methodology.
- Construct the labeled machine learning dataset.
- Perform train-validation-test splitting.
- Train and compare multiple machine learning classifiers.
- Evaluate classifier performance using standard classification metrics.
