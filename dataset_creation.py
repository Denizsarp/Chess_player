from torch.utils.data import Dataset, DataLoader
import pandas as pd
import chess
import torch
import numpy as np

class ChessDataset(Dataset):
    def __init__(self, csv_file):
        self.df = pd.read_csv(csv_file)

        self.key_mapping = {
            "p" : 0, "r" : 1, "n" : 2, "b" : 3, "q" : 4, "k" : 5,
            "P" : 6, "R" : 7, "N" : 8, "B" : 9, "Q" : 10, "K" : 11
        }

    def __len__(self):
        return len(self.df)

    def board_to_tensor(self, board):
        input_tensor = torch.zeros(12, 8, 8)
        for square, piece in board.piece_map().items():
            channel = self.key_mapping[piece.symbol()]
            row, col = chess.square_rank(square), chess.square_file(square)
            input_tensor[channel, row, col] = 1.0

        return input_tensor

    def __getitem__(self, index):
        fen = self.df.iloc[index]["FEN"]
        label = self.df.iloc[index]["Evaluation"]

        board = chess.Board(fen)
        tensor = self.board_to_tensor(board)

        try:
            label = float(label) / 1000.0
        except ValueError:
            label = 10.0 if "+" in str(label) else -10.0

        return tensor, torch.tensor([label], dtype=torch.float32)


# How to Use:
# dataset = ChessDataset("chess_evaluations.csv")
# train_loader = DataLoader(dataset, batch_size=64, shuffle=True)