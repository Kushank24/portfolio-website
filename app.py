import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Kushank Maheshwari - Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS with refined styling
st.markdown(
    """
    <style>
        /* Main container styling */
        .block-container {
            padding: 1rem 3rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Custom fonts and colors */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .centered {
            display: flex;
            justify-content: center;
            align-items: center;
            flex-direction: column;
            text-align: center;
            color: #333;
        }
        
        /* Profile section styling */
        .profile-img {
            border-radius: 50%;
            border: 3px solid #f0f2f6;
            padding: 3px;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 180px;
            height: 180px;
            object-fit: cover;
        }
        
        /* Header styling */
        h1 {
            color: #1a202c;
            font-weight: 700;
            font-size: 2.5rem !important;
            text-align: center;
            margin-bottom: 0.5rem !important;
        }
        
        h2 {
            color: #1a202c;
            font-weight: 600;
            font-size: 1.75rem !important;
            margin-top: 2rem !important;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e2e8f0;
        }
        
        h3 {
            color: #2d3748;
            font-weight: 600;
            font-size: 1.25rem !important;
            margin-bottom: 0.5rem !important;
        }
        
        /* Section styling */
        .section {
            background-color: #ffffff;
            padding: 1.5rem;
            margin: 0; /* Remove margin */
            border-left: 4px solid #3182ce;
            transition: all 0.3s ease;
        }
        
        .section:hover {
            border-left-color: #2b6cb0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }
        
        /* Links styling */
        a {
            color: #3182ce !important;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.2s ease;
        }
        
        a:hover {
            color: #2b6cb0 !important;
            text-decoration: none;
        }
        
        /* List styling */
        ul {
            list-style-type: none;
            padding-left: 0;
            margin-top: 0.5rem;
        }
        
        li {
            margin: 0.75rem 0;
            padding-left: 1.25rem;
            position: relative;
            line-height: 1.5;
        }
        
        li:before {
            content: "→";
            color: #3182ce;
            position: absolute;
            left: 0;
            font-size: 0.9em;
        }
        
        /* Contact info styling */
        .contact-info {
            text-align: center;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 4px;
            background: linear-gradient(to right, #f7fafc, #edf2f7);
        }
        
        .contact-info a {
            margin: 0 0.5rem;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            display: inline-block;
        }
        
        /* Text styling */
        p {
            color: #4a5568;
            line-height: 1.6;
            margin-bottom: 0.75rem;
        }
        
        em {
            color: #718096;
            font-style: italic;
        }
        
        strong {
            color: #2d3748;
            font-weight: 600;
        }
        
        /* Grid layout for projects */
        .project-grid {
            display: grid;
            gap: 1.25rem;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        }
        
        .project-item {
            padding: 1rem;
            border-radius: 4px;
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
        }

        img {
            border-radius: 80% !important;  /* Makes image circular */
            border: 3px solid #3182ce !important;  /* Adds blue border */
            padding: 3px !important;
            background: white !important;
        }
        
        /* This ensures the styling applies specifically to the profile image */
        .element-container:has(img) {
            display: flex;
            justify-content: center;
        }

    </style>
    """,
    unsafe_allow_html=True
)

# Main Content
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Profile Picture
    image = Image.open("images/kushank.jpg")
    # st.markdown('<div class="centered"><img src="images/kushank.jpg" class="profile-img" alt="Kushank Maheshwari"></div>', unsafe_allow_html=True)
    
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image(image, width=250, use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Name and Contact Info
    st.markdown("<h1>Kushank Maheshwari</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div class="contact-info">
            <a href="mailto:mkushank2000@gmail.com">📧 Email</a>
            <a href="tel:+919214560741">📱 Phone</a>
            <a href="https://www.linkedin.com/in/kushank-maheshwari" target="_blank">💼 LinkedIn</a>
        </div>
        """,
        unsafe_allow_html=True
    )

def create_section(title, content):
    st.markdown(f"<h2>{title}</h2>", unsafe_allow_html=True)
    st.markdown('<div class="centered"><div class="content-wrapper">', unsafe_allow_html=True)
    st.markdown(content, unsafe_allow_html=True)
    st.markdown('</div></div>', unsafe_allow_html=True)

# Education Section
create_section(
    "Education",
    """
    <div class="project-item">
        <h3>Birla Institute of Technology and Science, Pilani</h3>
        <p>Master of Science in Mathematics + Bachelor of Engineering in Computer Science Engineering</p>
        <p><strong>GPA:</strong> 8.73/10.00 | <strong>Graduation:</strong> June 2023</p>
        <br>
        <h3>Delhi Public School, Jodhpur</h3>
        <p><strong>Class XII:</strong> 95.4% | May 2018</p>
    </div>
    """
)

# Skills Section
create_section(
    "Skills",
    """
    <div class="project-item">
        <h3>Programming</h3>
        <p>C++, Python (NumPy, Pandas, Matplotlib, Scrapy, scikit-learn, Django), JavaScript, SQL, Slang</p>      
        <h3>Tools & Technologies</h3>
        <p>Airflow, Cylc, StackStorm, GIT, MS Excel, IBM-SPSS, MySQL</p>
        <h3>Relevant Coursework</h3>
        <p>Data Structures and Algorithms, Database Systems, Artificial Intelligence, Data Mining</p>
    </div>
    """
)

# Experience Section
create_section(
    "Experience",
    """
    <div class="project-item">
        <h3>Software Development Engineer (SDE) | Flipkart</h3>
        <p><em>Bangalore, India</em></p>
        <ul>
            <li>Automated OS and Runtime Upgrades by integrating with CICD, improving developer productivity by 30%</li>
            <li>Automated RCA Quality and Standardisation, reducing toil by 5%-15%</li>
        </ul>
        <br>
        <h3>Summer Analyst, Corporate Treasury | Goldman Sachs</h3>
        <p><em>Bangalore, India</em></p>
        <ul>
            <li>Modelled and simulated impact of hedging on Weighted Average Cost of Debt (WACD)</li>
            <li>Analyzed WACD changes using a bond table with over 40,000 entries</li>
        </ul>
    </div>
    """
)

# Projects Section
create_section(
    "Projects",
    """
    <div class="project-grid">
        <ul class="project-item">
            <h3>Solar Energy Forecasting</h3>
            <p>Conducted pre-processing on GHI dataset and utilized ARIMA models for forecasting</p>
            <h3>Web Scraping ML Model</h3>
            <p>Scraped 10,000 data points for ML matchmaking model using Scrapy</p>
            <h3>Stock Price Forecasting</h3>
            <p>Forecasted stock prices for Tesla, Amazon, and Netflix with 91.4% accuracy</p>
        </ul>
    </div>
    """
)

# Awards Section
create_section(
    "Competitions and Awards",
    """
    <div class="project-item">
        <ul>
            <li>Tata Crucible Hackathon: Developed simulations for airport queue management</li>
            <li>Western Digital Scholarship for STEM</li>
            <li>3-star coder at Codechef</li>
            <li>U-13 Chess Nationals: Runner-up in State Championship and All India Rank 100</li>
        </ul>
    </div>
    """
)