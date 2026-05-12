import chess
import torch
import numpy as np

board = chess.Board()

key_mapping = {
        "p" : 0,
        "r" : 1,
        "n" : 2,
        "b" : 3,
        "q" : 4,
        "k" : 5,
        "P" : 6,
        "R" : 7,
        "N" : 8,
        "B" : 9,
        "Q" : 10,
        "K" : 11,
}

input_tensor = torch.zeros(12,8,8)

for square, piece in board.piece_map().items():

        target_channel = key_mapping[piece.symbol()]
        row = chess.square_rank(square)
        column = chess.square_file(square)
        input_tensor[target_channel,row,column] = 1.0

input_tensor = input_tensor.unsqueeze(0)



