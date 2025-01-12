import torch
import os
from torch import nn
import torch.optim as optim

# Define your VAE model
class VariationalAutoEncoder(nn.Module):
    def __init__(self, input_channels=2, input_length=200, h_dim=128, z_dim=20):
        super().__init__()

        # Encoder definition (same as your original code)
        self.encoder = nn.Sequential(
            nn.Conv1d(input_channels, 16, kernel_size=3, stride=2, padding=1), 
            nn.ReLU(),
            nn.Conv1d(16, 32, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
            nn.Conv1d(32, 64, kernel_size=3, stride=2, padding=1),
            nn.ReLU(),
        )
        self.flatten = nn.Flatten()

        # Code (mu, sigma)
        self.fc_mu = nn.Linear(64 * 25, z_dim)
        self.fc_sigma = nn.Linear(64 * 25, z_dim)
        self.fc_z = nn.Linear(z_dim, 64 * 25)

        # Decoder
        self.decoder = nn.Sequential(
            nn.ConvTranspose1d(64, 32, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(32, 16, kernel_size=3, stride=2, padding=1, output_padding=1),
            nn.ReLU(),
            nn.ConvTranspose1d(16, input_channels, kernel_size=3, stride=2, padding=1, output_padding=1),
        )

    def encode(self, x):
        h = self.encoder(x)
        h_flat = self.flatten(h)
        mu = self.fc_mu(h_flat)
        sigma = self.fc_sigma(h_flat)
        return mu, sigma

    def decode(self, z):
        h = self.fc_z(z)
        h = h.view(h.size(0), 64, 25)
        x_reconstructed = self.decoder(h)
        return x_reconstructed

    def forward(self, x):
        mu, sigma = self.encode(x)
        epsilon = torch.randn_like(sigma)
        z_new = mu + sigma * epsilon
        x_reconstructed = self.decode(z_new)
        return x_reconstructed, mu, sigma

# Wrapper class for using the model
class Model:
    def __init__(self):
        self.clf = None

    def load(self):
        # Initialize the model architecture
        self.clf = VariationalAutoEncoder(z_dim=15) 
        
        # Load the saved model weights from a file
        model_weights_path = os.path.join(os.path.dirname(__file__), 'model.pth')  # Path to saved weights
        self.clf.load_state_dict(torch.load(model_weights_path))  # Load model weights
        self.clf.eval()  # Set the model to evaluation mode (important for inference)

    def predict(self, X):
        # Convert input data X to a tensor (if it's not already a tensor)
        X = torch.tensor(X, dtype=torch.float32)
        
        # Make the prediction using the model
        with torch.no_grad():  # No gradient computation needed for inference
            x_reconstructed, mu, sigma = self.clf(X)  # Call the model's forward method
        
        return x_reconstructed  # Return the reconstructed output as the prediction
