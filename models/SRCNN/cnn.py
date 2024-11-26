from torch import nn

class CNN(nn.Module):
    def __init__(self, scale_factor=8):
        super(CNN, self).__init__()

        self.scale_factor = scale_factor

        self.conv1 = nn.Conv2d(in_channels=3, out_channels=64, kernel_size=9, stride=1, padding=4)
        self.conv2 = nn.Conv2d(in_channels=64, out_channels=32, kernel_size=5, stride=1, padding=2)
        self.conv3 = nn.Conv2d(in_channels=32,out_channels=3, kernel_size=5, stride=1, padding=2)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        x = nn.functional.interpolate(x, scale_factor=self.scale_factor, mode='bicubic', align_corners=False)

        x = self.conv1(x)
        x = self.relu(x)

        x = self.conv2(x)
        x = self.relu(x)

        x = self.conv3(x)
        return x