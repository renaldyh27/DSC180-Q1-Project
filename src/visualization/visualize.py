import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def abbreviate(string, tcga_abbrev):
    abbr = tcga_abbrev.loc[string][0]
    return abbr

def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25, axes=None):
    mean = np.mean(values)
    stdev = np.std(values)
    confidence_interval = z * stdev / (len(values)**(1/2))

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    
    axes.plot([x, x], [top, bottom], color=color)
    axes.plot([left, right], [top, top], color=color)
    axes.plot([left, right], [bottom, bottom], color=color)
    axes.plot(x, mean, '.', color=color)

    return mean, confidence_interval


def plot_baseline(proportion, x, color='#2187bb', horizontal_line_width=0.25, axes=None):
    left = x - 0.3 - horizontal_line_width / 2
    right = x + 0.3 + horizontal_line_width / 2
    
    axes.plot([left, right], [proportion, proportion], color=color)

    return


def init_visualization(cancer_types, tcga_abbrev):
    ## INITIALIZE PLOT ##
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
    
    y_ticks = plt.yticks(np.arange(11)/10)
    x_ticks = plt.xticks(np.arange(1, len(cancer_types.columns)+1), [abbreviate(cancer, tcga_abbrev) for cancer in cancer_types.columns])

    plt.ylabel('Area Under Curve', fontsize='large')
    plt.autoscale(enable = False, tight=False, axis = 'y')
    ax[0].set_title('AUROC')
    ax[1].set_title('AUPR')
    return fig, ax


def save_plot_data(data):
    """Save plot data

    Args:
        data (dict): keys are dataset names, values are auroc and aupr scores per cancer
        
    """
    
    data = pd.DataFrame(data=data)
    data['Metric'] = ['AUROC', 'AUPR']
    path = 'data/out/plot_data.csv'
    data.to_csv(path, index=False)
    
    return path


def plot_model_metrics(plot_data_path, cancer_types, tcga_abbrev):
    ## INITIALIZE PLOT ##
    plot_data = pd.read_csv(plot_data_path, index_col='Metric')
    
    fig, ax = init_visualization(cancer_types, tcga_abbrev)

    colors = ['red','blue','orange']
    offsets = [-0.3, 0, 0.3]

    for color, offset, dataset_name in zip(colors, offsets, plot_data.columns):
        color = color
        offset = offset
        dataset_name = dataset_name

        auroc = eval(plot_data[dataset_name]['AUROC'])
        aupr = eval(plot_data[dataset_name]['AUPR'])

        for i, cancer in enumerate(cancer_types.columns, start=1):
            proportion = cancer_types[cancer].mean()

            plot_confidence_interval(i+offset, auroc[cancer], color=color, axes=ax[0]) #AUROC plot
            plot_confidence_interval(i+offset, aupr[cancer], color=color, axes=ax[1]) #AUPR plot
            plot_baseline(proportion=proportion, x=i, axes=ax[1]) #AUPR baselines


    ax[0].hlines(0.5, xmin=0, xmax=10, linestyle ='dashed', color = 'black')
    custom_lines = [Line2D([0], [0], color='red'),
                    Line2D([0], [0], color='blue'),
                    Line2D([0], [0], color='orange')]
    plt.legend(labels=['Species high coverage','Species ∩ WIS','Species decontaminated'],
               handles=custom_lines)
    
    plt.savefig('final_figure.png')
    
    return
    

