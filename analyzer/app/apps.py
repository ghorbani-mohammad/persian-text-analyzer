import hazm
from transformers import pipeline
from transformers import AutoTokenizer
from transformers import AutoModelForTokenClassification

from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

    normalizer = hazm.Normalizer()
    model_name_or_path = 'ner_model'
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForTokenClassification.from_pretrained(model_name_or_path)
    ner_model = pipeline('ner', model=model, tokenizer=tokenizer)