# Model based on convolutional layers, essentially reimplementing DeepSTARR in PyTorch
from typing import Tuple, Any, Optional
import os

import pytorch_lightning as pl

import torch
from torch import nn
from Bio import motifs
import numpy as np


class ConvolutionalClassificationModel(pl.LightningModule):
	def __init__(self, n_celltypes: int, length: int, *, dropout: float = 0.4, activation: str = "relu", dense: int = 256, channels: int = 256, optimizer: str = "", lr: float = 0.01, wd: float = 0.001, label_smoothing: float = 0) -> None:
		"""
		Convolutional model with cross entropy loss and class labels as targets, similar to scBasset
		"""
		super().__init__()
		# Note: optimizer and lr are not used; only for logging
		self.save_hyperparameters()
		self.lr = lr
		self.ls = label_smoothing

		def lu():
			if activation == "relu":
				return nn.ReLU()
			elif activation == "gelu":
				return nn.GELU()
			elif activation == "silu":
				return nn.SiLU()

		self.cnn = nn.Sequential(
			# Input is (batch_size, n_channels=4, length=400)
			nn.Conv1d(in_channels=4, out_channels=channels, kernel_size=7, padding="same"),
			nn.BatchNorm1d(channels),
			lu(),
			nn.MaxPool1d(2),

			nn.Conv1d(in_channels=channels, out_channels=60, kernel_size=3, padding="same"),
			nn.BatchNorm1d(60),
			lu(),
			nn.MaxPool1d(2),

			nn.Conv1d(in_channels=60, out_channels=60, kernel_size=5, padding="same"),
			nn.BatchNorm1d(60),
			lu(),
			nn.MaxPool1d(2),

			nn.Conv1d(in_channels=60, out_channels=120, kernel_size=3, padding="same"),
			nn.BatchNorm1d(120),
			lu(),
			nn.MaxPool1d(2),
			
			nn.Flatten(),

			nn.Linear(length // 16 * 120, dense),  # The division by 16 comes from the four max-pooling layers (2^4 = 16)
			nn.BatchNorm1d(dense),
			lu(),
			nn.Dropout(dropout),
			
			nn.Linear(dense, dense),
			nn.BatchNorm1d(dense),
			lu(),
			nn.Dropout(dropout),

			nn.Linear(dense, n_celltypes),
			nn.Softmax(-1)
		)
		self.loss = nn.CrossEntropyLoss(label_smoothing=self.ls)  # type: ignore


	def forward(self, x: torch.Tensor) -> torch.Tensor:  # type: ignore
		x = x.float()
		return self.cnn(x)

	def training_step(self, batch: Tuple[torch.Tensor, torch.Tensor], batch_idx: int) -> Any:  # type: ignore
		xb, yb = batch
		yb = yb.type(torch.LongTensor).cuda()
		y_pred = self(xb).cuda()
		loss = self.loss(y_pred, yb)
		self.log("loss", loss, prog_bar=True, logger=True, on_step=True, on_epoch=True)
		return loss

	def validation_step(self, batch: Tuple[torch.Tensor, torch.Tensor], batch_idx: int) -> Any:  # type: ignore
		xb, yb = batch
		yb = yb.type(torch.LongTensor).cuda()
		y_pred = self(xb).cuda()
		loss = self.loss(y_pred, yb)
		self.log("validation_loss", loss)
		return loss

	def configure_optimizers(self):
		optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
		return optimizer