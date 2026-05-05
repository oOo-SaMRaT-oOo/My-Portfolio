import streamlit as st

st.set_page_config(page_title="My Interests,", page_icon="📞")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@600&display=swap');

    /* 1. Dynamic Width Logic - Shrunk by default, expands on hover */
    [data-testid="stSidebar"] {
        /* Adjusted width to fit "Interests" comfortably in shrunk mode */
        width: 160px !important; 
        min-width: 160px !important;
        background: rgba(12, 27, 51, 0.8) !important;
        backdrop-filter: blur(15px) saturate(180%);
        border-right: 1px solid rgba(0, 183, 255, 0.3);
        box-shadow: 10px 0 30px rgba(0,0,0,0.5);
        
        /* Smooth transition for the 'opening' effect */
        transition: width 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275), 
                    min-width 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    /* Expands to normal size when mouse enters sidebar area */
    [data-testid="stSidebar"]:hover {
        width: 320px !important;
        min-width: 320px !important;
    }

    /* 2. Text and Font Styling */
    [data-testid="stSidebar"], [data-testid="stSidebar"] * {
        font-family: 'Dancing Script', cursive !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        color: #a0e7ff !important;
        text-shadow: 0 0 10px #00b7ff;
        white-space: nowrap; /* Prevents text wrapping when narrow */
    }

    /* 3. INTERACTIVE NAVIGATION */
    [data-testid="stSidebarNavLink"] {
        border-radius: 12px;
        margin: 8px 12px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    }

    [data-testid="stSidebarNavLink"]:hover {
        background: rgba(0, 255, 255, 0.15) !important;
        transform: translateX(8px) scale(1.02);
        box-shadow: -5px 0px 15px rgba(0, 255, 255, 0.4);
        color: #ffffff !important;
    }

    [data-testid="stSidebarNavLink"][aria-selected="true"] {
        background: linear-gradient(90deg, rgba(0,183,255,0.3), transparent) !important;
        border-left: 5px solid #00ffff !important;
        text-shadow: 0 0 15px #00ffff;
    }

    /* --- THE KILLER FIXES FOR "KEYBOARD" / TOGGLE TEXT --- */
    [data-testid="stSidebar"] button span,
    [data-testid="stSidebar"] div[class*="st-key"],
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
        font-size: 0 !important;
        visibility: hidden !important;
    }

    /* Cleanup Header */
    header[data-testid="stHeader"] {
        background: rgba(0,0,0,0) !important;
        box-shadow: none !important;
    }
</style>
""", unsafe_allow_html=True)





st.markdown("""
<style>
.stApp { 
    background: #0a0720; 
    overflow: hidden; 
}

.glow-orb {
    position: fixed;
    width: 800px;
    height: 800px;
    border-radius: 50%;
    filter: blur(140px);
    opacity: 0.7;
    z-index: 0;
    pointer-events: none;
    animation: drift 35s infinite linear;
}

/* Darker orb colors */
#orb1 { background: #004466; left: -20%; top: 5%; }       /* deep cyan */
#orb2 { background: #660033; left: -20%; top: 40%; animation-delay: -12s; } /* dark magenta */
#orb3 { background: #004d40; left: -20%; top: 75%; animation-delay: -24s; } /* dark teal-green */

@keyframes drift {
    0%   { transform: translateX(-400px) translateY(0); }
    100% { transform: translateX(calc(100vw + 1200px)) translateY(-300px); }
}
</style>
<div class="glow-orb" id="orb1"></div>
<div class="glow-orb" id="orb2"></div>
<div class="glow-orb" id="orb3"></div>
""", unsafe_allow_html=True)







st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .neon-elegant-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 108px !important;
        line-height: 1;
        margin: 0;
        padding: 20px 0;
        text-align: center;
        background: linear-gradient(90deg, #00d4ff, #8a2be2, #ff1493, #00ffb8);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px #00d4ff55, 0 0 50px #8a2be299;
        animation: slideUp 2.2s ease-out forwards,
                   gentlePulse 5s ease-in-out infinite,
                   flowColor 12s linear infinite;
    }

    @keyframes slideUp {
        from { opacity: 0; transform: translateY(90px) scale(0.8); }
        to   { opacity: 1; transform: translateY(0) scale(1); }
    }

    @keyframes gentlePulse {
        0%,100% { text-shadow: 0 0 20px #00d4ff55, 0 0 50px #8a2be299; }
        50%     { text-shadow: 0 0 35px #00d4ff88, 0 0 70px #ff1493bb, 0 0 100px #00ffb877; }
    }

    @keyframes flowColor {
        0%   { background-position: 0% 50%; }
        100% { background-position: 400% 50%; }
    }
</style>

<div class="neon-elegant-title">Me Beyond Engineering</div>
""", unsafe_allow_html=True)

st.write("---")




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
“ We are more than what we study — engineering sharpens my mind, 
but passions beyond it shape who I am, because everyone has a life beyond equations
and deadlines. ”
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
    🎶 Life Woven in Notes & Beats 🎸 <br>
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

    <div class="intro-text"><br>
    “ Since childhood, music has been my companion — guitar in hand,
    voice singing, helping me through tough times and shaping who I am today. 
    It’s more than a passion; it’s a way to connect with others and express what 
    words cannot. ”
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
    🏃‍♂️ Beyond Desk, Fitness Journey ⏱️<br>
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

    <div class="intro-text"><br>
    “ I began my fitness journey with a determination to push my 
            limits, build strength, and cultivate discipline and resilience. 
            Fitness isn’t just a routine — it’s a way to challenge myself, grow 
            stronger every day, and embrace the power of consistency in both body 
            and mind. ”
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
🚀Forever Learner, Journey of Growth🔥<br>
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

    <div class="intro-text"><br>
    “ I am committed to continuous learning and self-improvement, always seeking 
            new knowledge and skills to expand my mind and abilities. Growth isn’t a 
            destination — it’s a lifelong journey, one that challenges me, sharpens 
            my perspective, and shapes me into the best version of myself every day. ”
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

<div class="butterfly">🔍</div>
<div class="butterfly" style="animation-delay: -12s; font-size: 35px;">🔍</div>
<div class="butterfly" style="animation-delay -12s; font-size: 40px; opacity: 0.7;">🔍</div>

            
""", unsafe_allow_html=True)
