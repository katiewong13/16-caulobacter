# Calculate MLE and connfidence intervals for Caulobacter growth as an exponential model

def myExp(t, a_0, k):
    '''Define exponential function.'''
    return a_0 * np.exp(k * t)

def draw_parametric_bs_reps_exp(time, area, m, sigma, size=1):
    """Parametric bootstrap replicates of parameters of
    Normal distribution using the exponential model."""
    bs_reps_k = np.empty(size)
    bs_reps_a_0 = np.empty(size)

    for i in range(size):
        bs_sample = np.empty(size)
        for j in range(size):
            bs_sample[j] = np.random.normal(area[j], sigma, size=1)
        vals, _ = so.curve_fit(myExp, time, bs_sample, p0=[-1e-05, -2.88979809e-06])
        bs_reps_k[i] = vals[1]
        bs_reps_a_0[i] = vals[0]
    return bs_reps_k, bs_reps_a_0