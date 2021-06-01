import pandas as pd
import json

database = pd.read_csv("zomato.csv")
database = database[:150]
cuisines = database['cuisines']
cuisines = [c.split() for c in cuisines]
cuisines_classes = []
for c in cuisines:
    for i in c:
        if i not in cuisines_classes:
            cuisines_classes.append(str(i).replace(",",""))

#generate phrases with sinom_prices specification
sinom_prices_1 = {'high-price': ['fancy', 'expensive', 'chic'], 
                'low-price': ['cheap', 'low-price'], 
                'average-price': ['not too expensive nor cheap', 'ok price']}

find_restaurant_price_1 = ["I'd like to eat at a {0} restaurant", "I wanna go to a {0} restaurant",
                         "I'm looking for a {0} restaurant", "Find me a {0} place",
                          "I'd like to go to a {0} place to eat"]

sinom_prices_2 = {'low-price': ['little', 'not much'], 
                'high-price': ['plenty', 'more than enough']}

find_restaurant_price_2 = ["Find me a place to eat! I have {0} money!", 
                           "I'd like to go a place having {0} to spend"]

#generate phrases with cousine specification
cuisines_classes = set(cuisines_classes)
cuisines_classes.remove("Food")
sinom_cuisines = dict.fromkeys(cuisines_classes, 0)
for key in sinom_cuisines.keys():
    sinom_cuisines[key] = key

find_restaurant_cousine = ["I'd like to go to a {0} place!", "I wanna have some {0} food today!",
                          "Find me {0} places", "Some {0} food would be great", 
                           "I was thinking about going to a {0} place", "Do you know about any good {0} place?",
                          "I want to go to a {0} restaurant", "Are there any {0} restaurants out there?"]

#generate phrases with cousine & price specification
find_restaurant_cousine_price_1 = ["I'd like to go to a {0} {1} restaurant", 
                                 "I want to have some {1} food at a {0} place",
                                "Help me find a {0} restaurant to eat {1} food"]

find_restaurant_cousine_price_2 = ["Find me a {1} place to eat! I have {0} money!", 
                           "I'd like to go a {1} place having {0} to spend"]

train_dict = {"rasa_nlu_data": {
        "common_examples": [],
        "regex_features": [],
        "entity_synonyms": []
    }
}

def one_entity_add(phrases, subs, ent, train_dict):
    for phrase in phrases:
        for label, terms_list in subs.items():
            if isinstance(terms_list, list):
                for term in terms_list:
                    text_with_term = phrase.format(term)
                    start = text_with_term.find(term)
                    end = start + len(term)
                    if ent == "price":
                        ent = label
                    entities = [{"start": start, "end": end, "value": label, "entity": ent}]
                    example = {"intent": "find_restaurant", "entities": entities, "text": text_with_term}
                    train_dict["rasa_nlu_data"]["common_examples"].append(example)
            else:
                term = terms_list
                text_with_term = phrase.format(term)
                start = text_with_term.find(term)
                end = start + len(term)
                if ent == "price":
                    ent = label
                entities = [{"start": start, "end": end, "value": label, "entity": ent}]
                example = {"intent": "find_restaurant", "entities": entities, "text": text_with_term}
                train_dict["rasa_nlu_data"]["common_examples"].append(example)
                
    return train_dict

def two_entity_add(phrases, subs1, ent1, subs2, ent2, train_dict):
    for phrase in phrases:
        for label1, terms_list_1 in subs1.items():
            for term_1 in terms_list_1:
                for label2, term_2 in subs2.items():
                    text_with_term = phrase.format(term_1, term_2)
                    start1 = text_with_term.find(term_1)
                    end1 = start1 + len(term_1)
                    start2= text_with_term.find(term_2)
                    end2= start2 + len(term_2)
                    ent1 = label1
                    print(ent1)
                    entities = [{"start": start1, "end": end1, "value": label1, "entity": ent1},
                                       {"start": start2, "end": end2, "value": label2, "entity": ent2}]
                    example = {"intent": "find_restaurant", "entities": entities, "text": text_with_term}
                    train_dict["rasa_nlu_data"]["common_examples"].append(example)
                
    return train_dict

one_entity_combinations = [(find_restaurant_price_1, sinom_prices_1, "price"),
                          (find_restaurant_price_2, sinom_prices_2, "price"),
                          (find_restaurant_cousine,sinom_cuisines, "cousine")]

two_entity_combinations = [(find_restaurant_cousine_price_1, sinom_prices_1, "price", sinom_cuisines, "cousine"),
                          (find_restaurant_cousine_price_2, sinom_prices_2, "price", sinom_cuisines, "cousine")]

for phrases, subs, ent in one_entity_combinations:    
    train_dict = one_entity_add(phrases, subs, ent, train_dict)
    
for phrases, subs1, ent1, subs2, ent2 in two_entity_combinations:
    train_dict = two_entity_add(phrases, subs1, ent1, subs2, ent2, train_dict)

genraL_find_restaurant_intetion = ('find_restaurant', ["Find me a place to eat!", "I wanna go out for dinner",
                                "I wanna eat out", "Are there any good places to eat out here?", "I wanna go to a restaurant",
                                "Please find me a restaurant", "I wanna go to a restaurant with some friends today",
                                "I want to eat alone at a restaurant"])
greet_intetion = ('greet', ['Olá', 'Oi', 'Tudo bom?', 'Tranquilo?', "Eai", "De boa?", "Fala!", "Boa tarde", 
                  "Boa noite", "Bom dia", "Oie", "Ois"])
thankyou_intention = ('thankyou', ['Vlw', "Boa", "Obrigada", "Obrigado", "Valeu!", "Brigada", "Brigado"])

def add_intention(intent, list_inte, train_dict):
    for phrase in list_inte:
        example = {"intent": intent, "text": phrase}
        train_dict["rasa_nlu_data"]["common_examples"].append(example)
    return train_dict

for intent, list_inte in [greet_intetion, thankyou_intention]:
    train_dict = add_intention(intent, list_inte, train_dict)

with open('training_data.json', 'w') as outfile:
    json.dump(train_dict, outfile)     