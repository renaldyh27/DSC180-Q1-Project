import matplotlib.pyplot as plt
import numpy as np

def abbreviate(string, tcga_abbrev):
    abbr = tcga_abbrev.loc[string][0]
    return abbr

def plot_confidence_interval(x, values, z=1.96, color='#2187bb', horizontal_line_width=0.25):
    mean = np.mean(values)
    stdev = np.std(values)
    confidence_interval = z * stdev / (len(values)**(1/2))

    left = x - horizontal_line_width / 2
    top = mean - confidence_interval
    right = x + horizontal_line_width / 2
    bottom = mean + confidence_interval
    plt.plot([x, x], [top, bottom], color=color)
    plt.plot([left, right], [top, top], color=color)
    plt.plot([left, right], [bottom, bottom], color=color)
    plt.plot(x, mean, 'o', color=color)

    return mean, confidence_interval

def init_visualization(cancer_types):
    ## INITIALIZE PLOT ##
    fig = plt.figure()
    y_ticks = plt.yticks(np.arange(11)/10)
    x_ticks = plt.xticks(np.arange(1, len(cancer_types.columns)+1), [abbreviate(cancer) for cancer in cancer_types.columns])
    plt.autoscale(False)
    title = plt.title('AUROC')
    return