import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Advanced Econometrics Course",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    .section-header {
        font-size: 2rem;
        color: #ff7f0e;
        border-bottom: 3px solid #ff7f0e;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .subsection-header {
        font-size: 1.5rem;
        color: #2ca02c;
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
    }
    .method-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .info-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 5px solid #1f77b4;
        margin: 1rem 0;
    }
    .highlight-box {
        background: linear-gradient(90deg, #ffeaa7 0%, #fdcb6e 100%);
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        font-weight: 600;
        color: #2d3436;
    }
    .new-badge {
        background-color: #e74c3c;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    .hot-badge {
        background-color: #f39c12;
        color: white;
        padding: 0.2rem 0.6rem;
        border-radius: 12px;
        font-size: 0.8rem;
        font-weight: bold;
        margin-left: 0.5rem;
    }
    ul {
        line-height: 1.8;
    }
    .stExpander {
        background-color: white;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        margin-bottom: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.markdown("## 📚 Course Navigation")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Select Module:",
    [
        "🏠 Home",
        "📈 Unit Root & Stationarity",
        "🔗 Cointegration Methods",
        "🌊 Fourier Methods",
        "⚡ Causality & VECM",
        "🔄 Nonlinear ARDL",
        "📊 Wavelet Analysis",
        "📉 Quantile Methods",
        "📊 GARCH Models",
        "🚀 Hybrid Applications",
        "🎯 Course Overview"
    ]
)

# Home Page
if page == "🏠 Home":
    st.markdown('<p class="main-header">🎓 Advanced Econometric Methods</p>', unsafe_allow_html=True)
    st.markdown(
        '<p style="text-align: center; font-size: 1.3rem; color: #555;">Master Modern Time Series & Econometric Techniques</p>',
        unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="method-card">
            <h3>🔬 Advanced Methods</h3>
            <p>Learn cutting-edge econometric techniques including Fourier transforms, Wavelet analysis, and Quantile methods</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="method-card">
            <h3>💡 Practical Applications</h3>
            <p>Apply methods to real-world problems in finance, energy economics, and policy analysis</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="method-card">
            <h3>🛠️ Hands-on Tools</h3>
            <p>Master R, Python, MATLAB, and specialized econometric software packages</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    st.markdown("## 🎯 What You'll Master")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Core Competencies
        - **Unit Root Testing**: Classical & advanced Fourier/Quantile methods
        - **Cointegration Analysis**: ARDL, Fourier, and Quantile approaches
        - **Causality Testing**: Time-varying and frequency-domain methods
        - **Nonlinear Modeling**: NARDL and asymmetric dynamics
        - **Volatility Modeling**: Complete GARCH family
        """)

    with col2:
        st.markdown("""
        ### Advanced Techniques
        - **Wavelet Analysis**: Multi-scale time-frequency decomposition
        - **Fourier Methods**: Smooth structural breaks modeling
        - **Quantile Regression**: Distribution-specific analysis
        - **Rolling/Recursive Methods**: Time-varying parameters
        - **Hybrid Models**: Integrated cutting-edge frameworks
        """)

    st.markdown("---")

    st.markdown("""
    <div class="info-box">
        <h3>📌 Course Structure</h3>
        <p>This comprehensive program covers <strong>10 major modules</strong> spanning classical and modern econometric methods. 
        Each module builds progressively, from foundational concepts to advanced hybrid applications.</p>
        <p><strong>Perfect for:</strong> Graduate students, researchers, data scientists, and economists seeking advanced time series expertise.</p>
    </div>
    """, unsafe_allow_html=True)

# Unit Root & Stationarity
elif page == "📈 Unit Root & Stationarity":
    st.markdown('<p class="section-header">📈 Stationarity & Unit Root Testing</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <strong>Module Overview:</strong> Master the fundamental tools for testing stationarity and unit roots, 
        from classical methods to cutting-edge Fourier and Quantile approaches.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Classical Tests
    with st.expander("📊 Classical Unit Root Tests", expanded=True):
        st.markdown("### Essential Foundation Methods")
        st.markdown("""
        **Core Tests:**
        - **ADF (Augmented Dickey-Fuller)**: Standard unit root testing
        - **PP (Phillips-Perron)**: Non-parametric correction for serial correlation
        - **KPSS (Kwiatkowski-Phillips-Schmidt-Shin)**: Testing stationarity (null hypothesis differs)

        **Enhanced Tests:**
        - **DF-GLS**: Generalized Least Squares detrending for improved power
        - **Ng-Perron Tests**: Modified information criteria for lag selection

        **Structural Break Tests:**
        - **Zivot-Andrews Test**: Endogenous single structural break
        - **Perron Tests**: Unit root with known/unknown break dates
        """)

        st.info("💡 **Key Insight**: Classical tests may fail to reject unit root in presence of structural breaks")

    # Fourier Tests
    with st.expander("🌊 Fourier Unit Root Tests 🆕", expanded=True):
        st.markdown("### Next-Generation Break Modeling")
        st.markdown("""
        **Revolutionary Approach:**
        - **Enders-Lee Fourier ADF**: Captures smooth, gradual structural changes
        - **Flexible Fourier Form**: Models unknown number and form of breaks
        - **Fourier KPSS**: Stationarity testing with trigonometric trends
        - **Fourier-GLS**: Enhanced power with Fourier approximations

        **Advantages Over Classical Methods:**
        - No need to specify break dates
        - Captures multiple smooth transitions
        - Superior power in presence of gradual shifts
        - Flexible functional form for structural changes
        """)

        st.markdown("""
        <div class="highlight-box">
        🔥 <strong>Why Fourier?</strong> Traditional dummy variables require knowing break dates. 
        Fourier functions approximate structural changes without prior knowledge!
        </div>
        """, unsafe_allow_html=True)

    # Quantile Tests
    with st.expander("📊 Quantile Unit Root Tests 🆕"):
        st.markdown("### Distribution-Specific Testing")
        st.markdown("""
        **Quantile-Based Approaches:**
        - **Koenker-Xiao Quantile Autoregression**: Test unit roots at different quantiles
        - **Quantile ADF with Fourier**: Combines quantile and Fourier advantages

        **Key Applications:**
        - Tail behavior analysis
        - Asymmetric responses to shocks
        - Distribution-dependent persistence
        - Extreme value analysis

        **Unique Benefits:**
        - Robust to outliers
        - Captures heterogeneous dynamics across distribution
        - Identifies quantile-specific unit roots
        """)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **R Packages:**
        - `urca`: Classical unit root tests
        - `uroot`: Seasonal unit roots
        - Custom Fourier functions
        """)
    with col2:
        st.markdown("""
        **Applications:**
        - Macroeconomic time series
        - Financial data analysis
        - Climate change studies
        """)

# Cointegration Methods
elif page == "🔗 Cointegration Methods":
    st.markdown('<p class="section-header">🔗 Cointegration Analysis</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <strong>Module Overview:</strong> Explore long-run equilibrium relationships from classical two-step procedures 
        to modern ARDL bounds testing and quantile cointegration.
    </div>
    """, unsafe_allow_html=True)

    # Classical Cointegration
    with st.expander("📚 Classical Cointegration Methods", expanded=True):
        st.markdown("### Foundational Techniques")
        st.markdown("""
        **Engle-Granger Two-Step Procedure:**
        - Step 1: Estimate long-run cointegrating equation
        - Step 2: Test residuals for stationarity
        - Simple but limited to single cointegrating vector

        **Johansen Maximum Likelihood:**
        - Tests for multiple cointegrating relationships
        - Trace and Maximum Eigenvalue tests
        - Provides both cointegrating vectors and adjustment speeds

        **Phillips-Ouliaris Tests:**
        - Non-parametric residual-based tests
        - Alternative to Engle-Granger
        - Robust to certain violations
        """)

    # ARDL
    with st.expander("🚀 ARDL Bounds Testing", expanded=True):
        st.markdown("### Modern Flexible Framework")
        st.markdown("""
        **Pesaran-Shin-Smith (2001) Bounds Test:**
        - **Revolutionary Feature**: Works with mixed I(0)/I(1) variables
        - No pre-testing for unit roots required
        - Suitable for small samples

        **Key Components:**
        - Critical values with upper and lower bounds
        - Decision rules based on F-statistic
        - Error correction representation
        - Long-run and short-run dynamics

        **Advantages:**
        - Flexible lag structure
        - Handles different orders of integration
        - Robust in small samples
        - Simultaneous estimation of long and short-run parameters
        """)

        st.success("✅ **Best Practice**: ARDL is now preferred for most cointegration analysis")

    # Fourier Cointegration
    with st.expander("🌊 Fourier-Based Cointegration Tests 🔥", expanded=True):
        st.markdown("### Structural Break Cointegration")
        st.markdown("""
        **Advanced Fourier Methods:**

        **1. Fourier ADL Cointegration (Banerjee et al.):**
        - Autoregressive Distributed Lag with Fourier terms
        - Captures smooth structural changes in long-run relationship

        **2. Johansen-Type with Fourier:**
        - Multiple cointegrating vectors with structural breaks
        - Fourier approximation of deterministic components

        **3. Fourier Engle-Granger (FEG):**
        - Two-step procedure with Fourier adjustment
        - Improved power in presence of breaks

        **4. Tsong et al. Fourier Approximation:**
        - Flexible approach for testing cointegration null
        - Multiple frequency components

        **Fourier ARDL Bounds Test:**
        - Bootstrap critical values with Fourier function
        - Machine learning integration (Wu et al.)
        - Superior to traditional dummy variables
        - Handles smooth structural changes
        """)

        st.markdown("""
        <div class="highlight-box">
        🎯 <strong>Application Power:</strong> Fourier methods excel when structural breaks are 
        gradual, unknown, or multiple - common in economic data!
        </div>
        """, unsafe_allow_html=True)

    # Quantile Cointegration
    with st.expander("📊 Quantile Cointegration 🆕"):
        st.markdown("### Distribution-Specific Long-Run Relationships")
        st.markdown("""
        **Quantile Cointegration Methods:**

        **Xiao (2009) Quantile Cointegration:**
        - Tests cointegration at different quantiles
        - Allows for heterogeneous long-run relationships

        **Fully-Modified Quantile Regression:**
        - Addresses endogeneity in quantile framework
        - Corrects for serial correlation

        **Augmented Quantile Cointegration:**
        - Enhanced power and efficiency
        - Robust to distributional assumptions

        **Applications:**
        - Tail dependence analysis
        - Asymmetric market linkages
        - Risk management
        - Extreme event analysis
        """)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **R Packages:**
        - `ARDL`: Bounds testing
        - `urca`: Classical methods
        - `quantreg`: Quantile methods
        """)
    with col2:
        st.markdown("""
        **GAUSS:**
        - `tspdlib`: Fourier cointegration
        - Bootstrap procedures
        """)

# Fourier Methods
elif page == "🌊 Fourier Methods":
    st.markdown('<p class="section-header">🌊 Fourier Methods Revolution</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="method-card">
        <h3>🔥 Revolutionary Approach to Structural Breaks</h3>
        <p><strong>Core Innovation:</strong> Fourier approximations replace traditional dummy variables, 
        allowing flexible modeling of smooth, gradual, and multiple structural changes without requiring 
        knowledge of break dates.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Why Fourier
    with st.expander("💡 Why Fourier Methods?", expanded=True):
        st.markdown("""
        ### The Structural Break Problem

        **Traditional Approach Limitations:**
        - Requires knowing exact break dates
        - Assumes sharp, discrete breaks
        - Limited to small number of breaks
        - Poor power with unknown breaks

        **Fourier Solution:**
        - ✅ No need to specify break dates
        - ✅ Captures smooth, gradual transitions
        - ✅ Flexible functional form
        - ✅ Approximates any deterministic function
        - ✅ Superior power in presence of structural changes

        ### Mathematical Foundation
        Fourier series can approximate any deterministic function:
        """)

        st.latex(r"""
        f(t) = \alpha_0 + \sum_{k=1}^{n} \left[\alpha_k \cos\left(\frac{2\pi kt}{T}\right) + \beta_k \sin\left(\frac{2\pi kt}{T}\right)\right]
        """)

        st.markdown("""
        Where:
        - `k` = frequency component
        - `T` = sample size
        - `α, β` = Fourier coefficients
        """)

    # Unit Root
    with st.expander("📈 Fourier Unit Root Tests"):
        st.markdown("""
        **Enders-Lee Fourier ADF Test:**
        - Extends ADF with Fourier terms
        - Captures smooth transitions
        - Optimal frequency selection

        **Fourier-GLS:**
        - GLS detrending with Fourier approximation
        - Enhanced power
        - Efficient estimation

        **Fourier KPSS:**
        - Stationarity testing with structural breaks
        - Complementary to Fourier ADF

        **Key Features:**
        - Single frequency component often sufficient
        - Data-driven frequency selection
        - Robust to break form misspecification
        """)

    # Cointegration
    with st.expander("🔗 Fourier Cointegration"):
        st.markdown("""
        **Fourier ADL (Banerjee et al.):**
        - Distributed lag model with Fourier components
        - Tests for cointegration with smooth breaks

        **Fourier ARDL Bounds Test:**
        - Combines ARDL flexibility with Fourier power
        - Bootstrap critical values
        - Machine learning integration for optimal specification

        **Johansen with Fourier:**
        - Multiple cointegrating vectors
        - Fourier deterministic components
        - System estimation

        **Applications:**
        - Energy-economy relationships
        - Financial market linkages
        - Environmental Kuznets curves
        """)

    # VECM
    with st.expander("⚡ Fourier VECM"):
        st.markdown("""
        **Fourier Vector Error Correction Model:**
        - Explicit error correction equations with Fourier terms
        - Long-run and short-run dynamics with structural breaks
        - Fourier deterministic components in levels and differences

        **Model Structure:**
        """)

        st.latex(r"""
        \Delta Y_t = \alpha\beta'Y_{t-1} + \gamma F(t) + \sum_{i=1}^{p-1}\Gamma_i\Delta Y_{t-i} + \epsilon_t
        """)

        st.markdown("""
        Where `F(t)` represents Fourier terms

        **Advantages:**
        - Captures time-varying equilibrium
        - Smooth adjustment dynamics
        - No need for dummy variables
        """)

    # Causality
    with st.expander("🔄 Fourier Causality Testing"):
        st.markdown("""
        **Fourier Toda-Yamamoto:**
        - Causality testing with structural breaks
        - Level VAR with Fourier approximation
        - Robust to integration order

        **Nazlioglu et al. Fourier Granger Causality:**
        - Gradual shifts in causal relationships
        - Bootstrap critical values
        - Frequency component optimization

        **Key Benefits:**
        - Detects changing causal patterns
        - Avoids spurious non-causality
        - Flexible break modeling
        """)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Implementation Tools")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Software:**
        - R (custom functions)
        - GAUSS (tspdlib library)
        - MATLAB (custom codes)
        """)
    with col2:
        st.markdown("""
        **Best Practices:**
        - Start with single frequency
        - Use information criteria for selection
        - Bootstrap for critical values
        """)

# Causality & VECM
elif page == "⚡ Causality & VECM":
    st.markdown('<p class="section-header">⚡ Causality Analysis & Vector Error Correction</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <strong>Module Overview:</strong> Master causal inference in time series from classical Granger causality 
        to advanced time-varying, frequency-domain, and quantile-specific approaches.
    </div>
    """, unsafe_allow_html=True)

    # Fourier VECM
    with st.expander("🌊 Fourier Vector Error Correction Models", expanded=True):
        st.markdown("""
        ### Long-Run and Short-Run Dynamics with Breaks

        **Fourier VECM Framework:**
        - Error correction equations with Fourier structural breaks
        - Captures time-varying equilibrium relationships
        - Distinguishes long-run and short-run dynamics

        **Model Components:**
        - **Error Correction Term**: Speed of adjustment to equilibrium
        - **Fourier Deterministic Components**: Smooth structural changes
        - **Short-run Dynamics**: Lagged difference terms

        **Applications:**
        - Monetary policy transmission with regime changes
        - Energy-growth nexus with technological shifts
        - International trade relationships with gradual liberalization
        """)

        st.markdown("""
        <div class="highlight-box">
        💡 <strong>Innovation:</strong> Traditional VECM assumes stable equilibrium. Fourier VECM 
        allows equilibrium to evolve smoothly over time!
        </div>
        """, unsafe_allow_html=True)

    # Fourier Causality
    with st.expander("🔄 Fourier Causality Testing", expanded=True):
        st.markdown("""
        ### Structural Break-Robust Causality

        **Fourier Toda-Yamamoto Causality:**
        - Extends Toda-Yamamoto to structural breaks
        - Level VAR with Fourier approximation
        - No need for cointegration pre-testing

        **Nazlioglu et al. Fourier Granger Causality:**
        - Bootstrap critical values for size correction
        - Optimal frequency selection
        - Gradual shifts in causal relationships

        **Key Advantages:**
        - Avoids spurious non-causality from breaks
        - Detects changing causal patterns
        - More powerful than traditional tests

        **Practical Applications:**
        - Energy consumption → Economic growth (with policy changes)
        - Financial contagion across markets
        - Environmental policy effectiveness
        """)

    # Quantile Causality
    with st.expander("📊 Granger Causality in Quantiles 🆕", expanded=True):
        st.markdown("""
        ### Distribution-Specific Causal Analysis

        **Troster (2018) Quantile Causality Test:**
        - Tests causality at different quantiles
        - Non-parametric framework
        - Robust to distributional assumptions

        **Hybrid Non-Parametric Quantile Causality:**
        - Combines quantile and non-parametric methods
        - Captures tail dependencies
        - Identifies causality at extreme quantiles

        **Why Quantile Causality Matters:**
        - **Tail Dependencies**: Different causality in extremes vs. median
        - **Asymmetric Effects**: Positive vs. negative shock responses
        - **Risk Management**: Causal relationships during crises
        - **Policy Analysis**: Effects vary across economic states

        **Example Applications:**
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Financial Markets:**
            - Crisis contagion (lower quantiles)
            - Bull market linkages (upper quantiles)
            - Volatility spillovers
            """)
        with col2:
            st.markdown("""
            **Macroeconomics:**
            - Recession vs. expansion dynamics
            - Inflation asymmetries
            - Labor market responses
            """)

    # Wavelet Causality
    with st.expander("🌊 Wavelet-Based Causality", expanded=True):
        st.markdown("""
        ### Time-Frequency Domain Causality

        **CWT Causality:**
        - Continuous Wavelet Transform approach
        - No spectral factorization required
        - Scale-specific causal relationships

        **Wavelet Granger Causality (Olayeni):**
        - Decomposes series into time-scale components
        - Tests causality at each scale
        - Reveals multi-horizon causal patterns

        **Time-Varying Frequency Domain Causality:**
        - Causality evolves over time AND frequency
        - Captures changing lead-lag relationships
        - Identifies structural changes in causality

        **Unique Insights:**
        - Short-run vs. long-run causality
        - Time-varying causal strength
        - Frequency-specific channels
        - Crisis vs. normal period patterns
        """)

        st.info("🎯 **Power**: Wavelet methods reveal when and at what frequencies causality operates")

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **R Packages:**
        - `vars`: VAR/VECM
        - `biwavelet`: Wavelet
        - Custom causality functions
        """)
    with col2:
        st.markdown("""
        **MATLAB:**
        - Wavelet toolbox
        - Custom VECM codes
        - Causality functions
        """)
    with col3:
        st.markdown("""
        **Applications:**
        - Policy analysis
        - Market linkages
        - Risk transmission
        """)

# Nonlinear ARDL
elif page == "🔄 Nonlinear ARDL":
    st.markdown('<p class="section-header">🔄 Nonlinear ARDL Models</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="method-card">
        <h3>🚀 Capturing Asymmetric Dynamics</h3>
        <p><strong>Core Innovation:</strong> NARDL extends ARDL to capture positive and negative 
        asymmetries in both short-run and long-run relationships.</p>
    </div>
    """, unsafe_allow_html=True)

    # NARDL Framework
    with st.expander("📚 NARDL Framework (Shin et al.)", expanded=True):
        st.markdown("""
        ### Asymmetric Long-Run Cointegration

        **Core Concept:**
        Traditional models assume symmetric responses:
        - Oil price ↑ $10 = same effect as oil price ↓ $10
        - NARDL allows: Different responses to increases vs. decreases

        **Positive and Negative Partial Sum Decomposition:**
        """)

        st.latex(r"""
        x_t = x_0 + x_t^+ + x_t^-
        """)

        st.markdown("""
        Where:
        """)

        st.latex(r"""
        x_t^+ = \sum_{i=1}^t \Delta x_i^+ = \sum_{i=1}^t \max(\Delta x_i, 0)
        """)

        st.latex(r"""
        x_t^- = \sum_{i=1}^t \Delta x_i^- = \sum_{i=1}^t \min(\Delta x_i, 0)
        """)

        st.markdown("""
        **Asymmetric Dynamic Multipliers:**
        - **Short-run asymmetries**: Immediate response differences
        - **Long-run asymmetries**: Equilibrium relationship differences
        - **Adjustment asymmetries**: Different speeds of adjustment

        **Testing Procedures:**
        - Wald tests for short-run asymmetry
        - Wald tests for long-run asymmetry
        - Bounds test for cointegration
        """)

        st.success(
            "✅ **Key Advantage**: Captures realistic economic behavior where increases and decreases have different impacts")

    # Applications
    with st.expander("🌍 NARDL Applications", expanded=True):
        st.markdown("""
        ### Real-World Economic Asymmetries

        **1. Oil Price Pass-Through:**
        - **Rockets and Feathers**: Prices rise quickly but fall slowly
        - Gasoline retail pricing
        - Airline ticket pricing
        - Transportation costs

        **2. Exchange Rate Effects:**
        - Depreciation vs. appreciation impacts
        - Import vs. export price responses
        - Currency crisis asymmetries
        - Trade balance adjustments

        **3. Policy Asymmetries:**
        - Monetary policy tightening vs. easing
        - Fiscal stimulus vs. austerity
        - Interest rate changes
        - Tax policy effects

        **4. Financial Markets:**
        - Good news vs. bad news effects
        - Bull vs. bear market dynamics
        - Volatility asymmetries
        - Risk premium variations

        **5. Environmental Economics:**
        - Carbon pricing asymmetries
        - Energy efficiency responses
        - Climate policy impacts
        """)

        st.markdown("""
        <div class="highlight-box">
        💼 <strong>Industry Relevance:</strong> NARDL is extensively used in central banks, 
        energy companies, and financial institutions for policy analysis and forecasting.
        </div>
        """, unsafe_allow_html=True)

    # Quantile ARDL
    with st.expander("📊 Quantile ARDL (Q-ARDL) 🆕", expanded=True):
        st.markdown("""
        ### Location-Specific Long-Run Relationships

        **Cho et al. Q-ARDL Framework:**
        Combines ARDL with quantile regression to analyze:
        - Different cointegrating relationships at different quantiles
        - Distribution-dependent error correction
        - Heterogeneous long-run equilibria

        **Key Features:**
        - **Quantile-Specific Error Correction**: Adjustment speeds vary across distribution
        - **Location-Specific Dynamics**: Different relationships in tails vs. center
        - **Bootstrap Inference**: Robust critical values

        **Applications:**
        - **Income Distribution**: Growth effects differ across income levels
        - **Financial Risk**: Different dynamics in good vs. bad times
        - **Regional Analysis**: Heterogeneous responses across regions

        **Advantages Over Standard ARDL:**
        - Captures heterogeneity across distribution
        - Robust to outliers and non-normal errors
        - Provides complete distributional picture
        - Better for extreme value analysis
        """)

    # Wavelet-NARDL
    with st.expander("🌊 Wavelet-NARDL Integration 🔥🆕", expanded=True):
        st.markdown("""
        ### Multi-Scale Asymmetric Analysis

        **Jammazi et al. Wavelet-Based NARDL:**
        Revolutionary combination of wavelet decomposition and NARDL

        **Methodology:**
        1. **Wavelet Decomposition**: Decompose series using MODWT
        2. **Denoising**: Remove noise components
        3. **NARDL Estimation**: Apply NARDL to decomposed series
        4. **Multi-Scale Analysis**: Analyze asymmetries at each scale

        **Advantages:**
        - **Noise Removal**: Better signal extraction
        - **Scale-Specific Asymmetries**: Different asymmetries at different horizons
        - **Improved Model Fit**: Better diagnostics and forecasting
        - **Time-Frequency Insights**: When and at what frequencies asymmetries occur

        **Applications:**
        - Energy market dynamics with multiple cycles
        - Financial contagion across time scales
        - Climate-economy relationships
        - Multi-horizon policy analysis
        """)

        st.markdown("""
        <div class="highlight-box">
        🔥 <strong>Cutting Edge:</strong> W-NARDL represents the frontier of asymmetric 
        cointegration analysis, published in top-tier journals!
        </div>
        """, unsafe_allow_html=True)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **R Packages:**
        - `nardl`: NARDL estimation
        - `wavelets`: Wavelet decomposition
        - `quantreg`: Quantile methods
        """)
    with col2:
        st.markdown("""
        **EViews:**
        - Built-in NARDL procedures
        - User-friendly interface
        - Automated testing
        """)

# Wavelet Analysis
elif page == "📊 Wavelet Analysis":
    st.markdown('<p class="section-header">🌊 Wavelet Analysis</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="method-card">
        <h3>🎯 Time-Frequency Domain Analysis</h3>
        <p><strong>Revolutionary Feature:</strong> Wavelets decompose time series simultaneously 
        in time AND frequency, revealing when and at what frequencies relationships occur.</p>
    </div>
    """, unsafe_allow_html=True)

    # Fundamentals
    with st.expander("📚 Wavelet Theory Fundamentals", expanded=True):
        st.markdown("""
        ### Why Wavelets?

        **Limitations of Traditional Methods:**
        - **Time Domain**: Loses frequency information
        - **Fourier Analysis**: Loses time localization
        - **Assumption**: Stationarity over entire sample

        **Wavelet Solution:**
        - ✅ Simultaneous time-frequency analysis
        - ✅ Multi-scale decomposition
        - ✅ Handles non-stationarity
        - ✅ Localized in both time and frequency

        **Types of Wavelet Transforms:**

        **1. Continuous Wavelet Transform (CWT):**
        - Smooth, continuous representation
        - Best for visualization
        - Cross-wavelet and coherence analysis

        **2. Discrete Wavelet Transform (DWT):**
        - Efficient computation
        - Orthogonal decomposition
        - Multi-resolution analysis

        **3. Maximal Overlap DWT (MODWT):**
        - Non-decimated (no information loss)
        - Time-invariant
        - Best for time series analysis
        """)

        st.markdown("""
        <div class="highlight-box">
        🎓 <strong>Key Concept:</strong> Wavelets are "little waves" that oscillate for a short time, 
        unlike sine waves that oscillate forever. This allows localization in time!
        </div>
        """, unsafe_allow_html=True)

    # Decomposition
    with st.expander("🔍 Wavelet Decomposition & Multi-Resolution", expanded=True):
        st.markdown("""
        ### Multi-Scale Time Series Analysis

        **MODWT Decomposition Process:**
        Original series decomposed into:
        - **D1**: High frequency (2-4 periods) - Very short-run
        - **D2**: Medium-high frequency (4-8 periods) - Short-run
        - **D3**: Medium frequency (8-16 periods) - Business cycle
        - **D4**: Medium-low frequency (16-32 periods) - Medium-run
        - **D5**: Low frequency (32-64 periods) - Long-run
        - **S5**: Smooth component (>64 periods) - Trend

        **Multi-Resolution Advantages:**
        - Separate noise from signal
        - Identify dominant cycles
        - Scale-specific modeling
        - Better forecasting at each horizon

        **Applications:**
        - **Finance**: High-frequency trading vs. long-term investment
        - **Macro**: Business cycles vs. structural trends
        - **Energy**: Daily fluctuations vs. seasonal patterns
        """)

    # Correlation
    with st.expander("📊 Wavelet Correlation & Covariance"):
        st.markdown("""
        ### Scale-Specific Relationships

        **Wavelet Correlation Across Scales:**
        - Measure correlation at each time scale
        - Identify scale-dependent relationships
        - Distinguish short-run vs. long-run co-movements

        **Cross-Wavelet Correlation:**
        - Bivariate wavelet analysis
        - Reveals common features across series
        - Identifies synchronized components

        **Lead-Lag Relationships:**
        - Time-scale dependent causality
        - Which series leads at which frequencies
        - Phase difference analysis

        **Practical Uses:**
        - Portfolio diversification strategies
        - Economic indicator relationships
        - Market microstructure analysis
        """)

    # Coherence
    with st.expander("🌟 Wavelet Coherence Analysis 🔥", expanded=True):
        st.markdown("""
        ### Time-Frequency Co-Movement Analysis

        **Continuous Wavelet Transform (CWT):**
        - Smooth time-frequency representation
        - Visualizes energy distribution
        - Identifies dominant frequencies over time

        **Cross-Wavelet Transform:**
        - Common power between two series
        - Reveals synchronized oscillations
        - Time-varying cross-spectral analysis

        **Wavelet Coherence (WCA):**
        - "Correlation" in time-frequency space
        - Values from 0 (no coherence) to 1 (perfect coherence)
        - Statistical significance testing with bootstrapping

        **Phase Differences Interpretation:**
        - **In-phase (0°)**: Variables move together
        - **Anti-phase (180°)**: Variables move opposite
        - **Lead-lag (±90°)**: One variable leads the other

        **Advanced Extensions:**
        - **Partial Wavelet Coherence**: Controlling for other variables
        - **Multiple Wavelet Coherence**: Multi-variate relationships

        **Visualization:**
        - Heat maps showing coherence over time and frequency
        - Arrows indicating phase relationships
        - Cone of influence marking reliable regions
        """)

        st.markdown("""
        <div class="highlight-box">
        📈 <strong>Power of Visualization:</strong> Wavelet coherence plots reveal at a glance 
        when, for how long, and at what frequencies two variables are related!
        </div>
        """, unsafe_allow_html=True)

    # Applications
    with st.expander("🌍 Wavelet Applications"):
        st.markdown("""
        ### Real-World Use Cases

        **1. Financial Contagion:**
        - Crisis period identification
        - Cross-market spillovers
        - Time-varying correlations
        - Frequency-dependent contagion

        **2. Energy-Economy Linkages:**
        - Oil price-GDP relationships
        - Renewable energy integration
        - Energy efficiency dynamics
        - Multi-scale policy effects

        **3. Environmental Economics:**
        - Climate-economy co-movements
        - Carbon emission patterns
        - Environmental Kuznets curve
        - Sustainability transitions

        **4. International Finance:**
        - Exchange rate dynamics
        - Capital flow synchronization
        - Currency crisis analysis
        - International trade cycles
        """)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **R Packages:**
        - `wavelets`: Basic wavelet analysis
        - `waveslim`: Advanced methods
        - `biwavelet`: Coherence analysis
        """)
    with col2:
        st.markdown("""
        **MATLAB:**
        - Wavelet Toolbox
        - Comprehensive functions
        - Excellent visualization
        """)

# Quantile Methods
elif page == "📉 Quantile Methods":
    st.markdown('<p class="section-header">📊 Quantile Methods</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="method-card">
        <h3>🎯 Beyond-the-Mean Analysis</h3>
        <p><strong>Core Innovation:</strong> Quantile methods analyze relationships across the 
        entire distribution, revealing heterogeneous effects often masked by mean-based approaches.</p>
    </div>
    """, unsafe_allow_html=True)

    # Why Quantile
    with st.expander("💡 Why Quantile Methods?", expanded=True):
        st.markdown("""
        ### Limitations of Mean-Based Methods

        **Traditional OLS Problem:**
        - Estimates only conditional mean relationship
        - Single coefficient for entire distribution
        - Misses heterogeneity and asymmetries
        - Sensitive to outliers

        **Quantile Regression Solution:**
        - Estimates relationships at any quantile (τ)
        - τ = 0.1 (lower tail), τ = 0.5 (median), τ = 0.9 (upper tail)
        - Complete distributional picture
        - Robust to outliers

        **Example - Income and Consumption:**
        - OLS: Average effect across all income levels
        - Quantile: Different effects for poor (Q10), middle (Q50), rich (Q90)

        **Applications:**
        - Risk analysis (tail behavior)
        - Inequality studies
        - Extreme event analysis
        - Asymmetric market responses
        """)

        st.success("✅ **Key Insight**: Economic relationships often differ dramatically across the distribution!")

    # Unit Root
    with st.expander("📈 Quantile Unit Root Tests"):
        st.markdown("""
        ### Distribution-Specific Stationarity Testing

        **Koenker-Xiao Quantile Autoregression:**
        - Tests unit root at different quantiles
        - Allows for quantile-dependent persistence
        - Robust to distributional assumptions

        **Quantile ADF with Fourier:**
        - Combines quantile and Fourier advantages
        - Structural breaks vary across distribution
        - Enhanced power

        **Applications:**
        - Tail behavior of financial returns
        - Asymmetric inflation persistence
        - Distribution-dependent mean reversion
        """)

    # Cointegration
    with st.expander("🔗 Quantile Cointegration"):
        st.markdown("""
        ### Heterogeneous Long-Run Relationships

        **Xiao (2009) Quantile Cointegration:**
        - Long-run relationships vary across quantiles
        - Different equilibria for different states
        - Quantile-specific error correction

        **Fully-Modified Quantile Regression:**
        - Addresses endogeneity in quantile framework
        - Corrects for serial correlation
        - Optimal inference properties

        **Augmented Quantile Cointegration:**
        - Enhanced efficiency
        - Better finite sample performance
        """)

    # Q-ARDL
    with st.expander("🚀 Quantile ARDL (Q-ARDL) 🔥", expanded=True):
        st.markdown("""
        ### Location-Specific Dynamics

        **Cho et al. Q-ARDL Framework:**
        Extends ARDL to quantile regression framework

        **Key Components:**
        - **Quantile-Specific Cointegration**: Different long-run relationships
        - **Location-Dependent Error Correction**: Varying adjustment speeds
        - **Quantile Bounds Testing**: Distribution-specific inference
        - **Bootstrap Critical Values**: Robust inference

        **Model Structure:**
        """)

        st.latex(r"""
        Q_{\tau}(y_t | X_t) = \alpha(\tau) + \sum_{i=1}^p \beta_i(\tau) y_{t-i} + \sum_{j=0}^q \gamma_j(\tau) x_{t-j}
        """)

        st.markdown("""
        **Advantages:**
        - Complete distributional analysis
        - Identifies heterogeneous effects
        - Robust to outliers
        - Better for extreme scenarios

        **Applications:**
        - Income-growth nexus across income distribution
        - Financial stress transmission
        - Environmental policy effectiveness
        - Regional development heterogeneity
        """)

    # Quantile Causality
    with st.expander("⚡ Granger Causality in Quantiles", expanded=True):
        st.markdown("""
        ### Tail-Dependent Causality

        **Troster (2018) Quantile Causality Test:**
        - Tests causality at different quantiles
        - Reveals tail dependencies
        - Non-parametric framework

        **Hybrid Non-Parametric Quantile Causality:**
        - Combines quantile and non-parametric methods
        - Robust to model misspecification
        - Captures complex nonlinear relationships

        **Causality at Extreme Quantiles:**
        - **Lower tail (Q10)**: Crisis and downturn causality
        - **Median (Q50)**: Normal period causality
        - **Upper tail (Q90)**: Boom period causality

        **Why It Matters:**
        - Different causal mechanisms in good vs. bad times
        - Risk management insights
        - Policy effectiveness varies by economic state
        - Contagion analysis

        **Example Applications:**
        """)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""
            **Financial Markets:**
            - Bear market contagion
            - Bull market herding
            - Volatility spillovers
            - Tail risk transmission
            """)
        with col2:
            st.markdown("""
            **Macroeconomics:**
            - Recession dynamics
            - Expansion mechanisms
            - Asymmetric policy effects
            - Distributional impacts
            """)

    # QQR
    with st.expander("📊 Quantile-on-Quantile Regression (QQR) 🆕", expanded=True):
        st.markdown("""
        ### Complete Distributional Mapping

        **QQ Regression Methodology:**
        - Maps quantiles of X to quantiles of Y
        - Shows how distribution of one variable affects distribution of another
        - Local linear regression approach

        **Key Features:**
        - **Full Distributional Picture**: Not just mean effect
        - **Heterogeneous Effects**: Different impacts across distributions
        - **Nonlinear Relationships**: Captures complex patterns
        - **Visual Interpretation**: Heat maps and contour plots

        **Applications to Energy-Growth Nexus:**
        - How does energy consumption at different levels (quantiles) affect growth at different levels?
        - Identifies optimal energy-growth combinations
        - Policy implications for different development stages

        **Other Applications:**
        - Income inequality dynamics
        - Financial risk assessment
        - Environmental quality-growth relationships
        - Health-productivity linkages
        """)

        st.markdown("""
        <div class="highlight-box">
        🎯 <strong>Visualization Power:</strong> QQR produces stunning heat maps showing 
        the complete relationship landscape across distributions!
        </div>
        """, unsafe_allow_html=True)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **R Packages:**
        - `quantreg`: Core quantile regression
        - Custom Q-ARDL functions
        - Causality implementations
        """)
    with col2:
        st.markdown("""
        **Python:**
        - `statsmodels`: Quantile regression
        - `scikit-learn`: Quantile forest
        """)

# GARCH Models
elif page == "📊 GARCH Models":
    st.markdown('<p class="section-header">📈 GARCH Family Models</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="method-card">
        <h3>💹 Modeling Volatility Dynamics</h3>
        <p><strong>Core Purpose:</strong> GARCH models capture time-varying volatility and volatility 
        clustering - key features of financial and economic time series.</p>
    </div>
    """, unsafe_allow_html=True)

    # Univariate GARCH
    with st.expander("📊 Univariate GARCH Models", expanded=True):
        st.markdown("""
        ### Foundation Volatility Models

        **GARCH(p,q) Specification:**
        """)

        st.latex(r"""
        \sigma_t^2 = \omega + \sum_{i=1}^p \alpha_i \epsilon_{t-i}^2 + \sum_{j=1}^q \beta_j \sigma_{t-j}^2
        """)

        st.markdown("""
        Where:
        - σ²ₜ = conditional variance
        - ε²ₜ = squared residuals (ARCH term)
        - σ²ₜ₋₁ = lagged variance (GARCH term)

        **Key Properties:**
        - Captures volatility clustering
        - Heavy-tailed distributions
        - Persistent volatility shocks

        **EGARCH (Exponential GARCH):**
        - Asymmetric volatility responses
        - Leverage effects (bad news > good news)
        - Log specification ensures positive variance

        **TGARCH/GJR-GARCH (Threshold GARCH):**
        - Separate effects for positive and negative shocks
        - Captures asymmetric volatility
        - Widely used in finance

        **PGARCH (Power GARCH):**
        - Flexible power transformation
        - Accommodates various distributions

        **IGARCH (Integrated GARCH):**
        - Persistent volatility shocks
        - Unit root in variance equation
        """)

        st.info("💡 **Financial Fact**: Volatility clustering - large changes tend to be followed by large changes")

    # Extensions
    with st.expander("🚀 GARCH Extensions", expanded=True):
        st.markdown("""
        ### Advanced Specifications

        **GARCH-M (GARCH in Mean):**
        - Volatility appears in mean equation
        - Risk-return tradeoff modeling
        - Time-varying risk premium

        **QGARCH (Quadratic GARCH):**
        - Quadratic terms in variance equation
        - More flexible asymmetry

        **AVGARCH (Asymmetric Volatility GARCH):**
        - General asymmetric specification
        - Multiple asymmetry channels

        **Component GARCH:**
        - Separates permanent and transitory components
        - Long-run and short-run volatility

        **FIGARCH (Fractionally Integrated GARCH):**
        - Long memory in volatility
        - Fractional integration parameter
        - Gradual decay of shocks

        **HYGARCH (Hyperbolic GARCH):**
        - Generalization of FIGARCH
        - Flexible persistence structure

        **Regime-Switching GARCH:**
        - Multiple volatility regimes
        - Markov-switching dynamics
        - Captures structural changes

        **Time-Varying Coefficient GARCH:**
        - Parameters evolve over time
        - Adapts to changing market conditions
        """)

    # Multivariate
    with st.expander("🔗 Multivariate GARCH 🔥", expanded=True):
        st.markdown("""
        ### System Volatility Modeling

        **BEKK Model:**
        - Ensures positive definite covariance matrix
        - Flexible cross-market spillovers
        - Computationally intensive

        **DCC-GARCH (Dynamic Conditional Correlation):**
        - Time-varying correlations
        - Two-step estimation (efficient)
        - Most popular multivariate GARCH

        **Model Structure:**
        """)

        st.latex(r"""
        H_t = D_t R_t D_t
        """)

        st.markdown("""
        Where:
        - Dₜ = diagonal matrix of conditional standard deviations
        - Rₜ = time-varying correlation matrix

        **GOGARCH (Generalized Orthogonal GARCH):**
        - Independent component analysis
        - Reduces dimensionality
        - Efficient estimation

        **CCC-GARCH (Constant Conditional Correlation):**
        - Constant correlations (simplification)
        - Computationally efficient
        - Benchmark model

        **Applications:**
        - Portfolio optimization
        - Risk management (VaR, CVaR)
        - Contagion analysis
        - Hedge ratios
        """)

        st.success(
            "✅ **Industry Standard**: DCC-GARCH is widely used in finance industry for portfolio risk management")

    # Integration
    with st.expander("🌟 GARCH Integration with Other Methods 🆕", expanded=True):
        st.markdown("""
        ### Hybrid GARCH Frameworks

        **ARDL-GARCH Models:**
        - Mean equation: ARDL for cointegration
        - Variance equation: GARCH for volatility
        - Captures both long-run relationships and volatility dynamics

        **Quantile-GARCH:**
        - Quantile regression in mean equation
        - GARCH variance specification
        - Distribution-dependent volatility

        **Wavelet-GARCH Decomposition:**
        - Decompose series using wavelets
        - Apply GARCH to each scale
        - Multi-scale volatility modeling
        - Separate noise from signal

        **Fourier-GARCH with Structural Breaks:**
        - Fourier approximation for breaks in mean
        - GARCH for conditional variance
        - Smooth transitions in volatility regimes

        **Applications:**
        - Energy price modeling with structural breaks
        - Financial crisis volatility analysis
        - Multi-scale risk assessment
        - Time-varying risk-return relationships
        """)

        st.markdown("""
        <div class="highlight-box">
        🔥 <strong>Cutting Edge:</strong> Hybrid GARCH models represent the frontier of 
        volatility research, combining multiple methodologies!
        </div>
        """, unsafe_allow_html=True)

    # Model Selection
    with st.expander("🎯 Model Selection & Diagnostics"):
        st.markdown("""
        ### Choosing and Validating GARCH Models

        **Information Criteria:**
        - AIC (Akaike Information Criterion)
        - BIC (Bayesian Information Criterion)
        - HQIC (Hannan-Quinn)

        **Standardized Residuals Tests:**
        - Ljung-Box test for serial correlation
        - ARCH-LM test for remaining ARCH effects
        - Jarque-Bera test for normality

        **Volatility Forecasting:**
        - One-step ahead forecasts
        - Multi-step ahead forecasts
        - Forecast evaluation metrics (MSE, MAE, QLIKE)

        **Best Practices:**
        - Start with GARCH(1,1) - often sufficient
        - Check for leverage effects (EGARCH/GJR)
        - Consider long memory (FIGARCH) if needed
        - Validate with out-of-sample forecasting
        """)

    # Software
    st.markdown("---")
    st.markdown("### 🛠️ Software Implementation")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **R Packages:**
        - `rugarch`: Comprehensive
        - `rmgarch`: Multivariate
        - `fGarch`: Extended models
        """)
    with col2:
        st.markdown("""
        **EViews:**
        - User-friendly GARCH
        - Built-in diagnostics
        - Extensive options
        """)
    with col3:
        st.markdown("""
        **MATLAB:**
        - Econometrics Toolbox
        - MFE Toolbox (Kevin Sheppard)
        """)

# Hybrid Applications
elif page == "🚀 Hybrid Applications":
    st.markdown('<p class="section-header">🚀 Advanced Hybrid Applications</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="method-card">
        <h3>🔥🔥 Comprehensive Framework Integration</h3>
        <p><strong>The Frontier:</strong> Combining multiple advanced methods creates powerful 
        frameworks that capture complex, multi-dimensional economic phenomena.</p>
    </div>
    """, unsafe_allow_html=True)

    # Module 1
    with st.expander("🎯 Module 1: Fourier-Quantile-ARDL Hybrid 🔥", expanded=True):
        st.markdown("""
        ### Triple Integration Framework

        **Combining Three Powerful Methods:**
        1. **Fourier Functions**: Smooth structural breaks
        2. **Quantile Regression**: Distribution-specific analysis
        3. **ARDL**: Flexible dynamics and mixed integration

        **Q-ARDL with Fourier Structural Breaks:**
        - Quantile-specific long-run relationships
        - Fourier approximation for smooth breaks
        - No need to specify break dates
        - Distribution-dependent structural changes

        **Scale and Location-Specific Dynamics:**
        - Different relationships at different quantiles
        - Time-varying across the distribution
        - Captures heterogeneity comprehensively

        **Asymmetric Adjustments with Smooth Transitions:**
        - Combine NARDL with Fourier-Quantile
        - Positive/negative asymmetries vary across quantiles
        - Structural breaks in asymmetric responses

        **Applications:**
        - Energy-growth nexus with policy regime changes
        - Income inequality dynamics over time
        - Climate change impacts across development levels
        - Financial market integration with crises
        """)

        st.markdown("""
        <div class="highlight-box">
        💎 <strong>Research Frontier:</strong> This triple combination is at the cutting edge 
        of econometric research, with few published applications!
        </div>
        """, unsafe_allow_html=True)

    # Module 2
    with st.expander("🌊 Module 2: Wavelet-NARDL with GARCH 🔥", expanded=True):
        st.markdown("""
        ### Multi-Scale Asymmetric Volatility Framework

        **Integration Strategy:**
        1. **Wavelet Decomposition**: Separate time scales
        2. **NARDL**: Asymmetric cointegration at each scale
        3. **GARCH**: Time-varying volatility at each scale

        **Multi-Scale Asymmetric Volatility:**
        - Different asymmetries at different time horizons
        - Short-run vs. long-run asymmetric volatility
        - Scale-specific risk analysis

        **Time-Frequency Conditional Heteroskedasticity:**
        - Volatility clustering across scales
        - Frequency-dependent GARCH effects
        - Complete risk characterization

        **Crisis Period Analysis:**
        - Identify crisis frequencies
        - Scale-specific contagion
        - Time-varying correlation during turmoil
        - Multi-horizon risk assessment

        **Practical Applications:**

        **Energy Markets:**
        - Short-term: Daily trading volatility with asymmetric responses
        - Medium-term: Seasonal patterns with NARDL
        - Long-term: Structural trends with GARCH persistence

        **Financial Contagion:**
        - High frequency: Intraday spillovers
        - Medium frequency: Weekly co-movements
        - Low frequency: Long-term integration

        **Climate Finance:**
        - Multiple time scales of climate risk
        - Asymmetric responses to extreme weather
        - Time-varying volatility of green assets
        """)

        st.success(
            "✅ **Power**: This framework captures asymmetries, structural changes, and volatility simultaneously across time scales!")

    # Module 3
    with st.expander("📊 Module 3: Rolling/Recursive Methods with All Tools 🔥", expanded=True):
        st.markdown("""
        ### Time-Varying Parameter Framework

        **Core Concept:**
        Apply ALL methods in rolling or recursive windows to capture time-varying parameters

        **Time-Varying Fourier Cointegration:**
        - Rolling window Fourier ARDL
        - Track evolution of structural breaks
        - Changing frequency components over time
        - Optimal window size selection

        **Rolling Wavelet Coherence:**
        - Time-varying coherence over time and frequency
        - Evolution of lead-lag relationships
        - Changing synchronization patterns
        - Crisis vs. normal period dynamics

        **Recursive Quantile Causality:**
        - Forward-expanding quantile causality tests
        - Tracks emergence/disappearance of causality
        - Distribution-specific causal evolution
        - Early warning system capabilities

        **Dynamic GARCH Parameters:**
        - Rolling estimation of GARCH models
        - Time-varying persistence
        - Changing leverage effects
        - Regime transition detection

        **Methodology:**
        """)

        st.markdown("""
        **Rolling Window:**
        - Fixed window size (e.g., 5 years)
        - Slides forward one period at a time
        - Produces time series of parameter estimates
        - Bootstrap confidence intervals

        **Recursive:**
        - Expanding window from start
        - Accumulates information over time
        - CUSUM and CUSUMSQ tests for stability
        - Identifies structural break timing
        """)

        st.markdown("""
        **Applications:**

        **Policy Regime Changes:**
        - Track parameter changes around policy interventions
        - Quantify effectiveness evolution
        - Identify optimal policy windows

        **Financial Crises Detection:**
        - Early warning indicators
        - Real-time stability monitoring
        - Regime shift identification

        **Time-Varying Elasticities:**
        - Price elasticity evolution
        - Income elasticity dynamics
        - Cross-price elasticity changes
        """)

    # Module 4
    with st.expander("🎯 Module 4: Complete Decision Framework", expanded=True):
        st.markdown("""
        ### Integrated Methodological Workflow

        **Step-by-Step Research Design:**

        **Phase 1: Initial Exploration**
        1. **Data Visualization**: Time plots, histograms, correlations
        2. **Descriptive Statistics**: Distribution properties, outliers
        3. **Wavelet Analysis**: Identify dominant frequencies and scales

        **Phase 2: Stationarity & Integration**
        1. **Classical Tests**: ADF, PP, KPSS
        2. **If structural breaks suspected**: Fourier unit root tests
        3. **If distribution concerns**: Quantile unit root tests
        4. **Decision**: Proceed to cointegration if I(1)

        **Phase 3: Cointegration Analysis**
        1. **Start with ARDL**: Bounds testing (most flexible)
        2. **If breaks present**: Fourier-ARDL
        3. **If asymmetry suspected**: NARDL or W-NARDL
        4. **If distribution matters**: Q-ARDL
        5. **If all of above**: Fourier-Quantile-NARDL hybrid

        **Phase 4: Causality Testing**
        1. **Time domain**: Granger causality or Toda-Yamamoto
        2. **With breaks**: Fourier causality
        3. **Frequency domain**: Wavelet causality
        4. **Distribution**: Quantile causality
        5. **Comprehensive**: Combine all approaches

        **Phase 5: Volatility Modeling**
        1. **Test for ARCH effects**: Ljung-Box, ARCH-LM
        2. **Choose GARCH specification**: Start with GARCH(1,1)
        3. **If asymmetry**: EGARCH or GJR-GARCH
        4. **If multivariate**: DCC-GARCH
        5. **Integration**: ARDL-GARCH, Wavelet-GARCH, etc.

        **Phase 6: Stability Analysis**
        1. **Rolling/recursive estimation**: All key parameters
        2. **CUSUM tests**: Identify break points
        3. **Bootstrap confidence bands**: Uncertainty quantification

        **Phase 7: Validation & Robustness**
        1. **Diagnostic tests**: Residual analysis, specification tests
        2. **Out-of-sample forecasting**: Predictive accuracy
        3. **Alternative specifications**: Sensitivity analysis
        4. **Robustness checks**: Different periods, frequencies
        """)

        st.markdown("""
        <div class="highlight-box">
        📋 <strong>Practical Wisdom:</strong> Not every study needs every method! 
        Choose based on research question, data properties, and theoretical foundation.
        </div>
        """, unsafe_allow_html=True)

    # Real Applications
    with st.expander("🌍 Real-World Application Examples"):
        st.markdown("""
        ### Case Studies Across Domains

        **Case 1: Energy-GDP Nexus (Complete Framework)**
        - Fourier-ARDL: Long-run with smooth breaks
        - W-NARDL: Multi-scale asymmetries
        - Wavelet coherence: Time-frequency relationships
        - DCC-GARCH: Volatility spillovers
        - Rolling quantile causality: Time-varying effects

        **Case 2: Financial Contagion Analysis**
        - Quantile cointegration: Tail dependence
        - Wavelet coherence: Crisis frequency identification
        - DCC-GARCH: Dynamic correlations
        - Quantile causality: Extreme event transmission

        **Case 3: Climate Change Economics**
        - Fourier cointegration: Gradual environmental changes
        - Quantile-ARDL: Different effects across countries
        - Wavelet analysis: Multiple climate cycles
        - NARDL: Asymmetric policy responses

        **Case 4: Monetary Policy Effectiveness**
        - Fourier-VECM: Policy regime breaks
        - Rolling ARDL: Time-varying transmission
        - Quantile causality: Distributional effects
        - GARCH-M: Risk-adjusted policy impacts
        """)

    # Software Integration
    st.markdown("---")
    st.markdown("### 🛠️ Integrated Software Workflow")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **Primary Tools:**
        - **R**: Most flexible, free, extensive packages
        - **MATLAB**: Best for wavelets and advanced numerics
        - **GAUSS**: Fourier methods (tspdlib)
        - **EViews**: User-friendly for NARDL/GARCH
        """)
    with col2:
        st.markdown("""
        **Workflow Strategy:**
        - Data preparation: R or Python
        - Unit roots & cointegration: R
        - Wavelets: MATLAB or R (biwavelet)
        - NARDL: EViews or R (nardl)
        - GARCH: R (rugarch) or EViews
        - Visualization: R (ggplot2)
        """)

# Course Overview
elif page == "🎯 Course Overview":
    st.markdown('<p class="section-header">🎯 Complete Course Structure</p>', unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        <h3>📚 Comprehensive Learning Journey</h3>
        <p>This course provides complete mastery of modern econometric methods, from classical foundations 
        to cutting-edge hybrid applications. Designed for researchers, data scientists, and economists 
        seeking advanced time series expertise.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Create curriculum overview
    st.markdown("## 📖 Curriculum Modules")

    modules = [
        {
            "module": "Unit Root & Stationarity",
            "icon": "📈",
            "topics": ["Classical Tests (ADF, PP, KPSS)", "Fourier Unit Root Tests", "Quantile Unit Root Tests"],
            "level": "Foundation → Advanced"
        },
        {
            "module": "Cointegration Methods",
            "icon": "🔗",
            "topics": ["Classical Methods", "ARDL Bounds Testing", "Fourier Cointegration", "Quantile Cointegration"],
            "level": "Core → Advanced"
        },
        {
            "module": "Fourier Methods",
            "icon": "🌊",
            "topics": ["Theory & Applications", "Fourier Unit Roots", "Fourier Cointegration", "Fourier VECM",
                       "Fourier Causality"],
            "level": "Advanced"
        },
        {
            "module": "Causality & VECM",
            "icon": "⚡",
            "topics": ["Fourier VECM", "Fourier Causality", "Quantile Causality", "Wavelet Causality"],
            "level": "Advanced"
        },
        {
            "module": "Nonlinear ARDL",
            "icon": "🔄",
            "topics": ["NARDL Framework", "Applications", "Q-ARDL", "Wavelet-NARDL"],
            "level": "Advanced → Frontier"
        },
        {
            "module": "Wavelet Analysis",
            "icon": "🌊",
            "topics": ["Wavelet Theory", "Decomposition", "Coherence", "Wavelet Causality", "Wavelet-Quantile"],
            "level": "Advanced → Frontier"
        },
        {
            "module": "Quantile Methods",
            "icon": "📊",
            "topics": ["Quantile Unit Roots", "Quantile Cointegration", "Q-ARDL", "Quantile Causality", "QQR"],
            "level": "Advanced"
        },
        {
            "module": "GARCH Models",
            "icon": "📈",
            "topics": ["Univariate GARCH", "Extensions", "Multivariate GARCH", "Hybrid GARCH"],
            "level": "Core → Advanced"
        },
        {
            "module": "Rolling & Recursive Methods",
            "icon": "🔄",
            "topics": ["Rolling Window ARDL", "Recursive ARDL", "Time-Varying Parameters", "Stability Analysis"],
            "level": "Advanced"
        },
        {
            "module": "Hybrid Applications",
            "icon": "🚀",
            "topics": ["Fourier-Quantile-ARDL", "Wavelet-NARDL-GARCH", "Rolling Integration", "Complete Framework"],
            "level": "Frontier"
        }
    ]

    for i, mod in enumerate(modules, 1):
        with st.expander(f"{mod['icon']} Module {i}: {mod['module']}", expanded=False):
            st.markdown(f"**Level**: {mod['level']}")
            st.markdown("**Key Topics:**")
            for topic in mod['topics']:
                st.markdown(f"- {topic}")

    st.markdown("---")

    # Learning Outcomes
    st.markdown("## 🎓 Learning Outcomes")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Technical Skills
        - ✅ Master all major unit root and cointegration tests
        - ✅ Apply Fourier methods for structural breaks
        - ✅ Conduct wavelet time-frequency analysis
        - ✅ Implement quantile econometric methods
        - ✅ Model asymmetries with NARDL
        - ✅ Estimate complete GARCH family
        - ✅ Integrate multiple methods into hybrid frameworks
        - ✅ Use rolling/recursive for time-varying analysis
        """)

    with col2:
        st.markdown("""
        ### Research Capabilities
        - ✅ Design sophisticated econometric studies
        - ✅ Choose appropriate methods for research questions
        - ✅ Interpret complex model outputs
        - ✅ Validate models with proper diagnostics
        - ✅ Apply methods to real economic data
        - ✅ Present findings effectively
        - ✅ Publish in top-tier journals
        - ✅ Conduct policy-relevant analysis
        """)

    st.markdown("---")

    # Software Proficiency
    st.markdown("## 🛠️ Software Proficiency")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        ### R Programming
        - urca, ARDL packages
        - quantreg, nardl
        - wavelets, biwavelet
        - rugarch, rmgarch
        - Custom functions
        """)

    with col2:
        st.markdown("""
        ### MATLAB
        - Wavelet Toolbox
        - Econometrics Toolbox
        - Custom implementations
        - Visualization tools
        """)

    with col3:
        st.markdown("""
        ### Other Tools
        - GAUSS (tspdlib)
        - EViews (NARDL/GARCH)
        - Python (alternative)
        - LaTeX (reporting)
        """)

    st.markdown("---")

    # Target Audience
    st.markdown("## 👥 Who Should Participate")

    audience = [
        {"title": "PhD Students",
         "description": "Writing dissertations in econometrics, finance, or applied economics"},
        {"title": "Researchers", "description": "Publishing in top-tier journals requiring advanced methods"},
        {"title": "Policy Analysts", "description": "Conducting rigorous policy evaluation and forecasting"},
        {"title": "Data Scientists", "description": "Working with economic and financial time series"},
        {"title": "Quantitative Analysts", "description": "Building sophisticated financial models"},
        {"title": "Central Bank Staff", "description": "Performing monetary policy and stability analysis"}
    ]

    cols = st.columns(3)
    for i, aud in enumerate(audience):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="info-box">
                <h4>{aud['title']}</h4>
                <p>{aud['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Prerequisites
    st.markdown("## 📋 Prerequisites")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        ### Required Background
        - Basic econometrics (OLS, hypothesis testing)
        - Time series fundamentals (stationarity, autocorrelation)
        - Statistical theory (distributions, inference)
        - Linear algebra basics
        - Programming experience (any language)
        """)

    with col2:
        st.markdown("""
        ### Recommended (Not Required)
        - Graduate-level econometrics
        - Experience with R or MATLAB
        - Published research experience
        - Familiarity with GARCH models
        - Knowledge of cointegration
        """)

    st.markdown("---")

    # Key Features
    st.markdown("## ⭐ Key Course Features")

    features = [
        {"icon": "🎯", "title": "Hands-On Learning", "desc": "Real data analysis with actual economic datasets"},
        {"icon": "💻", "title": "Code Provided", "desc": "Complete R, MATLAB, and GAUSS implementations"},
        {"icon": "📊", "title": "Practical Focus", "desc": "Applied examples from published research"},
        {"icon": "🔬", "title": "Research-Ready", "desc": "Methods ready for dissertation and publication"},
        {"icon": "📚", "title": "Comprehensive Materials", "desc": "Slides, code, papers, and datasets"},
        {"icon": "🤝", "title": "Ongoing Support", "desc": "Post-course consultation and resources"}
    ]

    cols = st.columns(3)
    for i, feat in enumerate(features):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="method-card" style="min-height: 150px;">
                <h3>{feat['icon']} {feat['title']}</h3>
                <p>{feat['desc']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("---")

    # Application Areas
    st.markdown("## 🌍 Application Domains")

    st.markdown("""
    **This course prepares you for research in:**

    - 💹 **Finance**: Asset pricing, volatility forecasting, portfolio management, risk analysis
    - 🏦 **Monetary Economics**: Policy transmission, interest rate dynamics, exchange rates
    - ⚡ **Energy Economics**: Energy-growth nexus, oil price analysis, renewable energy
    - 🌱 **Environmental Economics**: Climate change, pollution, sustainability
    - 📈 **Macroeconomics**: Business cycles, growth, inflation, unemployment
    - 🌐 **International Economics**: Trade, capital flows, currency markets
    - 🏛️ **Development Economics**: Growth determinants, inequality, poverty dynamics
    """)

    st.markdown("---")

    # Final Message
    st.markdown("""
    <div class="method-card">
        <h2 style="text-align: center; color: white;">🎓 Transform Your Research Capabilities</h2>
        <p style="text-align: center; font-size: 1.1rem;">
            Master the most advanced econometric methods and join the frontier of economic research. 
            This comprehensive program equips you with tools used in top journals and leading institutions worldwide.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #666; font-size: 0.9rem;">
        <strong>Advanced Econometric Methods</strong><br>
        Comprehensive Training Program<br>
        <br>
        📧 Contact for more information
    </p>
</div>
""", unsafe_allow_html=True)