import numpy as np
import matplotlib.pyplot as plt

def plot_confusion_matrix(cm, classes, title=None, cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)

    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           ylabel='True label',
           xlabel='Predicted label')

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = '.2f'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

# Label for simulation
simulation_label = 1

# Loading confusion table
confusion_table = np.load('./outputs/confusion/' + str(simulation_label) + '/confusion_table.npy')

# Defining array of thresholds from 0 to 1 to consider in the ROC curve
thresholds_points = 101
thresholds = np.linspace(0, 1, num=thresholds_points)

# false/true positive/negative rates
fp_rate = []
tp_rate = []
fn_rate = []
tn_rate = []

# Creating rates
for i in range(thresholds_points):
    fp_rate.append(confusion_table[i, 0, 1] / (confusion_table[i, 0, 1] + confusion_table[i, 0, 0]))
    tp_rate.append(confusion_table[i, 1, 1] / (confusion_table[i, 1, 1] + confusion_table[i, 1, 0]))

    fn_rate.append(confusion_table[i, 1, 0] / (confusion_table[i, 1, 1] + confusion_table[i, 1, 0]))
    tn_rate.append(confusion_table[i, 0, 0] / (confusion_table[i, 0, 0] + confusion_table[i, 0, 1]))

# Distance of each threshold from ideal point at (0, 1)
distance_from_ideal = (np.array(tn_rate) - 1)**2 + (np.array(fn_rate) - 0)**2

# Threshold closest to (0, 1)
closest_threshold = np.argmin(distance_from_ideal)

# Area under ROC curve
area_under_curve = np.trapz(np.sort(tn_rate), x=np.sort(fn_rate))

print("Area under ROC curve: " + str(area_under_curve))
print("Closest threshold to optimal ROC: " + str(thresholds[closest_threshold]))

# Plotting ROC curve
straight_line = np.linspace(0, 1, 1001)

plt.gcf().subplots_adjust(bottom=0.15)
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', serif='New Century Schoolbook')
plt.gcf().subplots_adjust(bottom=0.15)
plt.plot(fn_rate, tn_rate, color='#056eee', linewidth=2.2)
plt.plot(straight_line, straight_line, color='#070d0d', linewidth=1.5, dashes=[6, 2])
plt.plot(0.0, 1.0, 'ko')
plt.plot(fn_rate[closest_threshold], tn_rate[closest_threshold], 'k^')
plt.ylim(-0.05, 1.05)
plt.xlim(-0.05, 1.05)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.xlabel('False negative rate', fontsize=15)
plt.ylabel('True negative rate', fontsize=15)
plt.tick_params(axis='both', which='major', labelsize=14, length=6, width=1)
plt.tick_params(axis='both', which='minor', labelsize=14, length=6, width=1)
plt.savefig('./roc.pdf')
plt.close()

# Selecting ideal confusion table and plotting
confusion_table_ideal = confusion_table[closest_threshold]

plt.figure()
plot_confusion_matrix.plot_confusion_matrix(confusion_table_ideal, classes=['Genuine', 'Fraudulent'], title='')

plt.savefig('./confusion.pdf')
