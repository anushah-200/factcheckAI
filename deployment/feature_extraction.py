import numpy as np

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from rouge_score import rouge_scorer
from bert_score import score
from nltk.translate.bleu_score import sentence_bleu

# Load models once
embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

rouge = rouge_scorer.RougeScorer(
    ["rouge1", "rougeL"],
    use_stemmer=True
)

def semantic_similarity(reference, prediction):

    embeddings = embedding_model.encode(
        [reference, prediction],
        convert_to_numpy=True
    )

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)


def bleu_score(reference, prediction):

    return float(
        sentence_bleu(
            [reference.split()],
            prediction.split()
        )
    )


def rouge_scores(reference, prediction):

    scores = rouge.score(reference, prediction)

    return (
        float(scores["rouge1"].fmeasure),
        float(scores["rougeL"].fmeasure)
    )


def bert_score(reference, prediction):

    P, R, F1 = score(
        [prediction],
        [reference],
        lang="en",
        verbose=False
    )

    return float(F1[0])


def response_length(response):

    return len(response.split())


def ground_truth_length(reference):

    return len(reference.split())


def question_length(question):

    return len(question.split())


def response_characters(response):

    return len(response)


def length_difference(response, reference):

    return abs(
        len(response.split()) -
        len(reference.split())
    )


def average_word_length(response):

    words = response.split()

    if len(words) == 0:
        return 0

    return len(response) / len(words)


def extract_features(question, ground_truth, response):

    similarity = semantic_similarity(
        ground_truth,
        response
    )

    bleu = bleu_score(
        ground_truth,
        response
    )

    rouge1, rougel = rouge_scores(
        ground_truth,
        response
    )

    bert = bert_score(
        ground_truth,
        response
    )

    resp_len = response_length(response)

    gt_len = ground_truth_length(ground_truth)

    ques_len = question_length(question)

    len_diff = length_difference(
        response,
        ground_truth
    )

    resp_chars = response_characters(response)

    avg_word_len = average_word_length(response)

    return {

        "SemanticSimilarity": similarity,

        "BLEU": bleu,

        "ROUGE1": rouge1,

        "ROUGEL": rougel,

        "BERTScore": bert,

        "ResponseLength": resp_len,

        "GroundTruthLength": gt_len,

        "QuestionLength": ques_len,

        "LengthDifference": len_diff,

        "ResponseCharacters": resp_chars,

        "AverageWordLength": avg_word_len

    }


