import numpy as np
import matplotlib.pyplot as plt

def surfaceplot(turb_model, commits, formats, fig=None, ax=None):
    results = {}
    for commit in commits:
        filename = turb_model.lower() + "/" + commit + "/surface_flow.csv"
        results[commit] = np.genfromtxt(filename, names=True, delimiter=",")
    if ax is None or fig is None:
        fig, ax = plt.subplots(nrows=2, sharex=True)
    for commit, format_code in zip(commits, formats):
        sorted_indices = np.argsort(results[commit]["Global_Index"])
        ax[0].plot(results[commit]["x_coord"][sorted_indices], results[commit]["Pressure_Coefficient"][sorted_indices], format_code, label=commit)
        ax[1].plot(results[commit]["x_coord"][sorted_indices], results[commit]["Skin_Friction_Coefficient_X"][sorted_indices], format_code, label=commit)
    ax[0].legend(loc="best")
    ax[0].set_ylabel("$C_p$")
    ax[1].set_ylabel("$C_f$")
    ax[-1].set_xlabel("$x$")
    ax[0].set_title(turb_model + " Results")
    fig.set_size_inches(8, 8)
    fig.tight_layout()
    return fig, ax

def histplot(turb_model, commits, formats, fig=None, ax=None):
    history = {}
    for commit in commits:
        filename = turb_model.lower() + "/" + commit + "/history.plt"
        history[commit] = np.genfromtxt(filename, skip_header=3, delimiter=",",
                                        names=("iteration", "density_residual", "energy_residual"),
                                        usecols=[0, 16, 19])
    if fig is None or ax is None:
        fig, ax = plt.subplots()
    for variable in ["density", "energy"]:
        for commit, format_code in zip(commits, formats):
            key = variable + "_residual"
            ax.plot(history[commit]["iteration"][1:], history[commit][key][1:] - history[commit][key][1],
                    format_code, label=(variable + " residual, " + commit))
    ax.legend(loc="best")
    ax.set_ylabel("log10(residual)")
    ax.set_xlabel("Iteration")
    ax.set_title(turb_model + " Convergence History")
    fig.set_size_inches(8, 6)
    fig.tight_layout()
    return fig, ax
