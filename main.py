import pandas as pd
import os
import matplotlib.pyplot as plt

df = pd.read_json('deviation.json')
if __name__ == '__main__':
    print(df.describe())
'''
1. Comparison `gt_corners` and `rb_corners`:
    The average value for gt_corners and rb_corners is approximately 4.31
    with a small standard deviation (0.81). This means that on average the model 
    predicts roughly the same number of corners as present in the original data. 
    The standard deviation indicates that the number of corners in the model's predictions 
    does not deviate significantly from the mean. 
    To make sure that model predicts the exact same data, we will compute MAE

2. Deviation evaluation:
    The average deviation values for various dimensions (mean, max, min, floor_mean, 
    floor_max, floor_min, ceiling_mean, ceiling_max, ceiling_min) range from 12.9 to 14.8. 
    This means that on average, deviations from true values are approximately 12-15 degrees

3. Std:
    For some measurements (e.g., mean, max, min), the standard deviation is quite high 
    (ranging from 21.8 to 42.8), indicating significant variability or dispersion in the data. 
    This may suggest the presence of outliers or substantial variability in the model's predictions

Overall, the model likely predicts the total number of corners in rooms well 
(based on the average values of gt_corners and rb_corners), but it has significant 
deviations from the true corner values (based on the average deviation values). 
The standard deviation and high maximum deviation values indicate considerable 
variability in the data and the potential presence of outliers
'''
mae = abs(df['gt_corners'] - df['rb_corners']).mean()
if __name__ == '__main__':
    print(f'MAE: {mae}')
'''
So, MAE being 0 indicates that model does a perfect job of predicting
the data. However, there are some aspects to be considered:
1. Possibility of overfitting:
    Overfitting means that the model has become too specific to the training data 
    and has lost its generalization ability. 
    Evaluate the model's performance on new, previously unseen data 
    to check its generalization ability
2. Test set:
    We don't know if the MAE was calculated on the test set rather than the training set. 
    The model's predictions may be perfect on the training set, but not necessarily on new data
'''

class PlotDrawer:
    def __init__(self):
        pass
    
    def draw_comparison_plot(self, df, column1, column2):
        plt.figure(figsize=(10, 6))
        plt.plot(df[column1], label=column1)
        plt.plot(df[column2], label=column2)
        plt.title(f'Comparison of {column1} and {column2}')
        plt.xlabel('Index')
        plt.ylabel('Value')
        plt.legend()
        plt.grid(True)
        plt.show()

    def save_plot(self, save_path):
        plt.savefig(save_path)
        
def draw_plots(json_file):

    plot_drawer = PlotDrawer()
    
    if not os.path.exists('plots'):
        os.makedirs('plots')
    
    df = pd.read_json(json_file)
    
    plot_paths = []
    
    columns_to_compare = ['gt_corners', 'rb_corners', 'mean', 'max', 'min', 'floor_mean', 'floor_max', 'floor_min', 'ceiling_mean', 'ceiling_max', 'ceiling_min']
    for column1 in columns_to_compare:
        for column2 in columns_to_compare:
            if column1 != column2:
                plot_name = f'plot_{column1}_vs_{column2}.png'
                save_path = os.path.join('plots', plot_name)
                plot_drawer.draw_comparison_plot(df, column1, column2)
                plot_paths.append(save_path)
                plot_drawer.save_plot(save_path)
                
    
    return plot_paths

