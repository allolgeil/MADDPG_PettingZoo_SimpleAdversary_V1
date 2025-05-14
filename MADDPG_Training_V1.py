import  torch

device = torch.device("CUDA:0" if torch.cuda.is_available() else "cup")
