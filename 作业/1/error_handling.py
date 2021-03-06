import logging
from time import sleep


def handle(re_raise = True, log_traceback = True, exc_type= Exception, tries = 1, delay = 0, backoff = 1):
    def log_de(f):
        def wra(*args, **kw):
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logger = logging.getLogger(__name__)
            if log_traceback == True:
                logger.info("Start  log")
            exc_info =""
            for k in range(tries):
                exc_info = ""
                try:
                    return f(*args, **kw)
                except exc_type as e:
                    if log_traceback == True:
                        logger.error(repr(e))
                    exc_info = repr(e)
                sleep(delay*backoff)
            if re_raise == True and exc_info !="":
                print(exc_info)
        return wra
    return log_de
 

import random
@handle ( re_raise =True , tries =3 , delay =0.5 , backoff =2 )
def some_function ():
    if random.random()<0.75: x = 1 / 0 # ZeroDivisionError
some_function ()
 
