import logging

from dff.core import Context, Actor


logger = logging.getLogger(__name__)
# ....


def example_response(reply: str):
    def example_response_handler(ctx: Context, actor: Actor, *args, **kwargs) -> str:
        return reply

    return example_response_handler


def error_response(reply: str):  # Error_response from bot-persona2-skill
    def error_response_handler(ctx: Context, actor: Actor, *args, **kwargs) -> str:
        return reply
    # logger.info(vars) maybe logger.debug("error_response")
    # state_utils.set_confidence(vars, CONF_SUPER_LOW)
    return error_response_handler("Sorry")


def ontology_info_response(vars):
    try:
        # Temporary case-sensitive
        # utt = state_utils.get_last_human_utterance(vars)["text"].lower()
        utt = state_utils.get_last_human_utterance(vars)["text"]

        # TODO: Search node in Ontology

        response = requests.post(os.environ["GRAPH_DB_URL"] + "/trigger", json={"sentence": utt})
        topic = response.json()["topic"]
        response = response.json()["answer"]

        # response = "Yes, it is my favourite actor!"
        state_utils.set_confidence(vars, confidence=CONF_HIGH)
        state_utils.set_can_continue(vars, continue_flag=CAN_NOT_CONTINUE)

        shared_memory = state_utils.get_shared_memory(vars)
        used_topics = shared_memory.get("used_topics", [])
        state_utils.save_to_shared_memory(vars, used_topics=used_topics + [topic])

        return response
    except Exception as exc:
        logger.info("WTF in ontology_info_response")
        logger.exception(exc)
        state_utils.set_confidence(vars, 0)

        return error_response(vars)


def ontology_detailed_info_response(vars):
    try:
        # Temporary case-sensitive
        # utt = state_utils.get_last_human_utterance(vars)["text"].lower()
        utt = state_utils.get_last_human_utterance(vars)["text"]

        # TODO: Search node in Ontology

        state_utils.set_confidence(vars, confidence=CONF_HIGH)
        state_utils.set_can_continue(vars, continue_flag=CAN_NOT_CONTINUE)

        shared_memory = state_utils.get_shared_memory(vars)
        used_topics = shared_memory.get("used_topics", [])

        topic = used_topics[-1].replace('_', ' ')

        response = requests.post(os.environ["GRAPH_DB_URL"] + "/detailed_trigger", json={"sentence": topic})
        response = response.json()["answer"]

        return response
    except Exception as exc:
        logger.info("WTF in ontology_detailed_info_response")
        logger.exception(exc)
        state_utils.set_confidence(vars, 0)

        return error_response(vars)
