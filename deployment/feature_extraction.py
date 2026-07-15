def response_length(response):
    
    return len(response.split())


def question_length(question):
    
    return len(question.split())


def response_characters(response):
    
    return len(response)


def average_word_length(response):
    

    words = response.split()

    if len(words) == 0:
        return 0

    return len(response) / len(words)


def extract_features(
        question,
        response,
        category,
        response_type,
        model_name
):

    features = {

        "Category": category,

        "Type": response_type,

        "Model": model_name,

        "ResponseLength":
            response_length(response),

        "QuestionLength":
            question_length(question),

        "ResponseCharacters":
            response_characters(response),

        "AverageWordLength":
            average_word_length(response)

    }


    return features


