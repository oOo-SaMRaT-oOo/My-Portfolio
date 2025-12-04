import streamlit as st
import base64

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

import os

def load_image_base64(path):
    abs_path = os.path.join(os.path.dirname(__file__), path)  # <— FIX HERE
    with open(abs_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


st.set_page_config(
    page_title = "Its me, Samrat Malla",
    page_icon = "👌",
)

st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/@studio-freight/lenis@1.0.36/bundled/lenis.min.js"></script>

<script>
const lenis = new Lenis({
    duration: 1.2,
    smooth: true,
    smoothTouch: true,  
    direction: 'vertical',
});

function raf(time) {
    lenis.raf(time);
    requestAnimationFrame(raf);
}
requestAnimationFrame(raf);
</script>
""", unsafe_allow_html=True)


st.markdown("""
<style>
.stApp { background: #0a0f1a; }  /* darker base */

.blob {
    position: fixed;
    width: 400px;
    height: 400px;
    border-radius: 50%;
    filter: blur(100px);
    opacity: 0.35;              
    z-index: 0;
    pointer-events: none;
    animation: float 20s infinite ease-in-out, pulse 12s infinite ease-in-out;
}

/* aesthetic dark tones with gradients */
#blob1 { 
    background: radial-gradient(circle at center, #0d3b66, #001f33); 
    top: 10%; left: 5%; 
    animation-duration: 22s; 
}
#blob2 { 
    background: radial-gradient(circle at center, #2e0f4f, #120022); 
    top: 65%; right: 8%; 
    animation-duration: 26s; 
    animation-name: float, pulse, spin; 
}
#blob3 { 
    background: radial-gradient(circle at center, #4a0d25, #1a000d); 
    bottom: 10%; left: 45%; 
    animation-duration: 30s; 
    animation-name: float, pulse, spin; 
}

/* float animation */
@keyframes float {
    0%, 100% { transform: translate(0,0) scale(1); }
    50%      { transform: translate(40px, -50px) scale(1.25); }
}

/* subtle pulsing glow */
@keyframes pulse {
    0%, 100% { opacity: 0.35; filter: blur(100px); }
    50%      { opacity: 0.55; filter: blur(120px); }
}

/* slow rotation */
@keyframes spin {
    0%   { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>

<div class="blob" id="blob1"></div>
<div class="blob" id="blob2"></div>
<div class="blob" id="blob3"></div>
""", unsafe_allow_html=True)





st.markdown("""
<style>
/* Smooth Fade */
.fade-in {
    animation: fadeIn 1.5s ease-in-out;
}
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

/* Glow Hover Card */
.card {
    padding: 20px;
    border-radius: 14px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    transition: 0.3s ease;
}
.card:hover {
    transform: translateY(-6px);
    box-shadow: 0px 6px 20px rgba(0,150,255,0.35);
}

/* Animated Title */
@keyframes slideIn {
    0% {opacity:0; transform:translateX(-50px);}
    100% {opacity:1; transform:translateX(0);}
}
.title-anim_1 {
    animation: slideIn 1s ease-out;
}

/* Background gradient */
body {
    background: linear-gradient(135deg,#0f172a,#001219,#072534);
    color: white;
}
</style>
""", unsafe_allow_html=True)


st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&display=swap');

    .title-anim {
        text-align: center;
        font-family: 'Pacifico', cursive;
        font-weight: normal;
        font-size: 48px;
        color: #333;
        animation: fadeIn 2s ease-in-out;
    }

    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

    <style>
    .big-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 110px !important;          /* way bigger */
        line-height: 1;
        margin: 0;
        padding: 0;
        text-align: center;
        color: #ffffff;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out;
    }
    @keyframes slideIn {
        from {opacity:0; transform:translateX(-100px);}
        to   {opacity:1; transform:translateX(0);}
    }
    </style>

    <div class="big-title">Samrat Malla</div>""",
    unsafe_allow_html=True
)

st.write("---")

c1,c2 = st.columns([5,3])
with c2:
    st.write("<br><br>",unsafe_allow_html=True)
    img_base64 = load_image_base64("Images/Profile.jpg")
    st.html(f"""
<style>
.animated-img {{
    animation: fadeIn 1.5s ease-in-out forwards;
    border-radius: 20px;
}}
@keyframes fadeIn {{
    from {{ opacity: 0; transform: translateY(30px); }}
    to   {{ opacity: 1; transform: translateY(0px); }}
}}
</style>

<img src="data:image/png;base64,{img_base64}" class="animated-img" width="300">
""")


    st.markdown(
    "<p class='title-anim' style='text-align:center; font-size:0.9em; color:gray;'>~ Its me Haha ... </p>",
    unsafe_allow_html=True
)   

with c1:
    st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.intro-text {
    font-family: 'Monotype Corsiva', cursive;
    font-size: 28px;
    color: #ffffff;
    line-height: 1;
    text-align: left;
    margin: 50px 20px;
    opacity: 0;
    transform: translateX(-100px);
    animation: slideIn 1.8s ease-out forwards, glow 3s ease-in-out infinite alternate 1.8s;
}

@keyframes slideIn {
    to { opacity: 1; transform: translateX(0); }
}

@keyframes glow {
    from { text-shadow: 0 0 12px #F4D03F; }
    to   { text-shadow: 0 0 30px #F39C12; }
}

.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="intro-text">~ Hi, I’m <span class="highlight-name"><span style="color:#F39C12;">Samrat Malla</span></span>,<br>
an Electrical Engineering student passionate about blending engineering with software.
I love using Python, simulations, and data-driven tools to solve real-world problems.
My goal is to become a <i>software-based electrical engineer</i> who builds impactful solutions.
I’m constantly learning and pushing myself to grow.
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <hr style="border: none; height: 4px; 
               background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """,
    unsafe_allow_html=True
)


st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

    <style>
    .welcome {
        font-family: 'Great Vibes', cursive !important;
        font-size: 45px !important;          /* way bigger */
        line-height: 1;
        margin: 0;
        padding: 0;
        text-align: left;
        color: #FFB6C1;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out;
    }
    @keyframes slideIn {
        from {opacity:0; transform:translateX(-100px);}
        to   {opacity:1; transform:translateX(0);}
    }
    </style>

    <div class="welcome"><br>Welcome to my Interactive Porfolio<br><br></div>""",
    unsafe_allow_html=True
)


st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.Normal-Text {
    font-family: 'Monotype Corsiva', cursive;
    font-size: 25px;          
    color: #ffffff;
    line-height: 1;
    text-align: left;
}
</style>
<div class="Normal-Text">Explore the sections of my portfolio 
using the navigation menu on the left. Each page reveals
a different part of my journey — who I am, what I build,
and what I’m learning.<br><br>
            . Dive into my projects to see how I blend engineering with software.<br>
. Discover simulations, Python apps, and creative tools I’ve designed.<br>
. Learn about the skills I’m sharpening and the challenges I’ve overcome.<br>
. Follow my vision of becoming a software-based electrical engineer.<br><br>

</div>
""", unsafe_allow_html=True)

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

<div class="butterfly">🦋</div>
<div class="butterfly" style="animation-delay: -12s; font-size: 25px;">🦋</div>
<div class="butterfly" style="animation-delay -25s; font-size: 30px; opacity: 0.7;">🦋</div>
""", unsafe_allow_html=True)





