import torch
from sklearn.model_selection import train_test_split
import pandas as pd
import chess


if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

df = pd.read_csv("data/archive/chessData.csv")

train_df , test_df = train_test_split(df, test_size=0.2, random_state=42)


