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

    pop = st.slider("Population Size", min_value=1, max_value=100, value=50)
    MaxIter = st.slider("Maximum Iterations", min_value=50, max_value=1000, value=600)
    dim = st.slider("Dimension", min_value=1, max_value=50, value=20)
    fl = st.slider("Lower Bound for solution", min_value=-10, max_value=1000, value=-10)
    ul = st.slider("Upper Bound for solution", min_value=0, max_value=1000, value=10)
    

    if st.button("Run Algorithm"):
        if fl > ul:
            st.write("Lower bound must be less than upper bound")
        else:
            lb = fl*np.ones([dim, 1])
            ub = ul*np.ones([dim, 1])
            GbestScore, GbestPositon, Curve = hba(pop, dim, lb, ub, MaxIter, fun)

            st.write('The optimal value：',GbestScore)
            st.write('The optimal solution：',GbestPositon)

            fig, ax = plt.subplots()
            ax.plot( Curve,color='dodgerblue', marker='o', markeredgecolor='k', markerfacecolor='dodgerblue')

            ax.set_xlabel('Number of Iterations',fontsize=15)
            ax.set_ylabel('Fitness',fontsize=15)
            ax.set_title('Honey Badger Optimization')

            st.pyplot(fig)

main()