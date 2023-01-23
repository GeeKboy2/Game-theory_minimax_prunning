import wandb
import random
from othello import *

# start a new wandb run to track this script
wandb.init(
    # set the wandb project where this run will be logged
    project="minimax_othello",
    
    # track hyperparameters and run metadata
    config={
    "learning_rate": 0.02,
    "architecture": "CNN",
    "dataset": "CIFAR-100",
    "epochs": 10,
    }
)

# simulate training
for depth in range(5):
    player1 = MyPlayer("Player1",depth)
    player2 = MyPlayer("Player2",depth)
    game = Othello(8, player1, player2)
    P1_score,P2_score=game.play(verbose=True)

    wandb.log({"min_duration": min(player1.min_duration,player2.min_duration), "depth": depth})


"""
epochs = 10
offset = random.random() / 5
for epoch in range(2, epochs):
    acc = 1 - 2 ** -epoch - random.random() / epoch - offset
    loss = 2 ** -epoch + random.random() / epoch + offset
    
    # log metrics to wandb
    wandb.log({"acc": acc, "loss": loss})
"""
# [optional] finish the wandb run, necessary in notebooks
wandb.finish()