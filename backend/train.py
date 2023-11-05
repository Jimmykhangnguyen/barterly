
# import libraries
import tez
import pandas as pd
import numpy as np
from sklearn import model_selection, metrics, preprocessing
import torch
import torch.nn as nn

"""# Load the Dataset"""

class item_mapDataset:
    def __init__(self, users, item_maps, ratings):
        self.users = users
        self.item_maps = item_maps
        self.ratings = ratings

    def __len__(self):
        return len(self.users) # num samples

    def __getitem__(self, item):
        user = self.users[item]
        item_map = self.item_maps[item]
        rating = self.ratings[item]

        return {
            "users": torch.tensor(user, dtype=torch.float),
            "item_maps": torch.tensor(item_map, dtype=torch.float),
            "ratings": torch.tensor(rating, dtype=torch.float),
        }

df = pd.read_csv("data.csv")
df_train, df_valid = model_selection.train_test_split(
        df, test_size=0.2, random_state=42, stratify=df['ratings'].values
)
#type(df.users.values)
#type(df['users'].values)

class recModel(tez.Model):
    def __init__(self, num_users, num_item_maps):
        super().__init__()
        self.user_embed = nn.Embedding(num_users, 32)
        self.item_map_embed = nn.Embedding(num_item_maps, 32)
        self.out = nn.Linear(64, 1) # 32+32, 1 output
        self.step_scheduler_after = "epoch"

    def fetch_optimizer(self):
        opt = torch.optim.Adam(self.parameters(), lr=1e-3)
        return opt

    def fetch_scheduler(self):
        sch = torch.optim.lr_scheduler.StepLR(self.optimizer, step_size=3, gamma=0.7)
        return sch

    def monitor_metrics(self, output, rating):
        output = output.detach().cpu().numpy()
        rating = rating.detach().cpu().numpy()
        return {
            'rmse': np.sqrt(metrics.mean_squared_error(rating, output))
        }

    def forward(self, users, item_maps, ratings=None):
        user_embeds = self.user_embed(users.long())
        item_map_embeds = self.item_map_embed(item_maps.long())
        output = torch.cat([user_embeds, item_map_embeds], dim=1)
        output = self.out(output)

        loss = nn.MSELoss()(output, ratings.view(-1, 1))
        calc_metrics = self.monitor_metrics(output, ratings.view(-1, 1))
        return output, loss, calc_metrics

    # def predict(self, user, item_map):
    #     return self.forward(user, item_map)
    def predict(self, user, item_map):
        user_tensor = torch.tensor([user])
        item_map_tensor = torch.tensor([item_map])
        output, _, _ = self.forward(user_tensor, item_map_tensor)
        return output.item()

def train():
    device = torch.device("cuda")
    df = pd.read_csv("data.csv")

    # users, item_maps, ratings
    lbl_user = preprocessing.LabelEncoder()
    lbl_item_map = preprocessing.LabelEncoder()

    df.users = lbl_user.fit_transform(df['users'].values)
    df.item_maps = lbl_item_map.fit_transform(df['users'].values)

    df_train, df_valid = model_selection.train_test_split(
        df, test_size=0.2, random_state=42, stratify=df.ratings.values
    )

    train_dataset = item_mapDataset(
        users=df_train['users'].values, item_maps=df_train['item_maps'].values, ratings=df_train['ratings'].values
    )

    valid_dataset = item_mapDataset(
        users=df_valid['users'].values, item_maps=df_valid['item_maps'].values, ratings=df_valid['ratings'].values
    )

    model = recModel(num_users=len(lbl_user.classes_), num_item_maps=len(lbl_item_map.classes_)).to(device)
    model.fit(
        train_dataset, valid_dataset, train_bs = 1024,
        valid_bs = 1024, fp16=True
    )

    '''
    # Define input data for prediction
    user_id = 50  # Replace with the user ID you want to predict for
    item_map_id = 19  # Replace with the item map ID you want to predict for

    # Call the predict method to get the model's prediction
    prediction = model.predict(user_id, item_map_id)

    # Print the prediction
    print("Model Prediction:", prediction)'''

train()
print("\ntraining is done!")
