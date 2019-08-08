import warnings
from lessons.warning_messages import make_warnings


# ignore with context
with warnings.catch_warnings():
    warnings.filterwarnings("ignore", module=make_warnings.__name__)
    make_warnings.mongodb_warning()
make_warnings.mongodb_warning()


# ignore module warnings
warnings.filterwarnings(
    "ignore",
    module=make_warnings.__name__)

make_warnings.mongodb_warning()


