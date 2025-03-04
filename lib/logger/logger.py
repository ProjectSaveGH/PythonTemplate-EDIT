from lib.config.loader import CONFIG
#from lib.utils.decorators import deactive

import os
import sys
from datetime import datetime

def _log(msg: str, level: str, printLog: bool = False) -> None:
    os.makedirs(os.path.dirname(CONFIG["paths"]["log_file"]), exist_ok=True)
    
    RST: str = CONFIG["logging"]["colors"]["RESET"]
    lvl: str = level.upper()
    msgp: str = CONFIG["logging"]["format"].replace(r'%(levelname)s', (CONFIG["logging"]["colors"][lvl] + lvl + RST)).replace(r'%(datetime)s', ((' ' * (15 - 4 - len(lvl))) + datetime.now().strftime(CONFIG["logging"]["colors"]["DATETIME"] + CONFIG["logging"]["datetimeFormat"] + RST))).replace(r'%(message)s', (CONFIG["logging"]["colors"]["MESSAGE"] + msg + RST) if level != "critical" else (CONFIG["logging"]["colors"][lvl] + msg + RST))
    msgf: str = CONFIG["logging"]["format"].replace(r'%(levelname)s', lvl).replace(r'%(datetime)s', (' ' * (15 - 4 - len(lvl))) + datetime.now().strftime(CONFIG["logging"]["datetimeFormat"])).replace(r'%(message)s', msg).replace('\u001b[36;1m', '').replace('\u001b[30;1m', '')  + '\n'
    
    with open(CONFIG["paths"]["log_file"], 'a', encoding="utf-8") as f:
        f.write(msgf)
    
    if printLog:
        print(msgp)
    

class Logger:
    def __init__(self, printLog: bool = False) -> None:
        self.printLog = printLog
    
    def debug(self, msg: str) -> None:
        _log(msg, "debug", self.printLog)
    
    def info(self, msg: str) -> None:
        _log(msg, "info", self.printLog)
    
    def warn(self, msg: str) -> None:
        _log(msg, "warn", self.printLog)
    
    def error(self, msg: str) -> None:
        _log(msg, "error", self.printLog)
    
    def critical(self, msg: str, exit: bool = False, exit_code: int = 0) -> None:
        _log(msg, "critical", self.printLog)
        if exit:
            sys.exit(exit_code)
    
    #@deactive("Not Implemented")
    #def errRaise(self, msg: str, trc: str | list[str], trc_type: str, trc_msg: str) -> None:
    #    pass

