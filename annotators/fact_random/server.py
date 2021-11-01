import logging
import os
import random
import time

from flask import Flask, request, jsonify
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

from common.fact_random import load_fact_file

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)
sentry_sdk.init(dsn=os.getenv("SENTRY_DSN"), integrations=[FlaskIntegration()])

app = Flask(__name__)

FACTS_ANIMALS = load_fact_file("./facts_for_animals.json")
FACTS_CITIES = load_fact_file("./facts_for_cities.json")
FACTS_COUNTRIES = load_fact_file("./facts_for_countries.json")
FACTS_FOOD = load_fact_file("./food_facts.json")
ALL_FACTS = {**FACTS_ANIMALS, **FACTS_CITIES, **FACTS_COUNTRIES, **FACTS_FOOD}


def find_facts(entity_substr_batch):
    facts_list = []
    for entity_substr_list in entity_substr_batch:
        current_facts = []
        for entity_substr in entity_substr_list:
            facts_for_entity = ALL_FACTS.get(entity_substr)
            if facts_for_entity:
                fact = random.choice(facts_for_entity)
                fact_data = {"entity_substr": entity_substr, "fact": fact}
                current_facts.append(fact_data)
        facts_list.append(current_facts)
    return facts_list


@app.route("/respond", methods=["POST"])
def respond():
    st_time = time.time()
    cur_utt = request.json.get("human_sentences", [" "])
    cur_utt = [utt.lstrip("alexa") for utt in cur_utt]

    entity_substr = request.json.get("entity_substr")
    if not entity_substr:
        entity_substr = [[] for _ in cur_utt]

    response = find_facts(entity_substr)

    total_time = time.time() - st_time
    logger.info(f"fact_random exec time: {total_time:.3f}s")
    # returns list of dictionaries for every sample in batch
    # each list contains dictionaries for different entities from user utterance
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=3000)
