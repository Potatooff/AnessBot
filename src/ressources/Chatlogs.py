from string import digits, ascii_letters; import random; from datetime import datetime
import functools; import os


current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = os.path.join(current_dir, "..")
current_dir = os.path.join(current_dir, "..")



@functools.lru_cache(maxsize=None)
def ID_Gen(lenght: int = 6) -> str:
    characters: str = digits + ascii_letters; id = []
    for _ in range(lenght):
        temp: str = random.choice(characters); id.append(temp)
    idStr: str = "".join(id); idStr = f"logs/Aness@{idStr}.txt"
    return idStr

@functools.lru_cache(maxsize=None)
def timee(log_id:str):
    live: str = datetime.now().strftime(f"Date: %Y-%m-%d\tTime: %H:%M:%S\tLogs ID: {log_id}\n\n")
    with open(log_id, "at") as f:
        f.write(live); f.close()

@functools.lru_cache(maxsize=None)
def logsw(log_id:str, input:str, response:str):
    QnA: str = f"{input}\n{response}\n\n"
    with open(log_id, "at") as f:
        f.write(QnA); f.close()


