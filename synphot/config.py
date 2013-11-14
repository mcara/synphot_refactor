# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""Synphot configurable items.

The default configuration heavily depends on STScI CDBS structure
but it can be easily re-configured as the user wishes via
`astropy.config`.

"""
from __future__ import division, print_function

# STDLIB
import os

# ASTROPY
from astropy.config.configuration import ConfigurationItem


__all__ = ['STDSTAR_DIR', 'VEGA_FILE', 'EXTINCTION_DIR', 'LMC30DOR_FILE',
           'LMCAVG_FILE', 'MWAVG_FILE', 'MWDENSE_FILE', 'MWRV21_FILE',
           'MWRV40_FILE', 'SMCBAR_FILE', 'XGAL_FILE', 'PASSBAND_DIR',
           'BESSEL_H_FILE', 'BESSEL_J_FILE', 'BESSEL_K_FILE', 'set_files']

# STANDARD STARS
STDSTAR_DIR = ConfigurationItem(
    'stdstar_dir', 'ftp://ftp.stsci.edu/cdbs/current_calspec/',
    'Location of standard star spectra.')
VEGA_FILE = ConfigurationItem(
    'vega_file', os.path.join(STDSTAR_DIR(), 'alpha_lyr_stis_005.fits'), 'Vega')

# REDDENING/EXTINCTION LAWS
EXTINCTION_DIR = ConfigurationItem(
    'extinction_dir', 'ftp://ftp.stsci.edu/cdbs/extinction/',
    'Location of extinction files.')
LMC30DOR_FILE = ConfigurationItem(
    'lmc30dor_file', os.path.join(EXTINCTION_DIR(), 'lmc_30dorshell_001.fits'),
    'Gordon et al. 2003, ApJ, 594, 279; R_V = 2.76')
LMCAVG_FILE = ConfigurationItem(
    'lmcavg_file', os.path.join(EXTINCTION_DIR(), 'lmc_diffuse_001.fits'),
    'Gordon et al. 2003, ApJ, 594, 279; R_V = 3.41')
MWAVG_FILE = ConfigurationItem(
    'mwavg_file', os.path.join(EXTINCTION_DIR(), 'milkyway_diffuse_001.fits'),
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 3.10')
MWDENSE_FILE = ConfigurationItem(
    'mwdense_file', os.path.join(EXTINCTION_DIR(), 'milkyway_dense_001.fits'),
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 5.00')
MWRV21_FILE = ConfigurationItem(
    'mwrv21_file', os.path.join(EXTINCTION_DIR(), 'milkyway_rv21_001.fits'),
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 2.1')
MWRV40_FILE = ConfigurationItem(
    'mwrv40_file', os.path.join(EXTINCTION_DIR(), 'milkyway_rv4_001.fits'),
    'Cardelli, Clayton, & Mathis 1989, ApJ, 345, 245; R_V = 4.0')
SMCBAR_FILE = ConfigurationItem(
    'smcbar_file', os.path.join(EXTINCTION_DIR(), 'smc_bar_001.fits'),
    'Gordon et al. 2003, ApJ, 594, 279; R_V=2.74')
XGAL_FILE = ConfigurationItem(
    'xgal_file', os.path.join(EXTINCTION_DIR(), 'xgal_starburst_001.fits'),
    'Calzetti et al. 2000, ApJ, 533, 682')

# COMMON FILTER PASSBANDS
PASSBAND_DIR = ConfigurationItem(
    'passband_dir', 'ftp://ftp.stsci.edu/cdbs/comp/nonhst/',
    'Location of passband files.')
BESSEL_H_FILE = ConfigurationItem(
    'bessel_h_file', os.path.join(PASSBAND_DIR(), 'bessell_h_004_syn.fits'),
    'Bessel H')
BESSEL_J_FILE = ConfigurationItem(
    'bessel_j_file', os.path.join(PASSBAND_DIR(), 'bessell_j_003_syn.fits'),
    'Bessel J')
BESSEL_K_FILE = ConfigurationItem(
    'bessel_k_file', os.path.join(PASSBAND_DIR(), 'bessell_k_003_syn.fits'),
    'Bessel K')
COUSINS_I_FILE = ConfigurationItem(
    'cousins_i_file', os.path.join(PASSBAND_DIR(), 'cousins_i_004_syn.fits'),
    'Cousins I')
COUSINS_R_FILE = ConfigurationItem(
    'cousins_r_file', os.path.join(PASSBAND_DIR(), 'cousins_r_004_syn.fits'),
    'Cousins R')
JOHNSON_B_FILE = ConfigurationItem(
    'johnson_b_file', os.path.join(PASSBAND_DIR(), 'johnson_b_004_syn.fits'),
    'Johnson B')
JOHNSON_I_FILE = ConfigurationItem(
    'johnson_i_file', os.path.join(PASSBAND_DIR(), 'johnson_i_003_syn.fits'),
    'Johnson I')
JOHNSON_J_FILE = ConfigurationItem(
    'johnson_j_file', os.path.join(PASSBAND_DIR(), 'johnson_j_003_syn.fits'),
    'Johnson J')
JOHNSON_K_FILE = ConfigurationItem(
    'johnson_k_file', os.path.join(PASSBAND_DIR(), 'johnson_k_003_syn.fits'),
    'Johnson K')
JOHNSON_R_FILE = ConfigurationItem(
    'johnson_r_file', os.path.join(PASSBAND_DIR(), 'johnson_r_003_syn.fits'),
    'Johnson R')
JOHNSON_U_FILE = ConfigurationItem(
    'johnson_u_file', os.path.join(PASSBAND_DIR(), 'johnson_u_004_syn.fits'),
    'Johnson U')
JOHNSON_V_FILE = ConfigurationItem(
    'johnson_v_file', os.path.join(PASSBAND_DIR(), 'johnson_v_004_syn.fits'),
    'Johnson V')


def set_files():  # pragma: no cover
    """Convenience function to update paths of configurable
    filenames. Useful for when these files are installed locally
    (see `stsynphot.config`).

    """
    VEGA_FILE.set(os.path.join(STDSTAR_DIR(), 'alpha_lyr_stis_005.fits'))

    ext_dir = EXTINCTION_DIR()
    LMC30DOR_FILE.set(os.path.join(ext_dir, 'lmc_30dorshell_001.fits'))
    LMCAVG_FILE.set(os.path.join(ext_dir, 'lmc_diffuse_001.fits'))
    MWAVG_FILE.set(os.path.join(ext_dir, 'milkyway_diffuse_001.fits'))
    MWDENSE_FILE.set(os.path.join(ext_dir, 'milkyway_dense_001.fits'))
    MWRV21_FILE.set(os.path.join(ext_dir, 'milkyway_rv21_001.fits'))
    MWRV40_FILE.set(os.path.join(ext_dir, 'milkyway_rv4_001.fits'))
    SMCBAR_FILE.set(os.path.join(ext_dir, 'smc_bar_001.fits'))
    XGAL_FILE.set(os.path.join(ext_dir, 'xgal_starburst_001.fits'))

    pb_dir = PASSBAND_DIR()
    BESSEL_H_FILE.set(os.path.join(pb_dir, 'bessell_h_004_syn.fits'))
    BESSEL_J_FILE.set(os.path.join(pb_dir, 'bessell_j_003_syn.fits'))
    BESSEL_K_FILE.set(os.path.join(pb_dir, 'bessell_k_003_syn.fits'))
    COUSINS_I_FILE.set(os.path.join(pb_dir, 'cousins_i_004_syn.fits'))
    COUSINS_R_FILE.set(os.path.join(pb_dir, 'cousins_r_004_syn.fits'))
    JOHNSON_B_FILE.set(os.path.join(pb_dir, 'johnson_b_004_syn.fits'))
    JOHNSON_I_FILE.set(os.path.join(pb_dir, 'johnson_i_003_syn.fits'))
    JOHNSON_J_FILE.set(os.path.join(pb_dir, 'johnson_j_003_syn.fits'))
    JOHNSON_K_FILE.set(os.path.join(pb_dir, 'johnson_k_003_syn.fits'))
    JOHNSON_R_FILE.set(os.path.join(pb_dir, 'johnson_r_003_syn.fits'))
    JOHNSON_U_FILE.set(os.path.join(pb_dir, 'johnson_u_004_syn.fits'))
    JOHNSON_V_FILE.set(os.path.join(pb_dir, 'johnson_v_004_syn.fits'))
