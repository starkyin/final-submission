import streamlit as st

def main():
    # Embedding CSS styles
    st.markdown("""
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 20px;
                padding: 0;
                line-height: 1.6;
            }
            h2, h3 {
                color: #333;
            }
            h2 {
                margin-top: 30px;
            }
            h3 {
                margin-top: 20px;
            }
            ul {
                list-style-type: none;
                padding-left: 0;
            }
            li {
                margin-bottom: 10px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Embedding HTML content
    st.markdown("""
        <!DOCTYPE html>

    <h1 style = "text-align: center;">Research Project</h1>
    <h3>Aim of the study</h3>
    <p>Our project aimed to investigate the relationship between temperature, population density, and land use/land cover patterns in Texas. We sought to understand how variations in temperature relate to population density and the distribution of land use types, such as residential, commercial, industrial, and green spaces.</p>

    <h3>Conclusions</h3>
    <ul>
        <li>- The population data provides insights into the distribution of people across different areas. 
            For example, the description highlights that Harris has the highest population with 
            approximately 2,835,927 people, followed by Dallas with 1,863,546 people. 
            This information helps in understanding the demographic characteristics of different regions
             and their potential impact on various socio-economic factors and public services. </li>
        <li>- The temperature data indicates the thermal conditions in urban and vegetated areas. 
            The description mentions that urban areas experience higher temperatures, with recorded 
            highs of 22°C and 20°C. This phenomenon is attributed to the urban heat island effect, where 
            urbanized areas absorb and retain more heat compared to surrounding rural or vegetated areas. 
            Conversely, vegetated areas exhibit lower temperatures due to the cooling effect of forest cover.</li>
    </ul>

    <h3>Challenges encountered in completing the project</h3>
    <ul>
        <li>- Some difficulties encountered during the project included data acquisition challenges, especially in obtaining high-resolution and up-to-date datasets for analysis.</li>
        <li>- Obtaining high-quality temperature data at a sufficient spatial and temporal resolution for urban areas proved challenging, particularly for historical or localized datasets.</li>
        <li>- Identifying reliable sources for land use/land cover data with detailed classifications and up-to-date information posed difficulties, especially for large geographic areas.</li>
    </ul>

    <h3>Skills required to complete the project</h3>
    <ul>
        <li>- Geographic information systems (GIS) for spatial analysis and visualization of temperature, population, and land use data.</li>
        <li>- Remote sensing techniques for extracting land use/land cover information from satellite imagery and aerial photographs.</li>
        <li>- Programming skills would have enhanced my ability to tackle complex data analysis challenges and develop more robust and scalable solutions for the project..</li>
        <li>- Data visualization and interpretation techniques for communicating complex spatial relationships and trends to diverse audiences.</li>
    </ul>

    <h3>Future improvements to the project</h3>
    <ul>
        <li>- Incorporate additional environmental variables, such as humidity, air quality, and vegetation indices, to enhance the analysis of urban climate dynamics.</li>
        <li>- Conduct spatial-temporal analysis to explore how temperature, population density, and land use patterns evolve over time and their implications for urban planning and climate resilience.</li>
        <li>- Evaluate the effectiveness of urban greening strategies and land use policies in mitigating the urban heat island effect and improving local climate conditions.</li>
        <li>- Collaborate with urban planners, policymakers, and community stakeholders to integrate research findings into decision-making processes and sustainable development initiatives aimed at creating healthier and more livable cities.</li>
    </ul>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
