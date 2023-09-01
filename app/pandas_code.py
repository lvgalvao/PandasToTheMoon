import pandas as pd

def calculate_statistics(data):
    df = pd.DataFrame(data, columns=['Values'])
    mean = df['Values'].mean()
    median = df['Values'].median()
    mode = df['Values'].mode()[0]
    std = df['Values'].std()
    return mean, median, mode, std
