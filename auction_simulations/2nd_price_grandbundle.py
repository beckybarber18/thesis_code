#!/usr/bin/env python

#-----------------------------------------------------------------------
# 2nd_price_grandbundle.py
# Author: Rebecca Barber
# 
# 2nd price auction on grand bundle (2 items)
#-----------------------------------------------------------------------

import scipy.stats as st
from statistics import *
import matplotlib.pyplot as plt
from sys import argv
import numpy as np
from math import *
import pandas as pd
from plotnine import *
from random import * 

# draws value from ER curve
def er_draw():
	q = random()
	return 1/(1-q)

# draws m values from the ER curve
# truncate the ER curve at T
# so if the value we draw is > T, set it = T
def draw_vals(m):
	vals = []
	for i in range(m):
		draw = er_draw()
		vals.append(draw)	
	return vals

# generates revenue for 2nd price auction of grand bundle
# given n bidders and m itemss 
def auction_rev(n, m, trial):

	# start w/ T = n^3, this could change
	T = np.power(n, 3)
	# for each bidder, stores their value of the grand bundle
	bidder_bundle_vals = []

	# for each bidder, draw values for each item
	for i in range(n):
		bundle_val = sum(draw_vals(m))
		# start w/ T = n^3, this could change
		if bundle_val > T: 
			bundle_val = T
			print('truncating on trial', trial)
		bidder_bundle_vals.append(bundle_val)

	# sort the array
	bidder_bundle_vals = sorted(bidder_bundle_vals, reverse = True)
	return float(bidder_bundle_vals[0]), float(bidder_bundle_vals[1])

def main(argv):

	num_trials = 100000
	min_bidders = 100
	max_bidders = 200
	num_items = 2

	figure_name = './figures/2nd_price_' + str(min_bidders) + 'to' + \
		str(max_bidders) + 'bidders_' + str(num_trials) + 'trials.png'

	csv_file = './data/2nd_price_' + str(min_bidders) + 'to' + \
		str(max_bidders) + 'bidders_' + str(num_trials) + 'trials.csv'

	num_bidders = []
	for i in range(min_bidders, max_bidders+1):
		num_bidders.append(i)

	avg_revs_over_n = []
	avg_highest_bid_over_n = []
	for n in range(min_bidders, max_bidders+1):
		print('number of bidders:', n)

		# run num_trials for each # of bidders so we can 
		# take the average
		all_revs = []
		highest_bids = []
		for i in range(num_trials):
			highest_bid, second_highest = auction_rev(n, num_items, i)
			all_revs.append(second_highest)
			highest_bids.append(highest_bid)

		avg_rev = mean(all_revs)
		avg_revs_over_n.append(avg_rev)
		avg_highest_bid = mean(highest_bids)
		avg_highest_bid_over_n.append(avg_highest_bid)

	# save all of the data
	df = pd.DataFrame(columns=['num bidders', 'avg rev', 'avg highest bid'])
	for i in range(len(num_bidders)):
		n = num_bidders[i]
		avg_rev = avg_revs_over_n[i]
		avg_highest = avg_highest_bid_over_n[i]
		df = df.append({'num bidders': n, 'avg rev': avg_rev, 
			'avg highest bid': avg_highest}, ignore_index=True)

	df.to_csv(csv_file)

	# make dataframe for plotting
	rev_df = pd.DataFrame(columns=['num bidders', 'avg rev', 'Legend'])
	for i in range(len(num_bidders)):
		n = num_bidders[i]
		avg_rev = avg_revs_over_n[i]
		# not totally sure what to do with constants here? and if I 
		# should have the m * n part
		# from appendix A
		sqrt_benchmark = num_items * n + num_items * sqrt(num_items * num_items)
		# from appendix B
		log_benchmark = num_items * n + np.log(n)

		rev_df = rev_df.append({'num bidders': n, 'avg rev': avg_rev, 'Legend': 'Simulation'}, 
				ignore_index=True)
		rev_df = rev_df.append({'num bidders': n, 'avg rev': sqrt_benchmark, 'Legend': 'nm + m * sqrt(nm)'}, 
				ignore_index=True)
		rev_df = rev_df.append({'num bidders': n, 'avg rev': log_benchmark, 'Legend': 'nm + ln(n)'}, 
				ignore_index=True)

	# make the plot
	plt1 = ggplot(aes(x='num bidders', y = 'avg rev', color = 'Legend', group = 'Legend'), data=rev_df) + \
		geom_line() +\
		theme(axis_text_x = element_text(color = 'black'), axis_text_y = element_text(color = 'black')) + \
		labs(x="Number of Bidders", y="Average Revenue", title = "Second Price Auction on Grand Bundle (m = 2)") 

	ggsave(filename=figure_name,
       plot=plt1,
       device='png', dpi = 200)

if __name__ == '__main__':
	main(argv)

