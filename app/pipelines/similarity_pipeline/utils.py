import nltk

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")


def split_text_into_sentences(text: str) -> list[str]:
    """
    Split text into sentences with support for Western and Eastern European languages.

    Supported languages:
    - Western languages: English, French, German, Spanish, Italian, Portuguese
    - Eastern Europe: Ukrainian, Russian, Polish, Czech, Slovak, Hungarian, Romanian, Bulgarian

    Args:
        text: Text to split into sentences

    Returns:
        List of sentences
    """
    if not text or not text.strip():
        return []
    try:
        sentences = nltk.sent_tokenize(text.strip())
    except Exception:
        sentences = _fallback_sentence_split(text.strip())

    cleaned_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and len(sentence) > 1:
            cleaned_sentences.append(sentence)

    return cleaned_sentences


def _fallback_sentence_split(text: str) -> list[str]:
    """
    Fallback method for splitting text into sentences if NLTK fails.
    Supports Eastern European languages with their specific punctuation marks.

    Args:
        text: Text to split

    Returns:
        List of sentences
    """
    import re

    sentence_end_patterns = [
        r"[\n.!:?…]+",
        r'[.!?]+["\']+',
        r"[.!?]+\)+",
        r"[.!?]+\s+[А-ЯA-Z]",
        r"[.!?\n:]+",
    ]
    pattern = "|".join(sentence_end_patterns)
    sentences = re.split(pattern, text)
    cleaned_sentences = []

    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and len(sentence) > 1:
            sentence = re.sub(r"\s+", " ", sentence)
            cleaned_sentences.append(sentence)

    return cleaned_sentences
