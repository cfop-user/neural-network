from network import *
from itertools import batched

def main():
	main_network = Network([2,10,10,1])
	batch_size = 4
	data_handler = DataHandler()
	samples = data_handler.read_samples()
	for mini_samples in batched(samples, batch_size):
		for sample in mini_samples:
			main_network.set_input_layer(sample.inputs)
			main_network.feedforward()
			main_network.backpropagate()

main()