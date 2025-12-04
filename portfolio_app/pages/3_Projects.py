import streamlit as st
import base64


st.set_page_config(page_title="Projects", page_icon="🚀")

def load_image_base64(path: str) -> str:
    """Load an image and return its Base64 string."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    


st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap');

    /* Your beautiful sidebar */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg,#0c1b33,#172a45);
        box-shadow: 0 0 20px #00b7ff;
        backdrop-filter: blur(10px);
    }
    [data-testid="stSidebar"], [data-testid="stSidebar"] * {
        font-family: 'Dancing Script', cursive !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        color: #a0e7ff !important;
        text-shadow: 0 0 10px #00b7ff;
    }
    [data-testid="stSidebarNavLink"][aria-selected="true"] {
        background: #00b7ff33 !important;
        border-left: 5px solid #00ffff;
    }
    [data-testid="stSidebarNavLink"]:hover {
        background: #00ffff33 !important;
    }

    /* ONLY removes the ugly black bar — sidebar still works 100% */
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
        box-shadow: none !important;
    }
    /* Hide only the dark background, not the collapse button */
    [data-testid="stHeader"]::before,
    [data-testid="stHeader"]::after {
        background: none !important;
    }
</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>
.stApp { background: #0d001a; overflow: hidden; }

.wave {
    position: fixed;
    width: 600px;
    height: 600px;
    border-radius: 50%;
    filter: blur(150px);
    opacity: 0.45;
    z-index: 0;
    pointer-events: none;
    animation: sweep 30s infinite linear;
}

#wave1 { background: #ff0040; left: -10%; top: 20%; }   /* neon red */
#wave2 { background: #ff8c00; left: -10%; top: 50%; animation-delay: -10s; } /* neon orange */
#wave3 { background: #ffd000; left: -10%; top: 80%; animation-delay: -20s; } /* neon yellow */

@keyframes sweep {
    0%   { transform: translateX(-200px); }
    100% { transform: translateX(calc(100vw + 800px)); }
}
</style>
<div class="wave" id="wave1"></div>
<div class="wave" id="wave2"></div>
<div class="wave" id="wave3"></div>
""", unsafe_allow_html=True)




st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .cyber-glow-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 110px !important;
        line-height: 1;
        margin: 0;
        padding: 20px 0;
        text-align: center;
        background: linear-gradient(90deg, #00ffff, #00ff88, #ff00ff, #ffff00, #ff0055);
        background-size: 500% 500%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 30px rgba(0,255,255,0.8), 0 0 60px rgba(255,0,255,0.6);
        animation: glideIn 2s ease-out forwards,
                   pulseGlow 4s ease-in-out infinite,
                   rainbowFlow 10s linear infinite;
    }

    @keyframes glideIn {
        from { opacity: 0; transform: translateY(100px) rotate(-8deg) scale(0.7); }
        to   { opacity: 1; transform: translateY(0) rotate(0deg) scale(1); }
    }

    @keyframes pulseGlow {
        0%,100% { text-shadow: 0 0 30px rgba(0,255,255,0.8), 0 0 60px rgba(255,0,255,0.6); }
        50%     { text-shadow: 0 0 60px rgba(0,255,255,1), 0 0 100px rgba(255,0,255,1), 0 0 140px rgba(0,255,0,0.7); }
    }

    @keyframes rainbowFlow {
        0%   { background-position: 0% 50%; }
        100% { background-position: 500% 50%; }
    }
</style>

<div class="cyber-glow-title">My Projects</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.fade-in-text {
    font-family: 'Monotype Corsiva', cursive;
    font-size: 25px;
    color: #ffffff;
    line-height: 1;
    text-align: left;
    opacity: 0;
    transform: translateX(-100px);
    animation: slideIn 1.8s ease-out forwards, glow 3s ease-in-out infinite alternate 1.8s;
}

@keyframes slideIn {
    to { opacity: 1; transform: translateX(0); }
}

.name-glow:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="fade-in-text">Welcome to my project showcase — a collection of work where engineering,
coding, and creativity come together. Each project reflects my journey of learning,
building, and solving real-world problems through software and simulation. Dive in and
explore how I bring ideas to life with Python and a passion for innovation.
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .my-purpose-title-2025 {
        font-family: 'Great Vibes', cursive !important;
        font-size: 48px !important;
        line-height: 1.1;
        margin: 0 !important;
        padding: 10px 0 !important;
        text-align: left;
        color: #FFB6C1 !important;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        opacity: 0;                     /* Start hidden */
        transform: translateX(-120px);  /* Start off-screen */
        animation: slideIn 1.8s ease-out forwards;
    }

    @keyframes slideInPurpose {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
</style>

<div class="my-purpose-title-2025">
    Data Analyzer :<br>
</div>
""", unsafe_allow_html=True)

c1,c2 = st.columns([5,3])
with c1:
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

    .normal-text {
        font-family: 'Monotype Corsiva', cursive;
        font-size: 25px;
        color: #ffffff;
        line-height: 1;
        text-align: left;
        opacity: 0;
        transform: translateX(-100px);
        animation: slideIn 1.8s ease-out forwards, glow 3s ease-in-out infinite alternate 1.8s;
    }

    @keyframes slideIn {
        to { opacity: 1; transform: translateX(0); }
    }

    .github-link {
        display: inline-block;
        margin-top: 20px;
        color: #00ff9f;
        font-size: 26px;
        text-decoration: none;
        font-weight: bold;
        text-shadow: 0 0 15px #00ff9f;
        transition: all 0.3s;
    }

    .github-link:hover {
        color: #ff00ff;
        text-shadow: 0 0 25px #ff00ff;
        transform: scale(1.1);
    }
    </style>

    <div class="normal-text"><br>
    Data Analyzer is a Python-built Streamlit web app that 
    lets users upload Excel files and instantly visualize data through
    bar charts, 2D plots, and trend graphs. It also provides statistical 
    analysis, forecasting, interpolation, and normalized comparisons — making 
    data exploration simple, fast, and effective.<br><br>
                
    <a href="https://datavisualizerappbysamratmalla.streamlit.app/" target="_blank" class="github-link">
    View App → 
    </a>
    <br>
    <a href="https://github.com/oOo-SaMRaT-oOo/Data-Visualizer-App" target="_blank" class="github-link">
    View Code →
    </a>
                
    
                
    </div>
    """, unsafe_allow_html=True)
    
    
    


with c2:
    img_base64 = load_image_base64(r"portfolio_app/pages/Images/Data_Analyzer.jpeg")
    st.html(f"""
<style>
.fade-up-img {{
    animation: fadeInUp 1.5s ease-out forwards;
    border-radius: 20px;
}}
@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(40px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
</style>

<img src="data:image/jpeg;base64,{img_base64}" class="fade-up-img" width="300">
""")

    
st.write("---")





st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .my-purpose-title-2025 {
        font-family: 'Great Vibes', cursive !important;
        font-size: 48px !important;
        line-height: 1.1;
        margin: 0 !important;
        padding: 10px 0 !important;
        text-align: left;
        color: #FFB6C1 !important;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        opacity: 0;                     /* Start hidden */
        transform: translateX(-120px);  /* Start off-screen */
        animation: slideIn 1.8s ease-out forwards;
    }

    @keyframes slideInPurpose {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
</style>

<div class="my-purpose-title-2025">
    Rlc Analyzer :<br>
</div>
""", unsafe_allow_html=True)

c1,c2 = st.columns([5,3])
with c1:
    st.html("""
<link href="https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap" rel="stylesheet">

<style>
    .normal-text {
        font-family: 'Monotype Corsiva', cursive;
        font-size: 25px;
        color: #ffffff;
        line-height: 1.4;
        text-align: left;
        opacity: 0;
        transform: translateX(-100px);
        animation: slideIn 1.8s ease-out forwards, glow 3s ease-in-out infinite alternate 1.8s;
    }

    @keyframes slideIn {
        to { opacity: 1; transform: translateX(0); }
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #00ff9f; }
        to { text-shadow: 0 0 20px #ff00ff; }
    }

    .github-link {
        display: inline-block;
        margin-top: 20px;
        color: #00ff9f;
        font-size: 26px;
        text-decoration: none;
        font-weight: bold;
        text-shadow: 0 0 15px #00ff9f;
        transition: all 0.3s;
    }

    .github-link:hover {
        color: #ff00ff;
        text-shadow: 0 0 25px #ff00ff;
        transform: scale(1.1);
    }
</style>

<div class="normal-text">
    <br>The RLC Analyzer is an interactive Streamlit application that lets you explore 
    and simulate the behavior of series RLC circuits. By combining symbolic math with
    real-time visualization, the app helps you analyze current, voltage, resonance, 
    damping, and system response with ease. Just input your circuit parameters and 
    instantly see both the mathematical solution and its graphical interpretation.<br><br>
            
    <a href="https://rlcanalyzerappbysamratmalla.streamlit.app/" target="_blank" class="github-link">
    View App →
    </a>
    <br>
    <a href="https://github.com/oOo-SaMRaT-oOo/RLC-Analyzer-App" target="_blank" class="github-link">
    View Code →
    </a>
</div>
""")
    
    


with c2:
    img_base64 = load_image_base64(r"portfolio_app/pages/Images/RLC.jpg")
    st.html(f"""
<style>
.fade-in-slide {{
    animation: fadeInUp 1.5s ease-out forwards;
    border-radius: 20px;
}}
@keyframes fadeInUp {{
    from {{ opacity: 0; transform: translateY(40px); }}
    to   {{ opacity: 1; transform: translateY(0); }}
}}
</style>

<img src="data:image/jpeg;base64,{img_base64}" class="fade-in-slide" width="300">
""")

    
st.write("---")











st.markdown("""
<style>
/* Flying butterfly emoji – works perfectly */
.butterfly {
    position: fixed;
    font-size: 20px;
    pointer-events: none;
    z-index: 10;
    animation: fly 38s infinite linear;
    opacity: 0.9;
    filter: drop-shadow(0 0 15px #00ffff);
    user-select: none;
}

@keyframes fly {
    0%   { left: -10%; top: 20%; transform: rotate(20deg); }
    15%  { left: 25%;  top: 70%; transform: rotate(-50deg); }
    35%  { left: 65%;  top: 15%; transform: rotate(80deg) scaleX(-1); }
    55%  { left: 90%;  top: 75%; transform: rotate(-40deg) scaleX(-1); }
    75%  { left: 35%;  top: 85%; transform: rotate(60deg); }
    100% { left: -10%; top: 20%; transform: rotate(20deg); }
}
</style>

<div class="butterfly">🔧</div>
<div class="butterfly" style="animation-delay: -12s; font-size: 35px;">🔧</div>
<div class="butterfly" style="animation-delay -12s; font-size: 40px; opacity: 0.7;">🔧</div>

            

""", unsafe_allow_html=True)

