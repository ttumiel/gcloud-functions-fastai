# Set the path to your model
PATH = "data/"


# TEXT GENERATION DEFAULTS
# ========================

# Default words when no data was set
DEFAULT_WORDS = ["the", "a", "there", "when"]

# Number of words per request
N_WORDS = 100

# Generation temperature: smaller value, more conservative
# sentences; larger value, more random sentences
TEMP = 0.75

# Use beam search, with beam size BEAM_SZ
BEAM = False
BEAM_SZ = 30
