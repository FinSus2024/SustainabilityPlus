import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import yfinance as yf
from supabase import create_client
from datetime import datetime, timedelta
import time
from concurrent.futures import ThreadPoolExecutor
import base64
import math
import traceback
#import mysql.connector

st.set_page_config(
    page_title="FiNTEL Sustain",
    layout="wide"  # Set the layout to wide
)


query_params = st.query_params

token = query_params.get("token")


supabase_key= st.secrets['supabase_key']
supabase_url= st.secrets['supabase_url']



supabase = create_client(supabase_url, supabase_key)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;700&display=swap');
    html, body, [class*="css"]  {
        font-family: 'Outfit', sans-serif !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

hide_style= """
            <style>
            #MainMenu {visibility: hidden;}
            header {visibility: hidden;}
            footer {visibility: hidden;}
            div._terminalButton_rix23_138 {display: none !important;}
            </style>
            """

st.markdown(hide_style, unsafe_allow_html=True)


with open("SustainabilityPlus_Logo.png", "rb") as img_file:
    sustainability_logo = base64.b64encode(img_file.read()).decode()









st.markdown("""
                <html>
                    <head>
                    <style>
                        .stApp {
                            overflow-y: auto !important; /* Force vertical scrollbar */
                        }
                        ::-webkit-scrollbar {
                            width: 1rem;
                            background-color: #ffffff;
                            overflow-y: auto !important; /* Force vertical scrollbar */
                            }
                            /* Track */
                            ::-webkit-scrollbar-track {
                            background: #f1f1f1;
                            }
                            /* Handle */
                            ::-webkit-scrollbar-thumb {
                            background: #f1f1f1;
                            }
                            /* Handle on hover */
                            ::-webkit-scrollbar-thumb:hover {
                            background: #ffffff;
                            }
                    </style>
                    </head>
                    <body>
                    </body>
                </html>
            """, unsafe_allow_html=True)




st.markdown("""
    <style>
    .stRadio {
        position: fixed;
        top: 10%;
        z-index: 1000;
        border: 0px solid white;
        display: flex;
        flex-direction: column;
        border-radius: 0px;
        height: 30px;
        width: 100%;
    }
    .stRadio > div {
        gap: 0px;
    }
    .stRadio div label {
        display: flex;
        justify-content: center;
        align-items: center;
        z-index: 1000;
        cursor: pointer;
        width: 30%; 
        text-align: center;
        height: 100%;
        font-size: 18px !important; /* Set font size */
        font-weight: normal !important; /* Set font weight */
    }
    .stRadio div label:hover {
        background-color: grey;
        color: white;        
    }
    label:has(> input[type="radio"]:checked) { /* styles to apply to the li tag */
        background-color: white !important;
        color: white !important; 
        border: 2px solid #ccc;
        border-bottom: 0px;
        border-radius: 0 0 0px 0px;
    }
    label:has(> input[type="radio"]:checked) * {
        color: lightgreen !important;
        font-weight: bold !important; /* Bold for selected option */
        font-size: 20px !important; /* Slightly larger font for selected option */
        background-color: transparent ;
                   
    }
            

            
.st-emotion-cache-ocqkz7:first-child {
    flex-wrap: wrap;
    -webkit-box-flex: 1;
    flex-grow: 1;
    -webkit-box-align: baseline;
    align-items: baseline;
    width:100%;
    gap: 1rem;
}

    [data-testid="stBaseButton-primary"] {
                    background-color: transparent ;
                    height: auto;
                    margin: 16.5px;
                    width: 100%;
                    z-index: 1000 ! important;
                    border-radius: 27px;
                    color: #000;
                    padding:3px;margin-bottom: 15px;
                    align-items: center;
                    text-align: center; 
                    font-weight: bold;
                    font-size: 1.25rem;
                    border: 1px solid #ccc ;
                    font-family: 'Outfit', sans-serif;
        }    
    [data-testid="stBaseButton-primary"] > div {
            background-color: transparent ;
            color: #000; 
            font-size: 1.25rem; 
            z-index: 3;
            font-family: 'Outfit', sans-serif;
        }  
             
    [data-testid="stBaseButton-primary"]:hover {
            background-color: #4682B4  ;  
            z-index: 3;
            color: white ! important;  
            border-color: #4682B4;  
            font-weight: bold !important; 
        }
            
    [data-testid="stBaseButton-secondary"] {
            background-color: transparent ;
            width: 100%;
            color: #4682B4;
            text-align: left; 
            z-index: 3;
            border: 1px solid transparent ;
            font-family: 'Outfit', sans-serif;
        } 
            
    [data-testid="stBaseButton-secondary"] :hover {
            background-color: #4682B4  ;  
            color: white ! important;  
        } 
            
    [data-testid="stBaseButton-secondary"] > div{
            background-color: transparent ;
            border-radius: 15px;
            width: 100%;
            border: 1px solid #ccc ;
            color: #000;
            text-align: left; 
            padding: 8px;
            font-size: .5 rem;
            z-index: 3;
            font-family: 'Outfit', sans-serif;
        }  
            
    
    [data-testid="stBaseButton-tertiary"] {
            background-color: transparent ;
            margin-top: 10px;
            width: 100%;
            text-align: left; 
            z-index: 3;
            border: 1px solid transparent ;
            font-family: 'Outfit', sans-serif;
        } 
            
    [data-testid="stBaseButton-tertiary"] :hover {
            background-color: #4682B4  ;  
            color: white ! important;  
        } 
            
    [data-testid="stBaseButton-tertiary"] > div{
            background-color: transparent ;
            border-radius: 10px;
            width: 100%;
            border: 1px solid #ccc ;
            color: #000;
            text-align: left; 
            padding: 5px;
            font-size: 1.25rem;
            z-index: 3;
            font-family: 'Outfit', sans-serif;
        }  

       
    .js-plotly-plot .plotly, .js-plotly-plot .plotly  .st-emotion-cache-s1invk  {
            font-family: "Outfit", sans-serif;
            margin-top: 15px;
            box-sizing: border-box;   
            border-radius: 27px;
            background: transparent;
            }

        .main-svg {
            direction: ltr;
            font-family: "Outfit", sans-serif;
            background: transparent;
            box-shadow: 1px 1px 5px #0000002E; 
            border-radius: 27px;
            margin-right:1.5rem;
        }
            

    </style>
""", unsafe_allow_html=True)



st.markdown(
    """
    <style>
    div[data-testid="stExpander"] div > p {
        padding: 0px;
        font-size: 1.15rem;
    }


    .st-emotion-cache-s1invk {
            position: relative;
            display: flex;
            width: 100%;
            font-size: 14px;
            padding: 8px;
            padding-left: 15px;
            cursor: pointer;
            list-style-type: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)





# Custom CSS styling for the header
st.markdown(
    """
    <style>
    .custom-header {
            background-color: #FFFFFF ;
            color: #0D0D0D ;
            font-size: 28px;
            padding: 5px;
            width: 100%;
            text-align: left;
            border-radius: 0px;
            font-weight: 600;
            font-family: 'Outfit', sans-serif; 
        }

    .custom-header sustain {
            color: #000;
            font-weight: bold;
            margin-left:2.5%;
            left:0%;
        }

    .kpis {
            width: 100%;
            padding: 2px;
            padding-left: 10px;
            height:100%;
            background-color: white;
            border-radius: 0px;
            text-align: justified;
            font-family: "Outfit", sans-serif;
                            }
    .kpis green {
            color: #3A3A3A;
            justify-content: flex-end; 
            display: flex;
            text-align: right;  
            position: relative;
            font-weight: bold;
        }
    
    .custom-headerbottom  {
            color: #000000;
            text-align: center;
            font-weight: 500;
            font-size: 1.25rem;
            width: 100%;
            margin-top: 1rem;
            background-color: #FFFFFF;
            font-family: 'Outfit', sans-serif;
        }

  

    .st-emotion-cache-1ibsh2c {
        padding-left: 1rem;
        padding-right: 1rem;
    }

    .stMainBlockContainer 
                {
                    width: 100%;
                    padding: 1rem 1.5rem 1rem 1.5rem;
                    max-width: initial;
                    min-width: auto;
                    height:100%;
                    overflow-y:auto;
                    z-index:0;
                }

    .st-emotion-cache-12fmjuu {
                    z-index:1;
	}

    footer {
	
	visibility: hidden;
	
	}
footer:after {
	content:'goodbye'; 
	visibility: visible;
	display: block;
	position: relative;
	background-color: red;
	padding: 5px;
	top: 2px;
}
       </style>
    """, 
    unsafe_allow_html=True
)




footer= """
        <style>
            .footer {
                position: relative;
                background-color:white;
                color: #000 ;
                margin-top: 45px;
                font-size: 15px;
                padding: 8px;
                width: 100%;
                text-align: left;
                font-family: 'Outfit', sans-serif;
                border-radius: 8px;
                font-weight: bold;

            }
            .left-top {
                position: absolute;
                top: 5px;
                left: 10px;
                font-size: 10px;
            }
            .right-bottom {
                position: absolute;
                bottom: 5px;
                right: 10px;
            }
              .footer a {
                color: blue; 
                font-size: 20px;
                text-decoration: none; 
                }

        </style>
        <div class="footer">
            <div class="right-bottom"><a href="https://www.sustainabilityplus.ai " target="_blank">www.sustainabilityplus.ai </a></div>
        </div>
    """

# Display the header with custom styling








def top20companies3(ranked_table, total_entries, pesgo_ranking):
    ranked_table = ranked_table[ranked_table['RANK']<=total_entries]

    
    st.markdown(
    '''
    <div class="custom-header">
            Top 20 Performance Ranking & Scores - Gaming Sector 
            <div style="
                            background-color: #FFFFFF; 
                            padding:0px;
                            border-radius: 5px; 
                            font-family: 'Outfit', sans-serif; 
                            font-size: 1.25rem; 
                            text-align: justify;
                            color: #000; 
                            font-weight:normal;
                            line-height:1.25;
                                ">  Analyzing key measurements against United Nations Sustainable Development Goals, 
                                    Earth, Society and Governance factors, Operational and Financial Performance criteria through FiNTEL 
                                    Sustain’s SustainabilityPlus platform. 
                                    Utilizing 25 discrete datasets with over 170 data inputs per company. The scores are based across a 3 year performance window.
                        </div>
    </div>
    ''',    unsafe_allow_html=True )
    st.markdown(
    '''-------''',    unsafe_allow_html=True )


    

    #top_20= st.columns([.6,1])



                # Render the complete table in Streamlit
    table_html = """
                <div style="
                    background-color: #ffffff;
                    text-align: left;
                    overflow-y: auto;
                    height: 45rem;
                    width:100%;
                    color: #0b0b0b;
                    font-family: 'Outfit', sans-serif;
                    font-size: 1rem;
                    z-index: 1;
                    position: relative;
                ">                    <table style="width: 100%; border-collapse: collapse;  ">
                        <thead style="
                            background: #C8C8C8;
                            color: #0b0b0b;
                            position: sticky;
                            width:100%;
                            top: 0;
                            z-index: 2;
                        ">                            <tr>
                                <th style="padding: 10px; font-weight: bold; text-align: center;">Rank</th>
                                <th style="padding: 10px; font-weight: bold; text-align: left;">Company</th>
                                <th style="padding: 10px; font-weight: bold; text-align: left;">Market</th>
                                <th style="padding: 10px; font-weight: bold; text-align: center;">Score</th>
                            </tr>
                        </thead>
                        <tbody>            """

                # Dynamically generate rows based on `ranked_table`
    for index, row in ranked_table.iterrows():
                    bg = "#FFFFFF" 
                    table_html += f"""                    <tr style="background: {bg};">
                            <td style="padding: 10px; text-align: center;">{row['RANK']}</td>
                            <td style="padding: 10px; text-align: left;">{row['COMPANY']}</td>
                            <td style="padding: 10px; text-align: left;">{row['MARKET']}</td>
                            <td style="padding: 10px; text-align: center;">{row['SCORE']}</td>
                        </tr>                """

                # Close table and div tags
    table_html += """
                            </tbody>
                        </table>
                    </div>
                """

    
        

        # Base HTML container
    flex_container =  f"""
            <div style="
                display: flex;
                flex-direction: column;
                flex-wrap: wrap;
                padding: 1rem;
                border-radius: 8px;
                position: relative;
            ">        <!-- Background Image with Opacity -->
            <div style="
                                background-color: transparent; 
                                z-index: 1;
                                font-family: 'Outfit', sans-serif; 
                                font-size: 1.5rem; 
                                margin-bottom: 1.5rem;
                                text-align: left;
                                color: #000000; font-weight:600;
                                    ">  Highest <span style="color: #0059FF;" > PESGO  </span>Scores</div> """

        # Add categories dynamically into rows
    categories = [
            "Performance", "Earth", "Society", "Governance", "Operational", "Compliance and Financial",  
            "Assets and Risk", "Market Exposure",  "Responsible Gambling",
            "Executive Board",  "Regulatory performance"
        ]

        # Group categories into rows: First two rows with 4 cards each, and the last row with 3 cards
    rows = [categories[:5]]
    rows2 = [ categories[5:8]]
    rows3 = [ categories[8:]]
        


    flex_container += """<div style="
            display: flex;
            flex-wrap: wrap;
            gap: 1.5%;
            padding: 
            background-color: transparent;
            box-sizing: border-box;
        ">"""

    for row in rows:
            for category in row:
                flex_container += f""" 
                <div style="
                    border: 1px solid #ddd;
                    padding: 1rem;
                    flex: 1 1 calc(20% - 1.5%); 
                    box-sizing: border-box;
                    flex-direction: column;
                    flex-wrap: wrap;
                    justify-content: left;
                    align-items: flex-start;;
                    margin-bottom: 1rem;
                    background-color: #FFFFFF;
                    box-shadow: 6px 12px 20px #0000002E;
                    border-radius: 27px;
                ">
                    <div style=" 
                        font-size: 1.2rem;
                        font-weight: bold;
                        color: #0059FF; 
                        font-family: 'Outfit', sans-serif;
                        text-align: left;
                        align-items: flex-start;; 
                    "> 
                    <span>  {category} </span>
                    </div>
                    <!-- Top Score -->
                    <div style="
                                font-size: .9rem;
                                color: #000000;
                                font-family: 'Outfit', sans-serif;
                                text-align: left;
                                display: flex;
                                gap: .25rem;
                                display:flex;
                                flex-direction: row;
                                justify-content: left;
                                align-items: flex-start;
                                padding: 10px;
                                padding-left: 0px;
                            "> 
                                <!-- Left Div (30%) -->
                                <div style="
                                    display: flex;
                                    flex-direction: column;
                                    align-items: flex-start;
                                    flex-wrap: nowrap;
                                    box-sizing: border-box; /* Prevents overflow */
                                ">
                                    <div>  <b style="font-size: 0.75rem;white-space: nowrap;">Top Score</b></div>
                                    <div>
                                        <span style="font-size: 1.25rem; font-weight: 750;">
                                            {pesgo_ranking[pesgo_ranking['Ratings_bucket'] == category]['SCORE'].iloc[0]}
                                        </span>
                                    </div>
                                </div>
                                <!-- Divider -->
                                <div style="border-right: 1px solid #000;  align-self: stretch;  margin-right: 5px;  margin-left: 5px; "></div>
                                <!-- Right Div (70%) -->
                                <div style="
                                    font-size: .9rem;
                                    color: black;
                                    text-align: left;
                                    display: flex;
                                    gap:2%;
                                    align-items: flex-start;
                                    box-sizing: border-box; /* Prevents overflow */
                                "> 
                                    {pesgo_ranking[pesgo_ranking['Ratings_bucket'] == category]['COMPANY'].iloc[0].strip()}
                                </div>
                            </div>
                </div>"""  # Close the category div

    flex_container += "</div>"  # Close the main container div


        
    flex_container2 = """
    <div style="
            background-color: transparent; 
            z-index: 1;
            font-family: 'Outfit', sans-serif; 
            font-size: 1.5rem; 
            text-align: left;
            opacity:1;
            color: #000000; 
            font-weight:600;
                flex-direction: column;
                flex-wrap: wrap;
                padding: 1rem;
                border-radius: 8px;
                position: relative;
            ">Highest Scores-Data and Key Indicators</div>        <div style="
                                        display: flex;
                                        flex-wrap: wrap;
                                        gap: 1.5rem;
                                        justify-content: space-around;
                                        background-color: transparent; 
                                        padding: 1%; 
                                        z-index: 1;
                                        font-family: 'Outfit', sans-serif; 
                                        font-size: 1.5rem; 
                                        text-align: left;
                                        color: #000000; font-weight:600;
                                    ">        """

        # Combine rows2 and rows3 for consistent layout
    combined_rows = rows2 + rows3

    for row in combined_rows:
            for category in row:
                flex_container2 += f""" 
                <div style="
                    border: 1px solid #ddd;
                    padding: 1.25%;
                    flex: 1 1 calc(33% - 1.5rem); 
                    box-sizing: border-box;
                    display: flex;
                    flex-direction: column;
                    flex-wrap: wrap;
                    justify-content: left;
                    align-items: left;
                    background-color: #FFFFFF;
                    box-shadow: 6px 12px 20px #0000002E;
                    border-radius: 27px;
                    font-weight:normal;
                ">
                    <div style=" 
                        font-size: 1.2rem;
                        font-weight: bold;
                        color: #0059FF; 
                        font-family: 'Outfit', sans-serif;
                        text-align: left;
                        align-items: flex-start; 
                    "> 
                    <span>  {category} </span>
                    </div>
                    <!-- Top Score -->
                    <div style="
                                font-size: .9rem;
                                color: #000000;
                                font-family: 'Outfit', sans-serif;
                                text-align: left;
                                display: flex;
                                gap: .25rem;
                                flex-direction: row;
                                justify-content: left;
                                align-items: flex-start;
                                padding: 10px;
                                padding-left: 0px;
                            "> 
                                <!-- Left Div (30%) -->
                                <div style="
                                    display: flex;
                                    flex-direction: column;
                                    align-items: center;
                                    box-sizing: border-box; /* Prevents overflow */
                                ">
                                    <div><b style="font-size: 0.75rem; white-space: nowrap; ">Top Score</b></div>
                                    <div>
                                        <span style="font-size: 1.25rem; font-weight: 750;">
                                            {pesgo_ranking[pesgo_ranking['Ratings_bucket'] == category]['SCORE'].iloc[0]}
                                        </span>
                                    </div>
                                </div>
                                <!-- Divider -->
                                <div style="border-right: 1px solid #000; height: 90%;   margin-right: 5px;  margin-left: 5px; "></div>
                                <!-- Right Div (70%) -->
                                <div style="
                                    font-size: .9rem;
                                    color: black;
                                    text-align: left;
                                    display: flex;
                                    align-items: flex-start;                                    
                                    box-sizing: border-box; /* Prevents overflow */
                                "> 
                                    {pesgo_ranking[pesgo_ranking['Ratings_bucket'] == category]['COMPANY'].iloc[0]}
                                </div>
                            </div>
                </div>"""  # Close the category div

    flex_container2 += "</div>"  # Close the main flex container

        
        
        # Add footer information
 

        # Render the flex container in Streamlit
        #st.markdown(flex_container, unsafe_allow_html=True)
        #st.markdown(flex_container2, unsafe_allow_html=True)
        #st.markdown(flex_container3, unsafe_allow_html=True)

    flex_container_end= """
        <div style='
            color: #000000;
            text-align: left;
            font-weight: 600;
            font-size: 20px;
            width: 100%;
            z-index:1;
            padding: 15px;
            background-color: transparent;
            font-family: 'Outfit', sans-serif;
        '>
            Company performance is measured against a detailed AI-enabled scoring 
            methodology based on open-source data. Our terms and conditions are covered in 
            detail on our website: <a href="https://www.sustainabilityplus.ai" target="_blank">www.sustainabilityplus.ai</a> </div>        """


        # Close the main container
        #st.markdown(flex_container_end, unsafe_allow_html=True)

    
    

    
    
    






    st.markdown(f"""
    <style>
        .top20container {{
            display: flex;
            flex-wrap: wrap;
            width: 100%;
            flex-direction: row;
        }}
        .item {{
            flex: 1 1 100%;  /* Full width on small screens */
            box-sizing: border-box;
        }}
        @media (min-width: 1600px) {{
            .table {{
                flex: 0 0 35%;
            }}
            .flex1 {{
                flex: 0 0 65%;
            }}
            .flex2 {{
                flex: 0 0 65%;
            }}
        }}
    </style>
    <div class="top20container">
        <div class="item table">            {table_html}        </div>
        <div class="item flex1">            {flex_container}        </div>
        <div class="item flex2">            {flex_container2}        </div> 
        <div class="item flex2">            {flex_container_end}        </div> 
    </div>
""", unsafe_allow_html=True)
    st.markdown("--------", unsafe_allow_html=True)
    st.markdown(
            '''<div class="custom-headerbottom">The open-source data represents the Top 20 of some of the Largest Companies in the iGaming, 
            Sports Betting and Land based casino sector by market capitalization. The maximum score is 5.0
                </div>''',
                    unsafe_allow_html=True
                )
    

    st.markdown(footer, unsafe_allow_html=True)



st.markdown("""
    <style>
    /* Style for the dropdown container */
    div[data-baseweb="select"] > div {
        color: #000000; 
        height: auto; 
        background-color: white; 
        border: 1px solid rgb(0, 32, 104); 
        border-radius: 15px; 
        font-size: 20px; /* Set desired font size */
        display: flex;
        align-items: center;  /* Center text vertically */
        padding: 0 10px;      /* Horizontal padding for better spacing */
    }
    
    /* Hover effect for dropdown */
    div[data-baseweb="select"] > div:hover {
        background-color: #FAFAFA; 
        color: #000000;
    }

    /* Container for the select box and label */
    .stSelectbox {
        display: flex;
        align-items: center;
        margin-top: 2.5%;
        font-weight: bold;
        color: #006400;  /* Use a dark green for contrast */
    }
    
    /* Label styling 
    .stSelectbox label {
        display: inline-block;
        text-align: left;
        margin-right: 10px;
        padding: 8px 0;
        white-space: nowrap;
        color: #006400;
    }
            */

    /* Select box width and alignment */
    .stSelectbox div[data-baseweb="select"] {
        display: inline-block;
        font-weight: bold;
            
    }
    
    /* Markdown container styling */
    .stSelectbox [data-testid='stMarkdownContainer'] {
        color: #000000;
        font-size: 30px;
        padding: 10px;
    }

    ._terminalButton_rix23_138 {
        visibility: hidden;
    }
    ._link_gzau3_10 {
        --tw-bg-opacity: 1;
        visibility: hidden ! important;
    }
            
    </style>
""", unsafe_allow_html=True)







def get_percentage_change(ticker_symbol):
    end_date = datetime.today().strftime('%Y-%m-%d')
    start_date = (datetime.today() - timedelta(days=90)).strftime('%Y-%m-%d')
    
    try:
        # Fetch data
        df = yf.download(ticker_symbol, start=start_date, end=end_date)
        if df.empty:
            return 0
        
        # Calculate percentage change from start to end
        total_change = ((df['Close'].iloc[-1] - df['Close'].iloc[0]) / df['Close'].iloc[0]) * 100
        return round(total_change.iloc[0],2) #f"{total_change:.2f}%"
    except Exception as e:
        return 0

    
def safe_get_value(df, company, column, default=0):
    try:
        value = df.loc[df['COMPANY'] == company, column].values
        return value[0] if pd.notnull(value[0]) else default
    except (IndexError, KeyError):
        return default

def CompanyDashboard(ranked_table_base, summary,  pesgo_list, Pesgo_Risks, revenue_excel, Financial_Data):

    companies = sorted(ranked_table['COMPANY'].unique())

    select_company= st.columns([5,2])

    summary_col, ratings_col= st.columns([5,2])
    with select_company[1]:
        st.session_state.selected_company= st.selectbox('**Select Company**', options=companies, label_visibility= 'collapsed')
    selected_company =st.session_state.selected_company
    selected_ticker= st.session_state.selected_ticker = summary.loc[summary['CompanyFullName'] == selected_company, 'TickerSymbol'].values[0].strip()


    with select_company[0]:
        st.markdown(f'''
            <div class="kpis" style="display: flex;  justify-content: space-between; border: none; font-size: 38px; background-color: transparent;   align-items: center; padding: 5px;">
                <span style="color: #0059FF; font-weight: 600;">{selected_company} - 3 year performance </span>
                <span  style=" font-size: 30px; ">Select Company</span>
            </div>
            ''', unsafe_allow_html=True)     

     
    
    selected_pesgo_risks=  Pesgo_Risks[Pesgo_Risks['COMPANY']== selected_company ]


    st.markdown("----", unsafe_allow_html=True)

    company_level = summary[summary['COMPANY']== selected_company ]
    pesgo_ranking_company = ranked_table_base[ranked_table_base['COMPANY']== selected_company ] 
    pesgo_scores = pesgo_ranking_company.groupby(['COMPANY', 'Ratings_bucket'])['SCORE'].mean().reset_index()
    pesgo_scores['SCORE'] = pesgo_scores['SCORE'].apply(lambda x: float(f"{x:.2f}") if pd.notnull(x) else x)

    #selected_ticker= summary[summary['COMPANY']== selected_company ]['TickerSymbol']
    #balance_sheet = get_balance_sheet(selected_ticker)
    #market_cap_data= get_market_cap(selected_ticker)

    #market_cap_data= get_market_cap(selected_ticker)
    #fin_data= get_financial_data(selected_ticker)

    #Financial_Data
    
    
    
    comp_revenue= Financial_Data[Financial_Data['COMPANY'] == selected_company]
    



    selected_Summary = company_level.loc[company_level['COMPANY'] == selected_company, 'Summary'].values[0]

    selected_Business = company_level.loc[company_level['COMPANY'] == selected_company, 'Business'].values[0]

    selected_Listing = company_level.loc[company_level['COMPANY'] == selected_company, 'Exchange'].values[0]

    selected_currency = company_level.loc[company_level['COMPANY'] == selected_company, 'Symbol'].values[0]


    
    rank= ranked_table[ranked_table['COMPANY']==selected_company]['RANK'].iloc[0]
    average_score= ranked_table[ranked_table['COMPANY']==selected_company]['SCORE'].iloc[0]

    if selected_company=='Kindred Group (acquired by FDJ in October 2024)':
        note= "Note:  Only the latest figures for FDJ are included in the company overview and financial performance graph."

    else:
        note= ''



    #comp_revenue= revenue[revenue['Company']== selected_company]

    max_year = comp_revenue["Year"].max() if "Year" in comp_revenue.columns and comp_revenue["Year"].notnull().any() else np.nan

    formatted_year = str(int(max_year)) if pd.notnull(max_year) else ""

    # Filter the DataFrame for the max year
    latest_year_revenue = comp_revenue[comp_revenue["Year"] == max_year]



    selected_MarketCap = safe_get_value(latest_year_revenue, selected_company, 'MarketCap')
    selected_EnterpriseValue = safe_get_value(latest_year_revenue, selected_company, 'EnterpriseValue')
    selected_Revenue = safe_get_value(latest_year_revenue, selected_company, 'TotalRevenue')

    # If you want to return string for listing/exchange instead of 0:


    


    for i in pesgo_list:
                trimmed_pesgo_v = i.replace(" ", "")

                if not pesgo_scores.empty:
                    st.session_state[trimmed_pesgo_v] = f"{round(pesgo_scores.loc[pesgo_scores['Ratings_bucket'] == i, 'SCORE'].iloc[0], 2):.2f}"
                else:
                    st.session_state[trimmed_pesgo_v]= 'N/A'

    
    pesgo_combined = f"""
            <div style="width: 100%; padding: 15px; padding-top: 0px; height: auto; background-color: transparent; border: 0px solid #ddd; border-radius: 0px;  font-family: 'Outfit', sans-serif; display: flex ;flex-direction: column;">
                <!-- PESGO Key Risks -->
                <div style="font-size: 37px; font-weight: 600; background-color: #FFFFFF; color: #0059FF; margin-bottom: 10px;">
                     <span style="color: #000000" " > PESGO Scores  </span>
                </div>
                <div style="width: 100%; display: flex; text-align: center; margin-bottom: 4px; border: 1px solid #1969FF30; flex: 1:1; align-items: center; justify-content: space-between; flex-direction: row;">
                <div  style=" border: 1px solid #1969FF30;  width: 20%; ">
                        <div style="flex: 1; background-color: #1969FF30; color: #000000; padding: 10px; font-size: 20px;  border: 1px solid white;">
                            Performance (Financial)
                        </div>
                        <div style="flex: 1; background-color: #FFFFFF; color: #0059FF  ; padding: 10px; font-size: 20px; font-weight: bold; border: 1px solid white;">
                            {st.session_state['PerformanceOutlook']}
                        </div>
                </div>
                <div style=" border: 1px solid #1969FF30;  width: 20%; ">
                    <div style="flex: 1; background-color: #1969FF30; color: #000000; padding: 10px; font-size: 20px;  border: 1px solid white;">
                        Earth
                    </div>
                    <div style="flex: 1; background-color: #FFFFFF; color: #0059FF  ; padding: 10px; font-size: 20px; font-weight: bold; border: 1px solid white;">
                        {st.session_state['Earth']}
                    </div>
                </div>
                <div style=" border: 1px solid #1969FF30;  width: 20%; ">
                    <div style="flex: 1; background-color: #1969FF30; color: #000000; padding: 10px; font-size: 20px;  border: 1px solid white;">
                        Society
                    </div>
                    <div style="flex: 1; background-color: #FFFFFF; color: #0059FF  ; padding: 10px; font-size: 20px; font-weight: bold; border: 1px solid white;">
                        {st.session_state['Society']}
                    </div>
                </div>
                <div style=" border: 1px solid #1969FF30;  width: 20%; ">
                    <div style="flex: 1; background-color: #1969FF30; color: #000000; padding: 10px; font-size: 20px;  border: 1px solid white;">
                        Governance
                    </div>
                    <div style="flex: 1; background-color: #FFFFFF; color: #0059FF  ; padding: 10px; font-size: 20px; font-weight: bold; border: 1px solid white;">
                        {st.session_state['Governance']}
                    </div>
                </div>
                <div style=" border: 1px solid #1969FF30;  width: 20%; ">
                    <div style="flex: 1; background-color: #1969FF30; color: #000000; padding: 10px; font-size: 20px;  border: 1px solid white;">
                        Operational
                    </div>
                    <div style="flex: 1; background-color: #FFFFFF; color: #0059FF  ; padding: 10px; font-size: 20px; font-weight: bold; border: 1px solid white;">
                        {st.session_state['Operational']}
                    </div>
                </div>
            </div>
            """
    
   

    comp = f"""
                <div style="width: 100%; padding: 15px; background-color: #FFFFFF; font-family: 'Outfit', sans-serif; display: flex; flex-direction: column; ">
                    <div style="font-size: 37px; font-weight: 600; color: #000000; margin-bottom: 10px;">
                        Data and Key Indicator Rating
                    </div>
                    <div style="width: 100%; display: flex; flex-direction: row; align-items: flex-start; justify-content: space-between; border: 1px solid #E8E6E6;">
                        <!-- Box 1 -->
                        <div style="border: 1px solid #E8E6E6; width: 17%; min-height: 120px; display: flex; flex-direction: column;">
                            <div class="label-container">
                                <div>Compliance and Financial</div>
                            </div>
                            <div class="value-container">
                                {st.session_state['ComplianceandFinancial']}
                            </div>
                        </div>
                        <!-- Box 2 -->
                        <div style="border: 1px solid #E8E6E6; width: 17%; min-height: 120px; display: flex; flex-direction: column;">
                            <div class="label-container">
                                <div>Market Exposure</div>
                            </div>
                            <div class="value-container">
                                {st.session_state['MarketExposure']}
                            </div>
                        </div>
                        <!-- Box 3 -->
                        <div style="border: 1px solid #E8E6E6; width: 17%; min-height: 120px; display: flex; flex-direction: column;">
                            <div class="label-container">
                                <div>Responsible Gambling</div>
                            </div>
                            <div class="value-container">
                                {st.session_state['ResponsibleGambling']}
                            </div>
                        </div>
                        <!-- Box 4 -->
                        <div style="border: 1px solid #E8E6E6; width: 17%; min-height: 120px; display: flex; flex-direction: column;">
                            <div class="label-container">
                                <div>Executive and non-Executive Board</div>
                            </div>
                            <div class="value-container">
                                {st.session_state['Executiveandnon-ExecutiveBoard']}
                            </div>
                        </div>
                        <!-- Box 5 -->
                        <div style="border: 1px solid #E8E6E6; width: 17%; min-height: 120px; display: flex; flex-direction: column;">
                            <div class="label-container">
                                <div>Regulatory performance across markets</div>
                            </div>
                            <div class="value-container">
                                {st.session_state['Regulatoryperformanceacrossmarkets']}
                            </div>
                        </div>
                        <!-- Box 6 -->
                        <div style="border: 1px solid #E8E6E6; width: 17%; min-height: 120px; display: flex; flex-direction: column;">
                            <div class="label-container">
                                <div>Asset performance and shareholder risk</div>
                            </div>
                            <div class="value-container">
                                {st.session_state['Assetperformanceandshareholderrisk']}
                            </div>
                        </div>
                    </div>
                </div>
                <style>
                .label-container {{
                    background-color: #E8E6E6;
                    color: #000000;
                    padding: 10px;
                    font-size: 20px;
                    text-align: center;
                    border: 1px solid white !important;
                    height: 4.5rem;  /* Ensures uniform height for all labels */
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border: 1px solid #ccc;
                }}

                .value-container {{
                    background-color: #FFFFFF;
                    color: #0059FF;
                    padding: 10px;
                    border: 1px solid white;
                    font-size: 20px;
                    font-weight: bold;
                    text-align: center;
                    height: 60px;  /* Ensures all values align */
                    display: flex;
                    align-items: center;
                    justify-content: center;
                }}
                </style>
            """
    
    fig = go.Figure() 

    fig.add_trace(
                        go.Scatter(
                            x=comp_revenue["Year"],
                            y=comp_revenue["MarketCap"]/1000000000,
                            mode="lines+markers",
                            name="Market Cap  ",  # Legend name
                            line=dict(width=3, color="#90e3c7"),  # Line color
                                            )            )
    fig.add_trace(
                        go.Scatter(
                            x=comp_revenue["Year"],
                            y=comp_revenue["EBITDA"]/1000000000,
                            mode="lines+markers",
                            name="EBITDA",  
                            line=dict(width=3, color="#fbc150" ),
                        )           )
    fig.add_trace(
                        go.Scatter(
                            x=comp_revenue["Year"],
                            y=comp_revenue["TotalRevenue"]/1000000000,
                            mode="lines+markers",
                            name="Revenue", 
                            line=dict(width=3,  color="#fd98a8"),
                        )
                    )

    fig.add_trace(
                        go.Scatter(
                            x=comp_revenue["Year"],
                            y=comp_revenue["EnterpriseValue"]/1000000000  ,
                            mode="lines+markers",
                            name="Enterprise Value  ", 
                            line=dict(width=3,  color="#66b9ff"),
                        )
                    )
            
         
    fig.update_layout(
                       
                        
                        xaxis=dict(
                            title="",
                            range=[comp_revenue['Year'].min(), comp_revenue['Year'].max()],  # Set the range of the x-axis
                            type="linear" , # 'linear', 'log', 'date', or 'category'
                            tickfont=dict(
                                family="Outfit, sans-serif",  # Font family
                                size=12,  # Font size
                                color="#000",  # Font color
                            ),
                            linecolor="#000",
                            linewidth=2,
                            position=0
                        ),
                        # y axis lables
                        yaxis=dict(
                            title="", 
                            type="linear" , 
                            tickformat=",.2f",
                            tickprefix= f"{selected_currency} ",
                            ticksuffix=" BN",
                            showgrid=True,  # Show the grid lines
                            gridcolor="#000",  # Light white grid color (adjust opacity as needed)
                            gridwidth=0.5,
                            tickfont=dict(
                                family="Outfit, sans-serif",  # Font family
                                size=15,  # Font size
                                color="#000",  # Font color
                            ),
                        )
                    )   
                    
            
    fig.update_layout(
                
                    title=dict(
                        text="Financial Performance",
                        font=dict(size=25, color="#000000", family="Outfit, sans-serif"),  
                        x=0.05,  
                        xanchor="left",  
                    ),
                    
                    legend=dict(
                    x=0.45,  
                    y=-0.15,  
                    xanchor="center", 
                    yanchor="top",  
                    orientation="h",  
                    font=dict(size=15, color="#000"),
                ),
                height=375,
                plot_bgcolor="#FFFFFF",  
                paper_bgcolor="#FFFFFF", 
                
                )
          
    
    
    

    with summary_col:
         #summmary
        
        st.markdown(f"""
                <div style='
                    width: 100%;
                    height: auto;
                    background-color: #FFFFFF;;
                    border:0px solid #f1f1f1;
                    font-family: "Outfit", sans-serif;
                    color: #000000;
                    font-size: 1.25rem; 
                    padding: 0;
                    margin-top: 5px;
                '>
                    <div style='
                        text-align: justify; 
                        color: #000; 
                        padding: 10px; 
                        line-height: 1.25;
                    '>
                        {selected_Summary}     </div>        </div>                """,
                unsafe_allow_html=True
            )

       
    with ratings_col:


        st.markdown(
                    f'''
                    <div style="display: flex; flex-direction: row; border: none; background-color: #FFFFFF; font-weight: bold; margin-top: 0px; gap: 2.5%;  flex-wrap: wrap; 
                                    padding: 1rem; ">
                            <div class="kpis" style="flex: 1; display: flex; font-size: 1.1rem; justify-content: center; margin-bottom: 5%; 
                                        border-radius: 27px;
                                        box-shadow: 3px 6px 10px #0000002E;
                                        opacity: 1;
                                        padding: 10px 15px; border: 1px solid #ddd; background-color: #FFFFFF;">
                                <span style="font-size: 1.5rem; text-align: center; line-height: 1.4;">
                                    Peer Ranking <br>  by Sector  <br> 
                                    <span style="font-size: 50px; color: #0059FF;">{rank}</span>  <br> of 20
                                </span> 
                            </div>
                            <div class="kpis" style="flex: 1; display: flex; font-size: 1.1rem; justify-content: center; 
                                        border-radius: 27px;
                                        box-shadow: 3px 6px 10px #0000002E;
                                        opacity: 1;
                                        padding: 10px 15px; border: 1px solid #ddd; background-color: #FFFFFF;">
                                <span style="font-size: 1.5rem; text-align: center; line-height: 1.4;">
                                    Weighted <br>  Overall Score <br> 
                                    <span style="font-size: 50px; color: #0059FF;"> {average_score}</span> <br> of 5.0
                                </span>
                            </div> 
                    </div>
                    ''',
                    unsafe_allow_html=True
                )



    

    #with pesgo_cols:
    st.markdown(pesgo_combined, unsafe_allow_html=True)
    st.markdown(comp, unsafe_allow_html=True)

    st.markdown("----", unsafe_allow_html=True)
          
      

    
    
    company_profile_col, finance_chart_col , key_risks_cols= st.columns([2.5,2.5, 2])


    
    with st.container():

        with company_profile_col:
            performance_change= get_percentage_change(selected_ticker)

            if performance_change > 0:
                performance_text = f"Up by {performance_change}%"
                color = "#00C853"  # dark green
                arrow_svg = f''' <svg width="65%" viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg">
                <!-- Draw the filled triangle using a polygon -->
                <polygon points="100,350 250,50 400,350" fill="#00C853" stroke="black" stroke-width="4"/>
                </svg>
                '''
            elif performance_change < 0:
                performance_text = f"Down by {abs(performance_change)}%"

                arrow_svg = f'''
                    <svg width="65%" viewBox="0 0 500 400" xmlns="http://www.w3.org/2000/svg" >
                    <!-- Draw the filled triangle using a polygon -->
                        <polygon points="100,50 400,50 250,350" fill="red" stroke="black" stroke-width="4"/>
                    </svg>
                    '''

                color = "#D50000"  # dark red
            else:
                performance_text = "No Change"
                # Neutral icon: a circle with a horizontal line
                arrow_svg = f'''
                <svg width="100" viewBox="0 0 24 24">
                <circle cx="12" cy="12" r="10" fill="#E0E0E0" />
                <line x1="8" y1="12" x2="16" y2="12" stroke="#616161" stroke-width="2"/>
                </svg>
                '''
                color = "#616161"  # neutral gray


        
            

            st.markdown("""
                <style>
                    /* Sticky Company Overview */
                    .sticky-header {
                        width: 100%;
                        background: white;
                        z-index: 10;
                        font-size: 1.5rem;
                        font-weight: bold;
                        display: flex;  /* Ensures flexbox layout */
                        justify-content: space-between; /* Spaces out elements */
                        align-items: center; /* Aligns items vertically */
                                        }

                    /* Main Container */
                    .container {
                        width: 100%;
                        height: 23.5rem;
                        display: flex;
                        flex-wrap: wrap;
                        flex: 1;
                        overflow: hidden;
                        padding-left: 1rem;
                        padding-right: 1rem;
                        margin-top: 13px;
                        font-family: "Outfit", sans-serif;
                        background: #FFFFFF;
                        box-shadow: 1px 1px 10px #0000002E;
                        border-radius: 27px;
                    }

                    /* Two-column layout */
                    .content {
                        display: flex;
                        justify-content: space-between;
                        align-items: flex-start;
                        gap: 2%;
                        width: 100%;
                    }

                    .left-box { width: 70%;  overflow: hidden; }
                    .right-box { width: 30%; overflow: hidden; } 

                    /* KPI box styling */
                    .kpis {
                        flex: 1:.5;
                        display: flex;
                        justify-content: space-between;
                        font-family: "Outfit", sans-serif;overflow: hidden;
                        align-items: center;
                        padding: 1.5%;
                        border: 1px solid #ccc;
                        border-radius: 12px;
                        background-color: #ffffff;
                        margin-bottom: 8px;
                    }

                    /* Responsive Layout */
                    @media screen and (max-width: 768px) {
                        .content {
                            flex-direction: column; /* Stack elements vertically */
                            overflow: hidden;
                        }
                        .left-box, .right-box {
                            width: 100%; /* Full width on mobile */
                            overflow-y: hidden;
                        }
                    }
                </style>
            """, unsafe_allow_html=True)
            
            today = datetime.today()
            quarter = (today.month - 1) // 3 + 1  # Determine current quarter (1-4)
            first_month_of_quarter = 3 * (quarter - 1) + 1  # Get first month of the quarter
            quater_start= datetime(today.year, first_month_of_quarter, 1).date()




            # HTML Layout
            st.markdown(f"""
                <div class="container">
                    <!-- Sticky Header -->
                    <div class="sticky-header"> <span>Company Overview</span> <span style=" font-weight: bold; font-size:1rem; color: #ccc; "> As of 15 Jan 2025 </span>  </div>
                    <div class="content">
                        <!-- Left Column (KPIs) -->
                        <div class="left-box">
                            <div class="kpis"><span>Company Listing</span>  <span style="margin-right: 1rem; font-weight: bold;"> {selected_Listing} </span> </div>
                            <div class="kpis"><span>Company Business</span>  <span style="margin-right: 1rem; font-weight: bold;"> {selected_Business} </span></div>
                            <div class="kpis"><span>Market Cap</span>  <span style="margin-right: 1rem; font-weight: bold;">  {selected_currency}  {round(selected_MarketCap/1000000000, 2)} BN </span></div>
                            <div class="kpis"><span>Revenues FY {(formatted_year)}</span>  <span style="margin-right: 1rem; font-weight: bold;">  {selected_currency}   {round(selected_Revenue/1000000000, 2)} BN </span></div>
                            <div class="kpis"><span>Enterprise Value</span>  <span style="margin-right: 1rem; font-weight: bold;">  {selected_currency}  {round(selected_EnterpriseValue/1000000000, 2)}   BN </span></div>
                        </div>
                        <div class="right-box">
                            <div style="
                                        padding-top: 10px; 
                                        border: 1px solid #ddd; 
                                        border-radius: 15px; 
                                        height:100%;
                                        background-color: #fdfdfd;
                                        box-shadow: 1.5px 3px 5px #0000002E; 
                                        text-align: center;">
                                        <div style="font-size: 1.25rem; font-weight: bold; ">Last 3 Months Stock Performance</div>
                                        <div >{arrow_svg}</div>
                                        <div style="font-size: 1.25rem; font-weight: bold; padding:1.5%;" > {performance_text} </div> 
                                    </div>
                        </div>
                    </div>
                    <div >  {note}</div>
                </div>
            """, unsafe_allow_html=True)
        with finance_chart_col:
                
                
                st.markdown("<div class='chart-container'>", unsafe_allow_html=True)
                st.plotly_chart(fig, key= f"{selected_company}_1", use_container_width=True)
                st.markdown("</div>", unsafe_allow_html=True)


        with key_risks_cols:

            pesgo_risks = selected_pesgo_risks['PESGO_RISKS'].dropna().tolist()

            # Start building the HTML content
            html_content = """
            <div style='
                width: 100%;
                height: 23.5rem;
                display: flex;
                flex-wrap: wrap;
                flex: 1;
                overflow-y: hidden;
                padding:1rem;
                margin-top:13px; align-items: center;justify-content: center;
                font-family: "Outfit", sans-serif;
                position: relative;   
                background: #FFFFFF 0% 0% no-repeat padding-box;
                box-shadow: 1px 1px 10px #0000002E; 
                border-radius: 27px;
                gap:1%;
                opacity: 1;'>
                <div style='
                    text-align: left;
                    color: black;
                    font-size: 1.5rem; 
                    font-weight: bold;
                    font-family: "Outfit", sans-serif; align-items: center;justify-content: center;
                    width: 100%;
                    color: #000;
                    background: #FFFFFF;
                    z-index: 10; '>
                <span style="color: #0059FF;"> PESGO </span> Key Risks
                </div>        """

            # Loop through each PESGO risk and add it dynamically
            for risk in pesgo_risks:
                html_content += f"""            <div style='
                    width: 100%;
                    padding-left: 15px;
                    padding:10px;
                    background-color:  #FF196717;
                    text-align: left;
                    align-items: center;justify-content: center;
                    color: #000;
                    font-size: 1.2rem; 
                    border-radius: 12px;
                    opacity: 1;'>
                    {risk}
                </div>            """

            # Close the main div
            html_content += "</div>"

            # Render in Streamlit
            st.markdown(html_content, unsafe_allow_html=True)

    
        
    
    st.markdown(footer, unsafe_allow_html=True)

            









# Function to generate dynamic graphs for each category


def create_category_graph(unpivoted_df, Ratings_bucket, sector):
    with st.container():
        # Filter the DataFrame based on the category
        Sector_df = unpivoted_df[unpivoted_df['Category'] == sector]
        
        # Convert 'Score' to numeric, coerce errors to NaN
        Sector_df['SCORE'] = pd.to_numeric(Sector_df['SCORE'], errors='coerce')
        
        # Group by Category and Company, then calculate the mean of 'Score'
        Sector_df = Sector_df.groupby(['Category', 'COMPANY'])['SCORE'].mean().reset_index()

        # Find the indices of the top 1 and top 2 scores

        max_value = Sector_df["SCORE"].max()

        # Find indices where SCORE equals the max value
        max_indices = Sector_df.index[Sector_df["SCORE"] == max_value].tolist()


        max_value1_idx = Sector_df["SCORE"].nlargest(1).index.tolist()  # Index of the max value for Value1
        max_value2_idx = Sector_df["SCORE"].nlargest(2).index.tolist()  # Get indices of the top 2 largest values for Value2
        Sector_df['SCORE'] = pd.to_numeric(Sector_df['SCORE'], errors='coerce').fillna(0).round(2)


        # Combine the top 1 and top 2 indices from both Value1 and Value2 into a list
        highlighted_indices = max_indices #list(set(max_value1_idx + max_value2_idx))        
        # Create Bar Chart
        fig = go.Figure()
        # Add Trace for the bars

        config = { "modeBarButtonsToRemove": ["toImage"],  # Remove the snapshot button
                }
        fig.add_trace(
            go.Bar(
                x=Sector_df["COMPANY"],
                y=Sector_df["SCORE"],
                hovertemplate="%{x}: %{y}<extra></extra>" ,
                text=(Sector_df["SCORE"]),
                textposition='outside'  ,
                marker=dict(
                    color=[
                        "green" if i in highlighted_indices else  # Highlight the top 1st and 2nd max bars with green
                        "#0086b3"  # Default color for all other bars
                        for i in range(len(Sector_df))  # Iterate over the DataFrame length
                    ]),
                textfont=dict(
                    color="black" ,
                )
            )
        )

        # Update Layout for the graph
        fig.update_layout(
            title=dict(
                text=f"{sector}",  # Dynamic chart title based on category
                font=dict(size=20, color="rgb(0, 89, 255)", family="Outfit"),  # Title font settings
                x=0.5,  # Center the title
                xanchor="center",  
            ),
            hoverlabel=dict(
                font_size=20,  # Increase the font size
                font_family="Outfit",  # Set the font family
                font_color="black",  # Set the font color
                bgcolor="white",  # Set the background color
                bordercolor="black"  # Set the border color
            ),
            legend=dict(
                x=0.5,
                y=-0.2,
                xanchor="center",
                yanchor="top",
                orientation="h",  # Horizontal legend
                bgcolor="rgba(0, 51, 0, 0.8)",  # Background color
                font=dict(size=12, color="white"),  # Font settings
            ),
            height=325,
            width=1000,
            barmode="group",  # Group bars side by side
            bargap=.7,  # Space between bars (lower value = wider bars)
            bargroupgap=0.05,  # Space between bar groups
            plot_bgcolor= "white", # "#003300",  # Plot area background color
            paper_bgcolor="white", #"#003300",  # Overall chart background color
            yaxis=dict(
                title='',        # Label for the y-axis
                type='linear', 
                dtick=0.5,            # Set y-axis to logarithmic scale
                range=[0.00,5.10]         # Auto-range to fit the data
            ),
        )

        # Display the chart in Streamlit
        st.plotly_chart(fig, key=f"key_{Ratings_bucket}_{sector}", use_container_width=True, config=config)

# Initialize session state to keep track of which expander is open
if 'open_expander' not in st.session_state:
    st.session_state.open_expander = None

# Function to set the currently open expander
def set_open_expander(expander_name):
    st.session_state.open_expander = expander_name


st.markdown("""
<style>
  [aria-label="dialog"] {
    width: 65% !important;
  }
</style>
""", unsafe_allow_html=True)




@st.dialog("Sub-Sector Comparison Data | Sustainable Development Goals", )
def pop_up_fun(selectedsubcategory, unpivoted_df, i):
                    
                    
                    
                    table_html = """
                                <div style="
                                    background-color: transparent;
                                    text-align: left;
                                    color: #003300;
                                    font-family: 'Outfit', sans-serif;
                                    font-size: 15px;
                                    border-radius: 5px; 
                                    padding:10px;
                                    margin-top:2px;
                                    overflow-y: auto; 
                                    line-height: 1.6;                                ">          
                                    <table style="width: 100%; border-collapse: collapse; text-align: left; box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.1); position: sticky;  top: 0; z-index: 2;">
                                                    <thead style="background: #c8c8c8; color: #000; box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.2); position: sticky;  top: 0; z-index: 1;">
                                            <tr>
                                                <th style="padding: 12px; font-weight: bold; text-align: left;">SubCategory</th>
                                                <th style="padding: 12px; font-weight: bold; text-align: center; ">Score</th>
                                            </tr>
                                        </thead>
                                        <tbody>   """

                    # Dynamically generate rows based on `ranked_table`
                    for index, row in selectedsubcategory.iterrows():
                        # Determine row background color based on RANK (odd/even)

                        if row['Weighted']=='Yes':
                            subcategory_weighted= row['SubCategory']  + " (Weighted)"
                            
                            weighted= '(Weighted)'
                        else:
                            subcategory_weighted= row['SubCategory']  
                            weighted= ''



                        table_html += f"""
                            <tr style="background: #FFFFFF; box-shadow: inset 0 0 5px rgba(0, 0, 0, 0.1);">
                                <td style="padding: 12px; text-align: left;  ">{subcategory_weighted}</td>
                                <td style="padding: 12px; text-align: center;  ">{   replace_na( row['SCORE'] )   }</td>                    </tr>                """

                    # Close table and div tags
                    table_html += """                    </tbody>                </table>            </div>            """


                    
                    create_category_graph(unpivoted_df, i, i)

                    st.markdown(f'''
                                <div style="display: flex; flex-direction: column; align-items: flex-start; width: 100%; 
                                margin-top: 15px; font-size: 20px; color: #000; padding: 20px; padding-left: 0px;">
                                    <div style="text-align: left; font-size: 20px; font-weight: 600; margin-bottom: 10px; ">
                                        Individual data points {weighted}
                                    </div>
                                </div>
                            ''', unsafe_allow_html=True)  

                    
                    st.markdown(table_html, unsafe_allow_html=True)

st.markdown("""
    <style>
    [data-webbase="popover"] {
        position: fixed !important; /* Make it fixed to stay centered */
        top: 50% !important; 
        left: 50% !important;
        transform: translate(-50%, -50%) !important; /* Shift it back by 50% of its width and height */
        z-index: 1000 !important; /* Ensure it stays on top */
        background-color: white; /* Optional: Ensure visibility */
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2); /* Optional: Add shadow for better visibility */
        border-radius: 10px; /* Optional: Smooth corners */
        padding: 15px; /* Optional: Add some spacing inside */
        width: auto; /* Optional: Adjust width as needed */
        max-width: 80%; /* Optional: Prevent it from becoming too wide */
    }


  [data-testid="stPopoverButton"] {
    background-color: white; /* Optional: Ensure visibility */
    border-radius: 10px; /* Smooth corners */
    width: 100%; /* Make it stretch full width */
    text-align: left !important; /* Ensure text aligns to the left */
    justify-content: flex-start !important; /* Align text properly in flex containers */
    display: flex; /* Ensure alignment works as expected */
}



    </style>
""", unsafe_allow_html=True)

def split_into_three(category_list):
        n = len(category_list)
        part_size = (n + 2) // 3  # Ensures roughly equal split
        
        return [
            category_list[:part_size],
            category_list[part_size: 2 * part_size],
            category_list[2 * part_size:]
        ]



def replace_na(value):
    if value in [None, 'None'] or (isinstance(value, float) and math.isnan(value)) or pd.isna(value):
        return 'N/A'
    return round(value,2) 


def DeepDive(raw_df, ranked_table):
    
    selected_company = st.session_state.selected_company 
    
    # st.selectbox('**Select Company**', options=company_unique)

    #selected_score= ranked_table[ranked_table['COMPANY']==selected_company]['SCORE'].iloc[0]

    category_list = raw_df[raw_df['COMPANY']==selected_company]['Category'].unique()
    #subcategory= raw_df[raw_df['COMPANY']==selected_company]
    raw_df['SCORE'] =raw_df['SCORE']/raw_df['Weighting']

    subcategory_clean = raw_df.dropna(subset=['Category', 'COMPANY', 'SCORE'])

    sub_cat_groupby = subcategory_clean.groupby(['Category', 'COMPANY'])['SCORE'].mean().reset_index()


    subcategory= raw_df[raw_df['COMPANY']==selected_company]


    st.markdown(f'''
            <div class="kpis" style=" border: none; font-size: 38px; background-color: transparent;  padding: 5px; ">
                <span style="color: #0059FF; font-weight: 600;">{selected_company}</span> <br>
            </div>
            ''', unsafe_allow_html=True) 
    st.markdown( f'''
            <div class="kpis" style=" border: none; font-size: 1,5rem; background-color: transparent;  padding: 5px; margin-bottom: 2rem;">
                <span  style="text-align: left; font-size: 1.5rem; font-weight: 500;  margin-top: 0; ">Sub-Sector Comparison Data Scores</span>          
            </div>
            ''', unsafe_allow_html=True) 


    deep_dive_cols= st.columns(3)


    sliced_categories = split_into_three(category_list)

    for idx, i in enumerate(sliced_categories):

        with deep_dive_cols[idx]:  
            
            for idx, i in enumerate(i):
                selectedsubcategory= subcategory[subcategory['Category']==i]
                selectedcategoryavg_base= selectedsubcategory.groupby('Category')['SCORE'].mean()


                selectedcategoryavg_base = selectedsubcategory.groupby('Category')['SCORE'].mean().apply(
    lambda x: math.ceil(x * 100) / 100 if not pd.isna(x) else np.nan
)

                selectedcategoryavg =   replace_na(selectedcategoryavg_base.get(i)) 


                expander_label= f'''{i} : **{selectedcategoryavg }**'''
    
                if st.button(expander_label, type= 'secondary'):
                    pop_up_fun(selectedsubcategory, raw_df, i)
   
    st.markdown('-----', unsafe_allow_html=True)
    st.markdown(footer, unsafe_allow_html=True)










load_raw_data= "Finteldata_cleaned.xlsx"





def loading_data(load_raw_data):

    df = pd.read_excel(load_raw_data, decimal='.', sheet_name='RawDataPoints')
    weightings = pd.read_excel(load_raw_data, decimal='.', sheet_name= 'Weightings')
    summary = pd.read_excel(load_raw_data,  sheet_name='Summary')
    Pesgo_Risks = pd.read_excel(load_raw_data,  sheet_name='Pesgo_Risks')
    revenue_excel = pd.read_excel(load_raw_data,  sheet_name='Revenue')
    Financial_Data = pd.read_excel(load_raw_data,  sheet_name='Financial_Data')

    



    return df, weightings, summary, Pesgo_Risks, revenue_excel,  Financial_Data 



df, weightings, summary, Pesgo_Risks, revenue_excel, Financial_Data = loading_data(load_raw_data)


summary['COMPANY'] = summary['COMPANY'].astype(str)
Pesgo_Risks['COMPANY'] = Pesgo_Risks['COMPANY'].astype(str)


summary.columns = summary.columns.str.strip()

revenue_base = summary[['CompanyFullName', 'TickerSymbol', 'Exchange']]

revenue_base['Company'] = revenue_base['CompanyFullName']









value_vars = df.columns.difference(['Category', 'SubCategory', 'Ratings_bucket']).tolist()

unpivoted_df = raw_df= pd.melt(df, id_vars=['Category', 'SubCategory', 'Ratings_bucket'], 
                       value_vars=value_vars,
                       var_name='COMPANY', value_name='BaseScore')




company_mapping = dict(zip(summary['COMPANY'], summary['CompanyFullName']))
ticker_mapping = dict(zip(summary['TickerSymbol'], summary['CompanyFullName']))

business_mapping = dict(zip(summary['CompanyFullName'], summary['Business']))
company_short_name_mapping = dict(zip(summary['CompanyFullName'], summary['CompanyShortName']))


unpivoted_df['COMPANY'] = unpivoted_df['COMPANY'].map(company_mapping)
Financial_Data['COMPANY'] = Financial_Data['COMPANY'].str.strip().map(company_mapping)

Pesgo_Risks['COMPANY'] = Pesgo_Risks['COMPANY'].map(company_mapping)
#st.write(Financial_Data)


# Dictionary to map old field values to new values
rename_mapping = {
    "Asset performance and shareholder risk": "Assets and Risk",
    "Compliance and Financial": "Compliance and Financial",
    "Earth": "Earth",
    "Executive and non-Executive Board": "Executive Board",
    "Governance": "Governance",
    "Market Exposure": "Market Exposure",
    "Operational": "Operational",
    "Performance Outlook": "Performance",
    "Regulatory performance across markets": "Regulatory performance",
    "Responsible Gambling": "Responsible Gambling",
    "Society": "Society"
}




pesgo_list= ['Earth','Society','Governance','Operational','Performance Outlook',
                 'Compliance and Financial',
                 'Market Exposure','Responsible Gambling','Executive and non-Executive Board',
                 'Regulatory performance across markets','Asset performance and shareholder risk']  


#st.write(unpivoted_df)
raw_df['SCORE']= raw_df['BaseScore']

raw_df = raw_df.merge(
                                        weightings,
                                        on=["Category", "SubCategory"], 
                                        how="left" 
                                    )



raw_df["Weighting"] = raw_df["Weighting"].fillna(1)
raw_df["Weighted"] = raw_df["Weighted"].fillna('No')

def data_prep( unpivoted_df, rename_mapping):

    unpivoted_df.replace(
                            ['N/A', 'N/a', 'n/a', 'NA', 'NaN', 'nan', None, '',0,  pd.NaT],
                            pd.NA,
                            inplace=True
                        )

    unpivoted_df.dropna(inplace=True)

    unpivoted_df = unpivoted_df.merge(
                                        weightings,
                                        on=["Category", "SubCategory"], 
                                        how="left" 
                                    )

    unpivoted_df["Weighting"] = unpivoted_df["Weighting"].fillna(1)
    unpivoted_df["Weighted"] = unpivoted_df["Weighted"].fillna('No')

    unpivoted_df['SCORE'] = pd.to_numeric(unpivoted_df['BaseScore'] / unpivoted_df["Weighting"]    , errors='coerce')


    weighted_yes=  unpivoted_df[unpivoted_df['Weighted'] == "Yes"].groupby(
                ['Ratings_bucket', 'COMPANY' ]
            )['SCORE'].mean().reset_index()


    weighed_no_base=   unpivoted_df[unpivoted_df['Weighted'] == "No"].groupby(
                ['Ratings_bucket', 'COMPANY', 'Category']
            )['SCORE'].mean().reset_index()

    weighed_no = weighed_no_base.groupby(
                ['Ratings_bucket', 'COMPANY' ]
            )['SCORE'].mean().reset_index()

    weighted_append = pd.concat([weighted_yes, weighed_no], ignore_index=True)

    Final_weighted= weighted_append.groupby(
                ['Ratings_bucket', 'COMPANY' ]
            )['SCORE'].mean().reset_index()



    #st.write(unpivoted_df[unpivoted_df['COMPANY']=='Aristocrat Leisure Limited'])
    #st.write(weighed_no[weighed_no['COMPANY']=='Aristocrat Leisure Limited'])
#    st.write(weighted_yes[weighted_yes['COMPANY']=='Caesars Entertainment'])
#    st.write(Final_weighted[Final_weighted['COMPANY']=='Caesars Entertainment'])
    
    
    ranked_table= Final_weighted.groupby(['COMPANY', 'Ratings_bucket'])['SCORE'].mean().reset_index()
    #.apply(    lambda x: math.ceil(x * 100) / 100 if not pd.isna(x) else np.nan)
    
    #e['Score']= e['Score'].apply(lambda x: f"{x:.2f}")

    ranked_table= ranked_table.groupby(['COMPANY'])['SCORE'].mean().reset_index()

    #ranked_table['RANK'] = ranked_table['SCORE'].rank(method='min', ascending=False).astype(int)
    #ranked_table['SCORE'] = ranked_table['Score'].apply(lambda x: round(float(x), 2))  # Explicit rounding

    ranked_table = ranked_table.sort_values(by=['SCORE', 'COMPANY'], ascending=[False, False]).reset_index(drop=True)

# Then assign ranks (now order is already correct)
    ranked_table['RANK'] = ranked_table.index + 1
    #st.write(ranked_table)

    ranked_table['SCORE']= ranked_table['SCORE'].astype(str).str[:2] + ranked_table['SCORE'].astype(str).str.split('.').str[1].str[:2]

    ranked_table['MARKET'] = ranked_table['COMPANY'].map(business_mapping)
    ranked_table = ranked_table.sort_values(by='RANK' )

    weighted_append['COMPANY'] = weighted_append['COMPANY'].map(company_short_name_mapping)

    max_score = Final_weighted.groupby(['COMPANY',  'Ratings_bucket'])['SCORE'].max().reset_index()
    
    #st.write(max_score[max_score['Ratings_bucket']=='Society'])

    max_score['SCORE'] = pd.to_numeric(max_score['SCORE'], errors='coerce').round(2)
    circular_table2 = max_score.groupby(['SCORE', 'Ratings_bucket']).agg( COMPANY=('COMPANY', lambda x: ', '.join(map(str, x))), ).reset_index()


    circular_table2['COMPANY'] = circular_table2['COMPANY'].apply(
        lambda text: ', '.join(text.split(',')[:2]) + ', ' + '<br>' + ', '.join(text.split(',')[2:]) 
        if text.count(',') >= 2 else text
    )
    circular_table3 = circular_table2[circular_table2['SCORE'] == circular_table2.groupby('Ratings_bucket')['SCORE'].transform('max')]
    circular_table3['Ratings_bucket'] = circular_table3['Ratings_bucket'].replace(rename_mapping)

    return  unpivoted_df, circular_table3, ranked_table,Final_weighted


unpivoted_df, circular_table3 , ranked_table,Final_weighted = data_prep(unpivoted_df, rename_mapping)


circular_table3['SCORE'] = circular_table3['SCORE'].apply(lambda x: f"{float(x):.2f}")

# Supabase credentials


# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = None

def login(email, password):
    try:
        response = supabase.auth.sign_in_with_password({"email": email, "password": password})
        if response.user:
            st.session_state.user = response.user
            login_response = True
        else:
            st.error("Login attempt unsuccessful. Incorrect username or password.")
            login_response = False

    except Exception as e:
        login_response = False
        st.error(f"Login failed: {e}")

        return login_response

@st.dialog('Sign up')
def signup(email, password):
    try:
        response = supabase.auth.sign_up({"email": email, "password": password})
        if response.user:
            st.success("Sign-up successful! Please check your email to confirm your account.")
        else:
            st.error("Sign-up failed. No user information received.")
    except Exception as e:
        st.error(f"Sign-up failed: {e}")

# Logout function
def temp_show_notification(msg, color_code):
    st.session_state.user = None
    
    notification_placeholder = st.empty()
                    
                        # Display the notification
    notification_placeholder.markdown(
                            f"""
                            <div style='display: flex; justify-content: center; align-items: center; 
                                         background-color: {color_code}; 
                                         position: fixed; 
                                         color: white; 
                                         font-size: 20px; 
                                         font-weight: bold; 
                                         padding: 15px 30px; 
                                         margin: 0;
                                         top: 50%;  
                                         left: 50%; 
                                         transform: translateX(-50%); 
                                         border-radius: 10px;  
                                         box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); 
                                         z-index: 1000;
                                         '>
                                {msg}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                    
                        # Pause for 1 second
    time.sleep(3)
                    
                        # Clear the notification after 1 second
    notification_placeholder.empty()
    st.rerun()







@st.dialog('Profile Details')
def profile():
    user = st.session_state.user
    
    # Editable user details
    name = st.text_input("Name", value=user.user_metadata.get("name", ""))
    address = st.text_area("Address", value=user.user_metadata.get("address", ""))

    # Country dropdown
    country_list = [country.name for country in pycountry.countries]
    selected_country = st.selectbox(
        "Country",
        options=country_list,
        index=country_list.index(user.user_metadata.get("country", "India")) if user.user_metadata.get("country") else 0,
    )
    
   
    contact = st.text_input("Contact Number", value=user.user_metadata.get("contact", ""))

    # Display email as non-editable
    email = user.email

    # Save updated profile details
    if st.button("Update Profile"):
        try:
            response = supabase.auth.update_user(
                user_metadata={
                    "name": name,
                    "contact": contact,
                    "address": address,
                    "country": selected_country,
                    "country_code": selected_country_code.split()[0],  # Save only the code
                }
            )
            if response:
                st.success("Profile updated successfully!")
        except Exception as e:
            st.error(f"Failed to update profile: {e}")

    # Change password
    with st.expander("Change Password" ):
        new_password = st.text_input("New Password", type="password")
        confirm_password = st.text_input("Confirm New Password", type="password")
        
        if st.button("Change Password"):
            if new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                try:
                    response = supabase.auth.update_user({"password": new_password})
                    if response:
                        st.success("Password changed successfully!")
                except Exception as e:
                    st.error(f"Failed to change password: {e}")



st.markdown("""
<style>

	.stTabs [data-baseweb="tab-list"] {
		gap: .25rem;
    }

    .stTabs [data-baseweb="tab"] {
        height: 2.5rem;
        background-color: #FFFFFF;
        border-radius: 4px 4px 0px 0px;
        border: 2px solid #E8E6E6;
        opacity: 1;
        padding-top: .5rem;
        padding-bottom: .5rem;
        min-width: 15%;
    }

        

    .stTabs [data-baseweb="tab"]:hover > div > p {
        color: #0F52BA  ;   /* Change text color on hover */
        font-weight: bold; /* Make the text bold on hover */
    }

     .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1rem;
    }

	.stTabs [aria-selected="true"] > div > p {
        color: #0059FF       !important; /* Makes the text green */
        font-size: 1rem !important; /* Increases font size */
        font-weight: 750 !important; /* Makes text bold */
    }

    .stTabs [aria-selected="true"] * {
        font-weight: 750 !important;
    }

    #root > div:nth-child(1) > div > div > div > div > section > div {padding-top: 0rem;}



    [data-testid="stVerticalBlock"] {
            gap: .01rem;
            display: flex !important;
            flex-direction: column !important;
            justify-content: stretch !important;
        }

    [data-testid="stVerticalBlockBorderWrapper"] {
            height: auto !important; /* Allows content to expand */
        }

</style>""", unsafe_allow_html=True)

options = ["**Top 20 Companies**",  "**Company Dashboard**", "**Deep Dive**",  "**Key Company Data**"]





def main_app():

    logo= st.columns([1.75,7,3])

    with logo[0]:
        st.markdown(
    f'''
    <div style="width: 100%; text-align: center;">
        <img src="data:image/png;base64,{sustainability_logo}" 
             alt="Logo" 
             style="width: 30vw; 
                    max-width: 225px; 
                    height: auto; 
                    margin-bottom: 15px;">
    </div>
    ''', 
    unsafe_allow_html=True
)




    with logo[2]:
        with st.container():
            button_cols = st.columns(2)

            with button_cols[0]:
                if  st.button('**Q1 2025**', type= 'primary'):
                    temp_show_notification( 'Signed out successfully.', 'rgb(0, 45, 128)' )
            with button_cols[1]:
                if  st.button('**Sign Out**', type= 'primary'):
                    temp_show_notification( 'Signed out successfully.', 'rgb(0, 45, 128)' )
    tab1, tab2, tab3, tab4= st.tabs( options )

    with logo[1]:
    

        with tab1:
            with st.container( border=None):
                #st.write(ranked_table)
                top20companies3(ranked_table, 20, circular_table3)

        with tab2:
            with st.container( border=None ):
                summary['COMPANY'] = summary['CompanyFullName']
                CompanyDashboard(Final_weighted, summary , pesgo_list, Pesgo_Risks, revenue_excel, Financial_Data)
        with tab3:
            with st.container(border=None ):
                DeepDive(raw_df, ranked_table)

        with tab4:
            filtered_df = raw_df[raw_df["COMPANY"] == st.session_state.selected_company]

            # Get unique categories
            categories = filtered_df["Category"].unique()

            st.markdown(
            '''
            <div class="custom-header">
                    Data/Touch Points and Key Indicators
                    <div style="
                                    background-color: #FFFFFF; 
                                    padding:0px;
                                    border-radius: 5px; 
                                    font-family: 'Outfit', sans-serif; 
                                    font-size: 1.25rem; 
                                    text-align: justify;
                                    color: #000; 
                                    font-weight:normal;
                                    line-height:1.25;
                                        ">  Analyzing key measurements against United Nations Sustainable Development Goals, 
                                            Earth, Society and Governance factors, Operational and Financial Performance criteria through FiNTEL 
                                            Sustain’s SustainabilityPlus platform. 
                                            Utilizing 25 discrete datasets with over 170 data inputs per company.
                                </div>
            </div>
            ''',    unsafe_allow_html=True )
            st.markdown(
            '''-------''',    unsafe_allow_html=True )



            # Create a layout with five columns
            category_counts = filtered_df.groupby("Category")["SubCategory"].count().sort_values(ascending=False)

            # Distribute categories into columns dynamically based on content size
            cols = st.columns(6)  # Create 5 columns
            col_heights = [0] * 6  # Track height of each column

            # Assign categories to columns based on least occupied space
            for category in category_counts.index:
                min_col = col_heights.index(min(col_heights))  # Find the least filled column
                with cols[min_col]:  
                    st.markdown(f"""<p style="font-size:18px; font-weight:bold; color:#0F52BA ; font-family: 'Outfit', sans-serif;  ">{category}</p>""", unsafe_allow_html=True)  # Category heading
                    subcategories = filtered_df[filtered_df["Category"] == category]["SubCategory"]
                    for subcat in subcategories:
                        #st.markdown(f"- {subcat}")  # Display subcategories
                        st.markdown(f'''<p style="font-size:14px; font-family: 'Outfit', sans-serif;  "> <span style="color:black; font-family: 'Outfit', sans-serif; ">●</span>  { subcat}</p>''', unsafe_allow_html=True)  # Category heading


                    col_heights[min_col] += len(subcategories) + 1  # Update column height estimate


            st.write('-----')
            st.markdown(footer, unsafe_allow_html=True)
            
            

    
query_params = st.query_params

# Display them in the app
#st.write("Query Parameters received:")
#st.json(query_params)

# Access individual parameters
user_id = query_params.get("user_id", None)
session_token = query_params.get("session_token", None)

#st.write(f"User ID: {user_id}")
#st.write(f"Session Token: {session_token}")



# Maange user log in 

#main_app()
#st.stop()

if st.session_state.user or token =='ba72f9c30d5c7fc8be7e4a6c80b4f5c88cf892c70718ea8f6f3c51c5e6c2aa9b':
    # Main app content here
    main_app()

else:
    # Login and Sign-Up views
    login_cols= st.columns(3)
    with login_cols[1]:
        st.markdown("""
            <div style="text-align: left; padding: 0px; margin-bottom: 15px;">
                <h2>Log In</h2>
            </div>
        """, unsafe_allow_html=True)


        with login_cols[1]:
            email = st.text_input("Email",  placeholder='Email', label_visibility= 'collapsed')
            st.markdown(            """
                        <div style="height: 1rem; text-align: center; font-size: 18px; font-weight: bold; color: transparent; padding: 10px;">
                BUTTON GAP
            </div>         """,           unsafe_allow_html=True       )
            
            password = st.text_input("Password", placeholder='Password', label_visibility= 'collapsed', type="password")

            st.markdown(            """
                        <div style="height: 1rem; text-align: center; font-size: 18px; font-weight: bold; color: transparent; padding: 10px;">
                PASSWORD GAP
            </div>         """,           unsafe_allow_html=True       )
    
    
    with login_cols[1]:
        buttons= st.columns(2)
        with buttons[0]:
            if st.button("**Login**",key='loginbutton', type ='tertiary' ):
                login_response=login(email, password)
                if login_response:
                    st.rerun()
                


                

        #with buttons[1]:
         #   st.write('')
          #  if st.button("**Sign up**", type ='secondary' ):
           #     signup(email, password)
            #    st.rerun()
    
  



 
