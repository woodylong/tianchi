import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
uactions=['user_id','song_id','gmt_create','action_type','ds']
songs=['song_id','artist_id','pulish_time','song_init_plays','language','gender']
predicts=['artist_id','plays','ds']
song=pd.read_csv('D:/mars_tianchi_songs.csv',header=None,names=songs)
