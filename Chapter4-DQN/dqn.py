import argparse
import time
from wrappers import build_env
from config import *
from utils import *


parser = argparse.ArgumentParser()
parser.add_argument('--seed', help='raandom seed', type=int, default=0)
args = parser.parse_args()

random.seed(args.seed)
np.random.seed(args.seed)
tf.random.set_seed(args.seed)  # reproducible

env = build_env(env_id, seed=args.seed)
in_dim = env.observation_space.shape
action_dim = env.action_space.n


############################### Network ################################
class QFunc(tf.keras.Model):
    