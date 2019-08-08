import warnings

def mongodb_warning():
    warnings.warn(
        "MongoClient opened before fork. Create MongoClient only "
        "after forking. See PyMongo's documentation for details: "
        "http://api.mongodb.org/python/current/faq.html#"
        "is-pymongo-fork-safe"
    )
