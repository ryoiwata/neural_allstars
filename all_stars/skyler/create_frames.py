# needed libraries
import matplotlib.pyplot as plt
import numpy as np
from joblib import delayed, Parallel

# dat = np.load('stringer_spontaneous.npy', allow_pickle=True).item()
# mask_arr = dat['beh_svd_mask']

dat = np.load("mask_reconstructions.npy", allow_pickle=True)

def save(idx):
    fig, ax = plt.subplots(nrows=1, ncols=1, frameon=False, layout="tight", dpi=100, figsize=(10, 10))
    ax.imshow(dat[:, :, idx])
    ax.set_axis_off()
    name = str(idx).zfill(3)
    try:
        fig.savefig(f'recon_frames/{name}.png')
    except IOError as e:
        print(e)
    finally:
        plt.close()

timeout = 99999
Parallel(n_jobs=4, timeout=timeout)(delayed(save)(idx) for idx in range(0, dat.shape[-1]))

