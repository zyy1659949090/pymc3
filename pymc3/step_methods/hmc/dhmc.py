from .base_hmc import BaseHMC

__all__ = ['DiscontinuousHMC']


class DiscontinuousHMC(BaseHMC):
    R"""A sampler for discrete parameters and likelihoods based on Hamiltonian mechanics.

    A detailed description can be found at [1], "Discontinuous Hamiltonian Monte Carlo for 
    sampling discrete parameters".
    
    References
    ----------
    .. [1] Nishimura, A., Dunson, D., and Lu, J. 2017. Discontinuous Hamiltonian Monte Carlo 
    for sampling discrete parameters. arXiv:1705.08510.
    """
    pass