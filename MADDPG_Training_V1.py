import torch
import torch.nn as nn
import numpy as np
import os
import time
from mpe2 import simple_adversary_v3

# Set device
# Set Hyperparameters
# 1 Initialize the Agents
# 1.1 Get obs_dim
# 1.2 Get action_dim
# 2 Main training loop
for episode_i in range(NUM_EPISODE):
    for step_i in range(NUM_STEP):
        # 2.1 Collect actions from all agents
        # 2.2 Execute action
        # 2.3 Store memory
        # 2.4 Update NN_brain every fixed steps
        # 2.4.1 Sample a batch of memories
            # 2.4.1.1 Single + batch
            # 2.4.1.2 Multiple + batch
        # 2.4.2 Update critic and actor
            # 2.4.2.1 Target critic
            # 2.4.2.1 Update critic
            # 2.4.2.1 Update actor
            # 2.4.2.2 Update target critic
            # 2.4.2.1 Update target actor
# 3 Render the env
# 4 Save the agents' models
# 5 plt