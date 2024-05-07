import streamlit as st
from hbalgo import hba, fun
import numpy as np
import time
import matplotlib.pyplot as plt

rng = np.random.default_rng()

def main():
    st.title("Honey Badger Metaheuristic Optimization Algorithm")
    st.write("This is a simple implementation of the Honey Badger Optimization Algorithm.")
    st.write("You may try various parameters and view how it affects the algorithms fitness value.")
    st.write("This algorithm will attempt to find the value closest to zero in the given search space.")

    pop = st.slider("Population Size", min_value=1, max_value=1000, value=50) # n*m search matrix, this is n
    dim = st.slider("Dimension", min_value=1, max_value=1000, value=20) # n*m search matrix, this is m
    MaxIter = st.slider("Maximum Iterations", min_value=1, max_value=1000, value=600) # total iterations of the algorithm
    fl = st.slider("Lower Bound of values in search space", min_value=-10, max_value=1000, value=-10) # lower bound of values in search array
    ul = st.slider("Upper Bound of values in search space", min_value=-10, max_value=1000, value=10) # upper bound of values in search array
    

    if st.button("Run Algorithm"):
        if fl > ul:
            st.write("Lower bound must be less than upper bound")
        else:
            s = time.time()
            lb = fl*np.ones([dim, 1])
            ub = ul*np.ones([dim, 1])
            GbestScore, GbestPositon, Curve = hba(pop, dim, lb, ub, MaxIter, fun)

            st.write('Lowest fitness score：',GbestScore)
            st.write('Solution for each row：',GbestPositon)

            fig, ax = plt.subplots()
            ax.plot( Curve,color='dodgerblue', marker='o', markeredgecolor='k', markerfacecolor='dodgerblue')

            ax.set_xlabel('Number of Iterations',fontsize=15)
            ax.set_ylabel('Fitness',fontsize=15)
            ax.set_title('Honey Badger Optimization')

            st.pyplot(fig)

            st.write(f"The running time is: {(time.time() - s):.6f} s")

main()