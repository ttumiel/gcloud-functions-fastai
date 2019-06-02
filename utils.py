from fastai.basic_train import load_learner
from config import path

learn = load_learner(path)

def generate_text(seed_phrase, n=100, temp=0.75, beam=False, beam_sz=1000):
    if beam: return learn.beam_search(seed_phrase, n, temperature=temp, beam_sz=beam_sz)
    return learn.predict(seed_phrase, n, temperature=temp)
