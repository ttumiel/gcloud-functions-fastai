from fastai.basic_train import load_learner
from config import PATH, MODEL_NAME, N_WORDS, TEMP, BEAM, BEAM_SZ

learn = load_learner(PATH, MODEL_NAME)

def generate_text(seed_phrase, n=N_WORDS, temp=TEMP, beam=BEAM, beam_sz=BEAM_SZ):
    if beam: return learn.beam_search(seed_phrase, n, temperature=temp, beam_sz=beam_sz)
    return learn.predict(seed_phrase, n, temperature=temp)

def classify_text(text):
    cat, pos, vals = learn.predict(text)
    return {
        "category": str(cat),
        "position": pos.item(),
        "preds": list(vals.numpy().astype('float'))
    }
