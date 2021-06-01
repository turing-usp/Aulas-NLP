import warnings
warnings.simplefilter("ignore")


from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.converters import load_data

training_data = load_data("training_data.json")

pipeline = [
    "nlp_spacy",
    "tokenizer_spacy",
    "ner_crf"
]

config = RasaNLUConfig(cmdline_args={"pipeline": pipeline})

trainer = Trainer(config)
model_directory = trainer.persist('./models/')

print(f"Saving metadata at {model_directory}")
interpreter = trainer.train(training_data)