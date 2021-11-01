from enum import Enum, auto


class State(Enum):
    USR_START = auto()
    ####################
    # from (scopes.GAMING, USR_CHECK_WITH_USER_GAME_TITLE)
    SYS_USER_WANTS_TO_TALK_ABOUT_MINECRAFT = auto()

    # from SYS_USER_WANTS_TO_TALK_ABOUT_MINECRAFT
    USR_ASK_USER_WHEN_HE_STARTED_TO_PLAY_MINECRAFT = auto()

    # from USR_ASK_USER_WHEN_HE_STARTED_TO_PLAY_MINECRAFT
    SYS_USER_TELLS_WHEN_HE_STARTED_TO_PLAY_MINECRAFT = auto()
    SYS_USER_TELLS_WHEN_HE_STARTED_TO_PLAY_MINECRAFT_AND_NO_HOW_TOS_LEFT = auto()

    # from SYS_USER_TELLS_WHEN_HE_STARTED_TO_PLAY_MINECRAFT
    USR_COMMENT_ON_USER_EXPERIENCE_AND_ASK_IF_USER_WANTS_TO_KNOW_HOW_TO = auto()

    # from SYS_USER_TELLS_WHEN_HE_STARTED_TO_PLAY_MINECRAFT_AND_NO_HOW_TOS_LEFT
    USR_COMMENT_ON_USER_EXPERIENCE_AND_SAY_BUILD_HOGWARTS_PHRASE = auto()

    # from USR_COMMENT_ON_USER_EXPERIENCE_AND_ASK_IF_USER_WANTS_TO_KNOW_HOW_TO
    SYS_USER_DOESNT_WANT_TO_KNOW_HOW_TO = auto()
    SYS_USER_WANTS_TO_KNOW_HOW_TO = auto()

    # from SYS_USER_DOESNT_WANT_KNOW_HOW_TO_DO and USR_ASK_IF_USER_WANTS_TO_KNOW_HOW_TO
    USR_TELL_HOW_TO_AND_ASK_USER_IF_IT_WAS_INTERESTING = auto()

    # from USR_TELL_HOW_TO_AND_ASK_IF_USER_KNEW_IT
    # SYS_USER_WAS_NOT_INTERESTED_BY_HOW_TO = auto()
    # SYS_USER_WAS_INTERESTED_BY_HOW_TO_AND_NO_HOW_TOS_LEFT = auto()
    SYS_BOT_CANNOT_GIVE_MORE_HOW_TOS = auto()
    SYS_BOT_WILL_GIVE_ANOTHER_HOW_TO = auto()
    # SYS_USER_WAS_INTERESTED_BY_HOW_TO_AND_MORE_HOW_TOS_LEFT = auto()

    # from SYS_USER_IS_INTERESTED_1_OR_MORE_HOW_TO_LEFT
    USR_ASK_IF_USER_WANTS_TO_KNOW_HOW_TO = auto()

    # from SYS_USER_IS_NOT_INTERESTED and SYS_USER_IS_INTERESTED_NO_HOW_TOS_LEFT
    USR_TELL_ABOUT_BUILDING_HOGWARTS_IN_MINECRAFT_ASK_WHAT_INTERESTING_USER_BUILT = auto()

    # from USR_TELL_ABOUT_BUILDING_HOGWARTS_IN_MINECRAFT_ASK_WHAT_INTERESTING_USER_BUILT
    SYS_USER_TELLS_ABOUT_HIS_ACHIEVEMENT_IN_MINECRAFT = auto()
    ####################
    SYS_ERR = auto()
    USR_ERR = auto()