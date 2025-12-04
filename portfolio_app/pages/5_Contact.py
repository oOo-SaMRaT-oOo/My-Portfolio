import streamlit as st

st.set_page_config(page_title="Contact Me,", page_icon="📞")

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
.stApp {
    background: radial-gradient(circle at 50% 50%, #1a0033 0%, #000000 70%);
    overflow: hidden;
}

.glow-orb {
    position: fixed;
    width: 700px;
    height: 700px;
    border-radius: 50%;
    filter: blur(200px);
    opacity: 0.4;
    z-index: 0;
    pointer-events: none;
    animation: drift 45s infinite ease-in-out;
}

#orb1 { background: #ff0a6c; bottom: -10%; left: -15%; animation-delay: 0s; }
#orb2 { background: #006fff; top: -20%; right: -10%; animation-delay: -15s; }
#orb3 { background: #00ff9f; top: 10%; left: 50%; animation-delay: -30s; }

@keyframes drift {
    0%,100% { transform: translate(0,0) rotate(0deg) scale(1); }
    33%     { transform: translate(100px,-120px) rotate(8deg) scale(1.3); }
    66%     { transform: translate(-80px,100px) rotate(-6deg) scale(0.9); }
}
</style>
<div class="glow-orb" id="orb1"></div>
<div class="glow-orb" id="orb2"></div>
<div class="glow-orb" id="orb3"></div>
""", unsafe_allow_html=True)




st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .contact-slide-top {
        font-family: 'Great Vibes', cursive !important;
        font-size: 110px !important;
        line-height: 1;
        margin: 0;
        padding: 20px 0;
        text-align: center;
        background: linear-gradient(90deg, #ff00ff, #00ffff, #00ff9d);
        background-size: 200% 200%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: slideInTop 1.8s ease-out forwards,
                   simpleGlow 4s ease-in-out infinite;
    }

    @keyframes slideInTop {
        from { opacity: 0; transform: translateY(-100px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes simpleGlow {
        0%, 100% { background-position: 0% 50%; }
        50%      { background-position: 100% 50%; }
    }
</style>

<div class="contact-slide-top">Contact Me</div>
""", unsafe_allow_html=True)

st.markdown("---")


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

<div class="intro-text"><span style="color:#F39C12;">
            Well ,</span><br>
Feel free to reach out! I’m usually active on social media between 5:00 PM and
8:30 PM. For anything important or urgent, email or phone calls are the best way to
contact me. I’ll get back to you as soon as possible
</div>
""", unsafe_allow_html=True)

st.write("---")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .my-purpose-title-2025 {
        font-family: 'Great Vibes', cursive !important;
        font-size: 25px !important;
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
    <style>
  a {
    text-decoration: none;
    color: #0077cc; /* calm blue */
    font-weight: bold;
    transition: 0.3s;
  }
  a:hover {
    color: #ff6600; /* playful orange glow */
    text-shadow: 0px 0px 8px rgba(255, 102, 0, 0.6);
  }
</style>

📧 Email Address : &nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://mail.google.com/mail/?view=cm&fs=1&to=samratmalla2006@gmail.com" target="_blank">
    samratmalla2006@gmail.com
</a>
<br><br>

🌐 Facebook Link : &nbsp;&nbsp;&nbsp;&nbsp;
<a href="https://www.facebook.com/samrat.malla.591855" target="_blank">
    Samrat Malla </a><br><br>
            
🐛 GitHub Link : &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://github.com/oOo-SaMRaT-oOo" target="_blank">oOo-Samrat-oOo </a><br>
                
</div>
""", unsafe_allow_html=True)


st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .my-purpose-title-2025 {
        font-family: 'Great Vibes', cursive !important;
        font-size: 25px !important;
        line-height: 1.1;
        margin: 0 !important;
        padding: 10px 0 !important;
        text-align: left;
        color: #FFB6C1 !important;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        opacity: 0;
        transform: translateX(-120px);
        animation: slideInPurpose 1.8s ease-out forwards;
    }

    @keyframes slideInPurpose {
        to {
            opacity: 1;
            transform: translateX(0);
        }
    }

    a {
        text-decoration: none;
        color: #0077cc;
        font-weight: bold;
        transition: 0.3s;
    }
    a:hover {
        color: #ff6600;
        text-shadow: 0px 0px 8px rgba(255, 102, 0, 0.6);
    }

    .schoolbook-number {
        font-family: 'Century Schoolbook', 'Georgia', serif;
        font-size: 25px;
        color: #FFD700;
    }
</style>

<div class="my-purpose-title-2025">
☎️ Contact Number : <span class="schoolbook-number">9861194754</span>
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

<div class="butterfly">📞</div>
<div class="butterfly" style="animation-delay: -12s; font-size: 35px;">📞</div>
<div class="butterfly" style="animation-delay -12s; font-size: 40px; opacity: 0.7;">📞</div>

            
""", unsafe_allow_html=True)




