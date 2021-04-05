from typing import Optional

import torch
import torch.nn as nn
from torch import Tensor


class ArcFaceLoss(nn.Module):
    """ArcFace: Additive Angular Margin Loss.
    
    - Reference:
    [ArcFace: Additive Angular Margin Loss for Deep Face Recognition](
        https://arxiv.org/abs/1801.07698)
    [Additive Angular Margin Loss](
        https://paperswithcode.com/method/arcface)
    """

    def __init__(
        self,
        in_features: int,
        out_features: int,
        s: Optional[float] = 30.0,
        m: Optional[float] = 0.5,
        easy_margin=False,
    ):
        super(ArcFaceLoss, self).__init__()

    def forward(self, input: Tensor, target: Tensor) -> Tensor:
        return
