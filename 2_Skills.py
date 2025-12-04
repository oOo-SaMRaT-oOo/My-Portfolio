import streamlit as st

st.set_page_config(page_title="Skills", page_icon="🧠")

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
.stApp {background:#0d001a;}  /* deep cosmic purple-black */

.cosmic-blob {
    position:fixed;
    border-radius:50%;
    filter:blur(180px);
    opacity:0.32;
    z-index:0;
    pointer-events:none;
    animation:drift 50s infinite ease-in-out;
}

/* Different sizes & positions */
#b1 {width:800px; height:800px; top:-10%; left:-15%; background:#ff2e63;}     /* neon pink */
#b2 {width:650px; height:650px; top:10%; right:-10%; background:#08f7fe;}     /* electric cyan */
#b3 {width:900px; height:900px; bottom:-20%; left:10%; background:#9d00ff;}    /* vivid purple */
#b4 {width:550px; height:550px; top:15%; left:45%; background:#ffea00;}       /* acid yellow */
#b5 {width:700px; height:700px; bottom:5%; right:20%; background:#00ff9d;}    /* mint green */

@keyframes drift {
    0%   {transform:translate(0,0) rotate(0deg);}
    25%  {transform:translate(80px,-120px) rotate(90deg);}
    50%  {transform:translate(-100px,80px) rotate(180deg);}
    75%  {transform:translate(60px,100px) rotate(270deg);}
    100% {transform:translate(0,0) rotate(360deg);}
}
</style>

<div class="cosmic-blob" id="b1"></div>
<div class="cosmic-blob" id="b2"></div>
<div class="cosmic-blob" id="b3"></div>
<div class="cosmic-blob" id="b4"></div>
<div class="cosmic-blob" id="b5"></div>
""", unsafe_allow_html=True)



st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .vibes-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 110px !important;
        line-height: 1;
        text-align: center;
        margin: 0;
        padding: 20px 0;
        background: linear-gradient(90deg, #d8b4fe, #f0abfc, #fca5a5, #fed7aa);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 12px rgba(236, 146, 255, 0.5);
        animation: fadeIn 2s ease-out,
                   gentleGlow 5s ease-in-out infinite alternate,
                   gradientMove 15s ease infinite;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(60px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes gentleGlow {
        from { text-shadow: 0 0 12px rgba(236, 146, 255, 0.5); }
        to   { text-shadow: 0 0 20px rgba(236, 146, 255, 0.7); }
    }

    @keyframes gradientMove {
        0%, 100% { background-position: 0% 50%; }
        50%      { background-position: 100% 50%; }
    }
</style>

<div class="vibes-title">My Skills</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .slide-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 48px !important;
        line-height: 1.1;
        margin: 0 !important;
        padding: 10px 0 !important;
        text-align: left;
        color: #FFB6C1 !important;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        opacity: 0;
        transform: translateX(-120px);
        animation: slideIn 1.8s ease-out forwards;
    }

    @keyframes slideIn {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
</style>

<div class="slide-title">
    Academic Skills :<br>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.intro-text {
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



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="intro-text">
. Programming & Simulation: Hands-on experience in Python 
for problem-solving, simulation, and data analysis. <br><br>

. Scientific Computing: Proficient with core scientific and mathematical 
Python libraries — NumPy, Pandas, Matplotlib, SciPy, SymPy, and Streamlit.<br>

. Strong Theoretical Foundation: Solid understanding of key engineering 
subjects — Mathematics, Physics, Chemistry, Applied Mechanics, Electric Circuits, 
and Electronic Circuits. <br>

. Applied AI: Utilized AI and automation techniques to streamline tasks, 
enhance efficiency, and support effective time management. <br>

</div>
""", unsafe_allow_html=True)

st.markdown("---")






st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .slide-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 48px !important;
        line-height: 1.1;
        margin: 0 !important;
        padding: 10px 0 !important;
        text-align: left;
        color: #FFB6C1 !important;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        opacity: 0;
        transform: translateX(-120px);
        animation: slideIn 1.8s ease-out forwards;
    }

    @keyframes slideIn {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
</style>

<div class="slide-title">
    Software Skills :<br>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.intro-text {
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



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="intro-text">
<span style="color:#F39C12;"><br>
Software Proficiency ,</span><br>
            . Python <br>
            . C programming <br>
            . Filmora { Heavy Video Editing }<br>
            . Microsoft Office { Word , Excel, Powerpoint }<br>
            . Microsoft Clipchamp { Light Video Editing }<br>
            . Sora-OPENAI { Photo Editing } <br>

</div>
""", unsafe_allow_html=True)


st.write("---")





st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .slide-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 48px !important;
        line-height: 1.1;
        margin: 0 !important;
        padding: 10px 0 !important;
        text-align: left;
        color: #FFB6C1 !important;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        opacity: 0;
        transform: translateX(-120px);
        animation: slideIn 1.8s ease-out forwards;
    }

    @keyframes slideIn {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }
</style>

<div class="slide-title">
    Language Skills :<br>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Monotype+Corsiva&display=swap');

.intro-text {
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



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="intro-text">
<span style="color:#F39C12;"><br>
Language Proficiency ,</span><br>
            . English { Fluent } <br>
            . German { Learning } <br>
            . Nepali { Native / Fluent } <br>
            . Hindi { Conversational } <br>
            . Newari { Conversational } <br>

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

<div class="butterfly">⚡</div>
<div class="butterfly" style="animation-delay: -12s; font-size: 35px;">⚡</div>
<div class="butterfly" style="animation-delay -12s; font-size: 40px; opacity: 0.7;">⚡</div>

            
""", unsafe_allow_html=True)



    