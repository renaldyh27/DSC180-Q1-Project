from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def init_visualization(disease_types, tcga_abbrev):
    """Initialize visualization

    Args:
        disease_types (DataFrame): Disease type one-hot encoded dataFrame
        tcga_abbrev (DataFrame): TCGA abbrevation dataframe

    Returns:
        Figure, axes: Returns figure and axes of the plot
    """
    fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=True)
    
    y_ticks = plt.yticks(np.arange(11)/10)
    x_ticks = plt.xticks(np.arange(1, len(disease_types.columns)+1), [abbreviate(cancer, tcga_abbrev) for cancer in disease_types.columns])

    fig.supylabel('Area Under Curve', fontsize='large')
    plt.autoscale(enable = False, tight=False, axis = 'y')
    ax[0].set_title('AUROC')
    ax[1].set_title('AUPR')
    return fig, ax

def abbreviate(disease_type, tcga_abbrev):
    """Abbreviate given disease/cancer type into TCGA abbreviation

    Args:
        disease_type (String): disease/cancer type name
        tcga_abbrev (DataFrame): Dataframe containing abbreviations of disease/cancer types

    Returns:
        String: Abbreviated disease/cancer type
    """
    abbr = tcga_abbrev.loc[disease_type][0]
    return abbr


def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25, axes=None):
    """Calculate and plot confidence interval

    Args:
        x (int): Position on x axis
        values (List(int)): Data from calculated AUROC/AUPR scores
        z (float, optional): z-value. Defaults to 1.96.
        color (str, optional): Color of line. Defaults to '#2187bb'.
        horizontal_line_width (float, optional): Width of horizontal line. Defaults to 0.25.
        axes (Axes, optional): The axes on which the confidence interval should be plotted. Defaults to None.

    Returns:
        (float, float): Mean and confidence interval of given values
        
    """
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
    """Plot baseline of graph

    Args:
        proportion (float): Proportion of given disease_type in relation to all disease_types
        x (int): location on x-axis
        color (str, optional): Color of baseline. Defaults to '#2187bb'.
        horizontal_line_width (float, optional): Width of horizontal line. Defaults to 0.25.
        axes (Axes, optional): The axes on which the baseline should be plotted. Defaults to None.
    """
    left = x - 0.3 - horizontal_line_width / 2
    right = x + 0.3 + horizontal_line_width / 2
    
    axes.plot([left, right], [proportion, proportion], color=color)

    return

def save_plot_data(data):
    """ Save plot data to csv file

    Args:
        data (dict): keys are dataset names, values are auroc and aupr scores per disease/cancer
        
    """
    
    data = pd.DataFrame(data=data)
    data['Metric'] = ['AUROC', 'AUPR']
    path = './data/out/plot_data.csv'
    data.to_csv(path, index=False)
    
    return path

def plot_model_metrics(plot_data_path, disease_types, tcga_abbrev, dataset_names):
    """Plot the model AUROC/AUPR scores

    Args:
        plot_data_path (String): path of the plot data
        disease_types (DataFrame): One hot encoded disease_type dataframe 
        tcga_abbrev (DataFrame): Dataframe of TCGA abbreviations
    """
    plot_data = pd.read_csv(plot_data_path, index_col='Metric')
    # initialize viz figure
    fig, ax = init_visualization(disease_types, tcga_abbrev)

    colors = ['red','blue','orange']
    offsets = [-0.3, 0, 0.3]

    for color, offset, dataset_name in zip(colors, offsets, plot_data.columns):
        color = color
        offset = offset
        dataset_name = dataset_name

        auroc = eval(plot_data[dataset_name]['AUROC'])
        aupr = eval(plot_data[dataset_name]['AUPR'])

        for i, cancer in enumerate(disease_types.columns, start=1):
            proportion = disease_types[cancer].mean()

            plot_confidence_interval(i+offset, auroc[cancer], color=color, axes=ax[0]) #AUROC plot
            plot_confidence_interval(i+offset, aupr[cancer], color=color, axes=ax[1]) #AUPR plot
            plot_baseline(proportion=proportion, x=i, axes=ax[1]) #AUPR baselines


    ax[0].hlines(0.5, xmin=0, xmax=10, linestyle ='dashed', color = 'black')
    custom_lines = [Line2D([0], [0], color='red'),
                    Line2D([0], [0], color='blue'),
                    Line2D([0], [0], color='orange')]
    plt.legend(labels=dataset_names,
               handles=custom_lines)
    
    plt.savefig('final_figure.png')
    
    return
    

