# Calculating MLE and confidence intervals for Caulobacter growth as linear model

# Linear model
def draw_parametric_bs_reps_lin(time, area, m, sigma, size=1):
    """Parametric bootstrap replicates of parameters of
    Normal distribution."""
    bs_reps_k = np.empty(size)
    bs_reps_a_0 = np.empty(size)
    
    for i in range(size):
        bs_sample = np.empty(size)
        for j in range(size):
            bs_sample[j] = np.random.normal(area[j], sigma, size=1)
        bs_reps_k[i], bs_reps_a_0[i], _, _, _ = st.linregress(time, bs_sample)

    return bs_reps_k, bs_reps_a_0

