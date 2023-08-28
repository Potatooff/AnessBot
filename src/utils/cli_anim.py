from time import sleep; import functools

"""  Typing effects """
@functools.lru_cache(maxsize=None)
def typing_effect(text:str):
    for char in text:
        print(char, end="", flush=True); sleep(0.05)
    print("\n")
  
