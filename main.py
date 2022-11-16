import matplotlib.pyplot as plt


def main():

    # raw data JSON size
    # line 1 points
    x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y1 = [25, 134, 241, 443, 513, 906, 710, 803, 970, 1100]
    y2 = [56, 145, 264, 428, 555, 987, 1289, 1140, 999, 987]
    # plotting the line 1 points
    plt.plot(y1, label="Example 1")
    plt.plot(y2, label="Example 2")
    plt.xlabel('Simulation time (minutes)')
    # Set the y axis label of the current axis.
    plt.ylabel('Data')
    # Set a title of the current axes.
    # plt.title('Number of active IIoT devices during 10-minute simulation')
    # show a legend on the plot
    plt.legend()

    # Show graphs
    plt.show()

if __name__ == "__main__":
    main()

