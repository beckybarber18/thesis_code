# thesis_code

All of this code is written in Python, and most of the files are Jupyter Notebooks. To launch the environment: (1) Download the code. (2) Using terminal, ``cd`` into the GitHub directory, and then type ``jupyter notebook.`` The notebook interface will appear in a new browser window or tab.

There are three folders in this GitHub repository: (1) ``auction_simulations``, (2) ``analyze_roasolver_output``, and (3) ``flow_simulations``. We will briefly describe the contents of each.

## ``auction_simulations``

The most important file in this folder is: ``evaluate_2nd_price_grandbundle_integral.ipynb``. This program evaluates the integral that was used to compute the expected revenue of the second-price auction on the grand bundle (of two items). The code graphs the result and finds the closest fit logarithmic and square root functions.

## ``analyze_roasolver_output``

There is only one notebook in this folder: ``analyze_opt_solver_results.ipynb``. This file analyzes the output of RoaSolver over different values of *n*. It plots the result and finds the closest fit logarithmic and square root functions. Note that we only analyze the data for *n* <= 36 because the data for *n* > 36 is unreliable (due to computer overflow). 

## ``flow_simulations``

There are many notebooks in this folder, most of which analyze the output of different flows we derived. The more important files are listed below with descriptions:

* **``diagonal_flow.ipynb:``** Simulates the adjusted revenue that corresponds to the (discrete) pure diagonal flow.
* **``flow_scratch.ipynb:``** This program easily allows you to adjust the virtual value functions (for both the favorite and non-favorite items) to determine which virtual value functions result in a logarithmic upper bound on adjusted revenue.
* **``diag_to_zero_continuous_E[vv2].ipynb:``** Simulates the adjusted revenue that corresponds to the (continuous) flow that terminates at (0,0).
* **``pure_diag_continuous_E[vv2].ipynb:``** Simulates the adjusted revenue that corresponds to the (continuous) pure diagonal flow.
