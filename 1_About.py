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




st.set_page_config(page_title="Its About Me,", page_icon="👌")



def load_image_base64(path: str) -> str:
    """Load an image and return its Base64 string."""
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")



st.markdown("""
<style>
.stApp { background: #0d1117; }

.blob {
    position: fixed;
    width: 450px;
    height: 450px;
    border-radius: 50%;
    filter: blur(120px);
    opacity: 0.4;
    z-index: 0;
    pointer-events: none;
    animation: float 22s infinite ease-in-out;
}

#blob1 { background: #00ff88; }  /* neon mint */
#blob2 { background: #00d4ff; }  /* neon cyan */
#blob3 { background: #ff00ff; }  /* neon magenta */

@keyframes float {
    0%,100% { transform: translate(0,0) rotate(0deg); }
    50%     { transform: translate(50px,-60px) rotate(10deg) scale(1.3); }
}
</style>
<div class="blob" id="blob1"></div>
<div class="blob" id="blob2"></div>
<div class="blob" id="blob3"></div>
""", unsafe_allow_html=True)



st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

<style>
    .about-pulse-title {
        font-family: 'Great Vibes', cursive !important;
        font-size: 110px !important;
        line-height: 1;
        margin: 0;
        padding: 20px 0;
        text-align: center;
        background: linear-gradient(90deg, #ff7e5f, #feb47b, #ff6ec4, #9b5de5, #3a0ca3);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 25px rgba(255, 120, 180, 0.7), 0 0 50px rgba(255, 80, 120, 0.5);
        animation: fadeInUp 2s ease-out forwards,
                   pulseGlow 4s ease-in-out infinite,
                   gradientShift 10s ease infinite;
    }

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(100px); }
        to   { opacity: 1; transform: translateY(0); }
    }

    @keyframes pulseGlow {
        0%, 100% { text-shadow: 0 0 25px rgba(255, 120, 180, 0.7), 0 0 50px rgba(255, 80, 120, 0.5); }
        50%      { text-shadow: 0 0 50px rgba(255, 200, 255, 1), 0 0 100px rgba(255, 150, 200, 0.8); }
    }

    @keyframes gradientShift {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
</style>

<div class="about-pulse-title">About Me</div>
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
            In a Nutshell,</span><br>
            I’m an Electrical Engineering student who loves building real solutions through 
the blend of hardware, software, and creative engineering.  
I work with Python, simulations, and analytical thinking to understand systems, 
solve real-world problems, and design ideas that actually work.  
Every day, I’m learning, experimenting, and shaping myself into a software-based 
engineer ready for the future I’m building.
</div>
""", unsafe_allow_html=True)



st.markdown(
    """
    <hr style="border: none; height: 4px; 
               background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);">
    """,
    unsafe_allow_html=True
)

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
    Purpose in Motion :<br>
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

<div class="intro-text"><span style="color:#F39C12;"><br>
            Well ,</span><br>
            I aspire to create transformative solutions that benefit my country
 and drive progress across multiple fields, shaping technology, society, and innovation 
for a better tomorrow. My personal mission is to become a software-based electrical 
engineer who solves real-world challenges through programming, simulations, and smart 
engineering. I strive to grow every day — in discipline, skill, mindset, and impact — so 
I can build a future I’m proud of.
</div>
""", unsafe_allow_html=True)




st.markdown("---")

st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

    <style>
    .subheading {
        font-family: 'Great Vibes', cursive !important;
        font-size: 35px !important;          /* way bigger */
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

    <div class="subheading">Diving into my education :<br></div>""",
    unsafe_allow_html=True
)

st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

    <style>
    .subheading_1 {
        font-family: 'Great Vibes', cursive !important;
        font-size: 25px !important;          /* way bigger */
        line-height: 1;
        margin: 0;
        padding: 0;
        text-align: left;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out;
    }
    @keyframes slideIn {
        from {opacity:0; transform:translateX(-100px);}
        to   {opacity:1; transform:translateX(0);}
    }
    </style>

    <div class="subheading_1"><br>Bachelors Degree<br></div>""",
    unsafe_allow_html=True
)

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



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="normal-text"><br>
<span style="color:#3498DB ;"> University : </span> Pulchowk Campus <br>
<span style="color:#3498DB ;"> Address : </span> Pulchowk, Lalitpur <br>
<span style="color:#3498DB ;"> Major : </span> Electrical Engineering <br>
<span style="color:#3498DB ;"> GPA : </span> Currently Studying <br><br>
                
“ Learning to speak up, take responsibility, and work with people — whether it’s classroom 
projects, coding challenges, or helping friends in study groups. I’m discovering my 
strengths and slowly becoming a more confident engineer. ”



                
            
</div>
""", unsafe_allow_html=True)
    


with c2:
    img_base64 = load_image_base64(r"C:\Users\User\OneDrive\Documents\portfolio_app\pages\Pulchowk.jpeg")
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

<img src="data:image/jpeg;base64,{img_base64}" class="animated-img" width="300">
""")


    st.markdown(
    """
    <p class='title-anim' style='text-align:center; font-size:1em; color:gray;'>
        ~ <a href="https://pcampus.edu.np/" target="_blank" style="color:gray; text-decoration:none;">
            Pulchowk Campus
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
    
st.write("---")






st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

    <style>
    .subheading-high {
        font-family: 'Great Vibes', cursive !important;
        font-size: 25px !important;          /* way bigger */
        line-height: 1;
        margin: 0;
        padding: 0;
        text-align: left;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out;
    }
    @keyframes slideIn {
        from {opacity:0; transform:translateX(-100px);}
        to   {opacity:1; transform:translateX(0);}
    }
    </style>

    <div class="subheading-high"><br>High School <br></div>""",
    unsafe_allow_html=True
)

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



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="normal-text"><br>
<span style="color:#3498DB ;"> College : </span> Little Angel's College <br>
<span style="color:#3498DB ;"> Address : </span> Hattiban, Lalitpur <br>
<span style="color:#3498DB ;"> Major : </span> Physical Group <br>
<span style="color:#3498DB ;"> GPA : </span> 3.91 (10 + 2) <br><br>
                
“ Realizing that college wasn’t just about grades — it was about learning how to think, 
adapt, and build the foundation for the future I’m now working toward. ”



                
            
</div>
""", unsafe_allow_html=True)
    


with c2:
    img_base64 = load_image_base64(r"C:\Users\User\OneDrive\Documents\portfolio_app\LA.jpg")

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

<img src="data:image/jpeg;base64,{img_base64}" class="animated-img" width="300">
""")



    st.markdown(
    """
    <p class='title-anim' style='text-align:center; font-size:1em; color:gray;'>
        ~ Little Angels College
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
    
st.write("---")
    




st.markdown(
    """
    <link href="https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap" rel="stylesheet">

    <style>
    .subheading-high {
        font-family: 'Great Vibes', cursive !important;
        font-size: 25px !important;          /* way bigger */
        line-height: 1;
        margin: 0;
        padding: 0;
        text-align: left;
        text-shadow: 0 0 20px #00c6ff, 0 0 40px #0072ff;
        animation: slideIn 1.5s ease-out;
    }
    @keyframes slideIn {
        from {opacity:0; transform:translateX(-100px);}
        to   {opacity:1; transform:translateX(0);}
    }
    </style>

    <div class="subheading-high"><br>Schooling <br></div>""",
    unsafe_allow_html=True
)

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



.highlight-name:hover {
    color: #ff6b6b;
    text-shadow: 0 0 35px #F39C12;
    transform: scale(1.15);
    transition: all 0.4s;
}
</style>

<div class="normal-text"><br>
<span style="color:#3498DB ;"> School : </span> Little Angel's School <br>
<span style="color:#3498DB ;"> Address : </span> Hattiban, Lalitpur <br>
<span style="color:#3498DB ;"> Major : </span> Maths, Science, Computer <br>
<span style="color:#3498DB ;"> GPA : </span> 3.80 (10th) <br><br>
                
“ Looking back, school was where I first learned to dream, to try, and to believe in 
something bigger — and every small step, every class, every mistake along the way quietly
 shaped the confidence I carry forward today. ”



                
            
</div>
""", unsafe_allow_html=True)
    


with c2:
    img_base64 = load_image_base64(r"C:\Users\User\OneDrive\Documents\portfolio_app\laschool.jpg")
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

<img src="data:image/jpeg;base64,{img_base64}" class="animated-img" width="300">
""")


    st.markdown(
    """
    <p class='title-anim' style='text-align:center; font-size:1em; color:gray;'>
        ~ <a href="https://www.las.edu.np/" target="_blank" style="color:gray; text-decoration:none;">
            Little Angel's School
        </a>
    </p>
    """,
    unsafe_allow_html=True
)
    
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

<div class="butterfly">🌟</div>
<div class="butterfly" style="animation-delay: -12s; font-size: 25px;">🌟</div>
<div class="butterfly" style="animation-delay -25s; font-size: 30px; opacity: 0.7;">🌟</div>
""", unsafe_allow_html=True)





