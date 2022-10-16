import matplotlib.pyplot as plt


class Graphique:
	all = []

	def __init__(self, x_axis, y_axis, xlabel: str, ylabel: str, title: str):
		self.x_axis = x_axis
		self.y_axis = y_axis
		self.xlabel = xlabel
		self.ylabel = ylabel
		self.title = title
		Graphique.all.append(self)

	@classmethod
	def afficher(cls):
		fig, axs = plt.subplots(len(cls.all), constrained_layout = True)

		for graph in Graphique.all:
			if len(cls.all) > 1:
				ax = axs[Graphique.all.index(graph)]
			else:
				ax = axs
			ax.plot(graph.x_axis, graph.y_axis)
			ax.set(title=graph.title, xlabel=graph.xlabel, ylabel=graph.ylabel)

		plt.suptitle('Représentations graphiques des proportions de femelles cistudes dans la population totale',
					 weight = 'bold')
		manager = plt.get_current_fig_manager()
		manager.full_screen_toggle()
		plt.show()
		fig.savefig('plot.png')
