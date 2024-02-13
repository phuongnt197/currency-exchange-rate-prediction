import pandas as _pd
import matplotlib.pyplot as _plt
from scipy import stats as _stats
import statsmodels.api as _sm
from statsmodels.graphics.tsaplots import plot_acf as _plot_acf, plot_pacf as _plot_pacf

# time-series analysis plots

def tsplot(y, lags=None, figsize=(15, 10), style='bmh'):
    if not isinstance(y, _pd.Series):
        y = _pd.Series(y)
    with _plt.style.context(style):    
        fig = _plt.figure(figsize=figsize)
        #mpl.rcParams['font.family'] = 'Ubuntu Mono'
        layout = (3, 2)
        ts_ax = _plt.subplot2grid(layout, (0, 0), colspan=2)
        acf_ax = _plt.subplot2grid(layout, (1, 0))
        pacf_ax = _plt.subplot2grid(layout, (1, 1))
        qq_ax = _plt.subplot2grid(layout, (2, 0))
        pp_ax = _plt.subplot2grid(layout, (2, 1))
        
        y.plot(ax=ts_ax)
        ts_ax.set_title('Time Series Analysis Plots')
        _plot_acf(y, lags=lags, ax=acf_ax, alpha=0.05)
        _plot_pacf(y, lags=lags, ax=pacf_ax, alpha=0.05)
        _sm.qqplot(y, line='s', ax=qq_ax)
        qq_ax.set_title('QQ Plot')        
        _stats.probplot(y, sparams=(y.mean(), y.std()), plot=pp_ax)

        _plt.tight_layout()
    return 