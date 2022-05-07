import hazm
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification

from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"
    try:
        # normalizer
        normalizer = hazm.Normalizer()
        # ner
        tokenizer = AutoTokenizer.from_pretrained("/app/analyzer/ner_model")
        model = AutoModelForTokenClassification.from_pretrained(
            "/app/analyzer/ner_model"
        )
        ner_model = pipeline("ner", model=model, tokenizer=tokenizer)
        # sentiment
        sentiment_model = pipeline(
            "sentiment-analysis", model="/app/analyzer/sentiment_model"
        )
        # classification
        classification_model = pipeline(
            "text-classification", "/app/analyzer/classification_model"
        )
    except:
        print("Error in loading models")
