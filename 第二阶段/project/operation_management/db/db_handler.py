import os
from conf import settings
import pickle


def save(obj):
    import os
    from conf import settings
    import pickle
    path_type = os.path.join(settings.BASE_DB, obj.__class__.__name__.lower())
    if not os.path.isdir(path_type):
        os.mkdir(path_type)
    path_obj = os.path.join(path_type, obj.name)
    with open(path_obj, "wb") as f:
        pickle.dump(obj, f)
        f.flush()


def select(name, user_type):
    path_type = os.path.join(settings.BASE_DB, user_type)
    if not os.path.isdir(path_type):
        os.mkdir(path_type)
    path_obj = os.path.join(path_type, name)
    if os.path.exists(path_obj):
        with open(path_obj, "rb") as f:
            return pickle.load(f)
    else:
        return False
