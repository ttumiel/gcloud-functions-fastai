from fastai.basic_train import load_learner
from config import PATH, N_WORDS, TEMP, BEAM, BEAM_SZ

learn = load_learner(PATH)

def generate_text(seed_phrase, n=N_WORDS, temp=TEMP, beam=BEAM, beam_sz=BEAM_SZ):
    if beam: return learn.beam_search(seed_phrase, n, temperature=temp, beam_sz=beam_sz)
    return learn.predict(seed_phrase, n, temperature=temp)
