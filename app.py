from structlog import wrap_logger, PrintLogger
from structlog.processors import JSONRenderer
from random import randint
from datetime import datetime

log = wrap_logger(PrintLogger(), processors=[JSONRenderer()])

counter = 0
limit   = 1000

while counter < limit:
	current_time = datetime.utcnow()
	log.info("login", user_id=randint(1, 1000), timestamp=current_time.isoformat())