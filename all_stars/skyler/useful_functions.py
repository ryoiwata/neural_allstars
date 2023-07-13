import numpy as np 
import matplotlib.pyplot as plt
import copy


def raster_plot_2(spike_data, num, *, std:int =2, win_length:int=500, ):
  assert type(win_length) != list
  

  t_bin = 1.2
  ticks = np.arange(0, num)
  if isinstance(win_length,int):
    lower = 0
    upper = win_length
    span = int((upper*t_bin)/60)
  elif isinstance(win_length, tuple):
    lower = win_length[0]
    upper = win_length[1]
    span = (int((lower*t_bin)/60), int((upper*t_bin)/60))
  # else:
  #   raise f"win_length must be of type int or type tuple. Element of type {type(win_length)} was used!"
  subset = copy.deepcopy(spike_data[:num])
  Z = np.nan_to_num(zscore(subset, axis = 1))
  tol = Z.std() * std

  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(10, num*2))
  tmp = np.where(Z>=tol, 1, 0 )
  events = list()
  for row in tmp: 
    events.append(np.argwhere(row>0))
  # print(eventsts.shape)
  # print(tmp.shape)
  for idx, event in enumerate(events):
    ax.eventplot(event, lineoffsets=[idx]* len(event), linelengths= 0.25, colors='k',alpha=0.8,)
  ax.set_yticks(ticks)
  ax.set_yticklabels(np.arange(1,num+1))
  ax.set(title=f"raster of {num} neurons with {std} from {(lower*1.2)/60:.2f} to {(upper*1.2)/60:.2f} mins")
  
  # fig.show()


def plot_activity(spike_data, num, *, win_length:int=500, sep:int = 20):
  assert type(win_length) != list

  t_bin = 1.2
  ticks = np.arange(0, num*sep , sep)
  if isinstance(win_length,int):
    lower = 0
    upper = win_length
    span = int((upper*t_bin)/60)
  elif isinstance(win_length, tuple):
    lower = win_length[0]
    upper = win_length[1]
    span = (int((lower*t_bin)/60), int((upper*t_bin)/60))
  elif win_length == None:
    lower = 0
    upper = spike_data.shape[1]
  # else:
  #   raise f"win_length must be of type int or type tuple. Element of type {type(win_length)} was used!"
  subset = zscore(spike_data[:num],axis=1)
  subset = subset + ticks[:, np.newaxis]
  fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(16, 11))
  ax.plot(np.arange(lower, upper), subset[:, lower:upper].T)
  ax.set_yticks(ticks)
  ax.set_yticklabels(np.arange(1,num+1))
  ax.set(title=f"plot of zscore {num} neurons from {(lower*1.2)/60:.2f} to {(upper*1.2)/60:.2f} mins")
  fig.show()



