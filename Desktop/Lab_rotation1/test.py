import numpy as np
import pandas as pd

p_transition = pd.DataFrame(index=range(32),columns=range(32))
p_transition[:] = 0
p_action = pd.DataFrame(index=range(32),columns=range(1,6))
p_action[:] = 0
p_action.iloc[1,4]
d = np.zeros(5)
p_initial = np.zeros(32)
p_initial[0] = 1
d = np.zeros((32,32,5))
d1 = np.copy(d)

reward = np.zeros((5,)) + 0.5
print(reward)