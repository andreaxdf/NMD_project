import matplotlib.pyplot as plt
import pandas as pd

FILE_PATH = "../execution_times_more.csv"


# Print the main statistics about the dataset in input
def get_statistics(df: pd.DataFrame):

    grouped_df = df.groupby('Function')

    for group_name, group in grouped_df:
        print(group_name)
        print("Accuracy:  " + str(get_accuracy(group)))
        print("Precision: " + str(get_precision(group)))
        print("Recall:    " + str(get_recall(group)))

# Accuracy: (TP+TN)/TOTAL
def get_accuracy(df: pd.DataFrame):
    total_rows = len(df)
    TP = len(df[(df['Is isomorphic'] == df['Test result'])])
    accuracy = (TP / total_rows) * 100
    return accuracy

# Recall: TP/(TP+FN)
def get_recall(df: pd.DataFrame):
    df = df[df['Test result'] == True]
    TP_FN = len(df)
    TP = len(df[(df['Is isomorphic'] == df['Test result'])])
    recall = (TP / TP_FN) * 100
    return recall

# Precision: TP/(TP+TN)
def get_precision(df: pd.DataFrame):
    df = df[df['Is isomorphic'] == True]
    TP_FP = len(df)
    TP = len(df[(df['Is isomorphic'] == df['Test result'])])
    precision = (TP / TP_FP) * 100
    return precision

def plot_results(df: pd.DataFrame, column: str, only_isomorphic: bool = False):
    if only_isomorphic:
        df = df[df['Is isomorphic'] == True]
        print(df)

    grouped_df = df.groupby("Function")

    # Add labels
    plt.xlabel(column)
    plt.ylabel('Test execution time')
    plt.yscale('log')

    for group_name, group in grouped_df:
        means: pd.Series = group.groupby(column)['Test execution time'].mean()

        plt.plot(means.index, means, label=group_name)

    means: pd.Series = df.groupby(column)['Test execution time'].mean()
    plt.plot(df[column].unique(), means, label='NX test')

    plt.legend()

    plt.show()


result_df = pd.read_csv(FILE_PATH)

# plot_results(result_df, 'Nodes', True)
# plot_results(result_df, 'p', True)

get_statistics(result_df)
