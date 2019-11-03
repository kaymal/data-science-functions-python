# Plot the new correlation matrix
plt.figure(figsize = (10,10))
ax = sns.heatmap(corr.round(1), linewidths=.5, cmap="RdYlGn", annot=True, square=True)
ax.set_title('Correlation Heatmap of Features')
ax.set_ylim(ax.get_ylim()[0].round(), 0) # Required after the last update