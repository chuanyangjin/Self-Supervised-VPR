# GLOBAL
NUM_POINTS = 256
GRID_X = 1080
GRID_Y = 1920
SIZED_GRID_X = 64*4
SIZED_GRID_Y = 64
FEATURE_OUTPUT_DIM = 512
RESULTS_FOLDER = "results/"
OUTPUT_FILE = "results/results.txt"
#file_name = "Springhill"

LOG_DIR = 'log/'
MODEL_FILENAME = "model.ckpt"

DATASET_FOLDER = '/mnt/NAS/data/cc_data/2D_RGB_real_full3'

# TRAIN
BATCH_NUM_QUERIES = 2
TRAIN_POSITIVES_PER_QUERY = 2
TRAIN_NEGATIVES_PER_QUERY = 18
DECAY_STEP = 200000
DECAY_RATE = 0.7
BASE_LEARNING_RATE = 0.000005
MOMENTUM = 0.9
OPTIMIZER = 'ADAM'
MAX_EPOCH = 20

MARGIN_1 = 0.5
MARGIN_2 = 0.2

BN_INIT_DECAY = 0.5
BN_DECAY_DECAY_RATE = 0.5
BN_DECAY_CLIP = 0.99

RESUME = False

#scene_names = ['Micanopy','Nimmons','Reyno','Spotswood','Springhill','Stilwell']

TRAIN_FILE = 'generating_queries/train_pickle/training_queries_baseline_0.pickle'
TEST_FILE = 'generating_queries/train_pickle/test_queries_baseline_0.pickle'

# LOSS
LOSS_FUNCTION = 'triplet'
LOSS_LAZY = True
TRIPLET_USE_BEST_POSITIVES = False
LOSS_IGNORE_ZERO_BATCH = False

# EVAL6
EVAL_BATCH_SIZE = 2
EVAL_POSITIVES_PER_QUERY = 4
EVAL_NEGATIVES_PER_QUERY = 12
INIT_TRUST = 100
NEIGHBOR = 10

EVAL_DATABASE_FILE = 'generating_queries/evaluation_database.pickle'
EVAL_QUERY_FILE = 'generating_queries/evaluation_query.pickle'


def cfg_str():
    out_string = ""
    for name in globals():
        if not name.startswith("__") and not name.__contains__("cfg_str"):
            #print(name, "=", globals()[name])
            out_string = out_string + "cfg." + name + \
                "=" + str(globals()[name]) + "\n"
    return out_string
