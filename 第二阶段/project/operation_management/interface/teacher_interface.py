from db import models
import os
from conf import settings
from lib import common

logger = common.get_logger("teacher")


def get_all_course():
    path = os.path.join(settings.BASE_DB, "course")
    return common.get_all_dir_obj(path)