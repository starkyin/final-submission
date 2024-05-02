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

   
<h1>Spatial Analysis on the Impact of Weather on Human Settlement and Land Cover Change</h1>

<p>The project aims to evaluate the impacts of weather on human settlements, identify vulnerable areas to climate risks, and analyze land use/land cover dynamics. Using historical weather data, the study will investigate how weather conditions influence human settlement patterns and vulnerabilities, informing targeted adaptation strategies. By integrating weather data with population density information and land use/land cover data, the project will identify areas vulnerable to extreme weather conditions. Additionally, analysis of land cover dynamics will elucidate the interactions between land use changes, urbanization, and environmental resilience, providing insights for sustainable development and climate resilience planning.</p>

<h2>Getting data</h2>
<p>Obtain climate data from National Oceanic and Atmospheric Administration (NOAA), population data from Global Human Settlement Layer and land use land cover data from USGS EarthExplorer.</p>

<h2>Data Resources:</h2>
<ul>
  <li><a href="https://earthexplorer.usgs.gov/">USGS EarthExplorer</a>: Description of data/API: USGS EarthExplorer provides access to a wide range of satellite imagery and remote sensing data, including land use/land cover datasets. This dataset represents the classification of land cover types such as urban areas, forests, agriculture, water bodies, etc. It can be used to analyze the spatial distribution of land cover types and their relationship with weather patterns.</li>
  <li><a href="https://ghsl.jrc.ec.europa.eu/">Global Human Settlement Layer (GHSL)</a>: Description of data/API: The Global Human Settlement Layer (GHSL) provides global spatial information about the human presence on the planet over the last 40 years. It includes datasets related to population distribution, built-up areas, and land use/land cover. This dataset represents the spatial distribution of human settlements, which can be valuable for understanding population density and urbanization patterns.</li>
  <li><a href="https://www.ncdc.noaa.gov/cdo-web/">NOAA Climate Data Online Tool (CDOT)</a>: Description of data/API: NOAA's Climate Data Online Tool (CDOT) provides access to a wide range of weather data including temperature, precipitation, wind speed, and more. This dataset represents historical weather observations collected from various weather stations worldwide. It includes information on daily weather conditions, which can be useful for analyzing long-term weather patterns and trends.</li>
</ul>

<h2>Combination of datasets:</h2>
<p>To combine these datasets, the GHSL dataset can be used to identify areas of high population density. Then, extract weather data from the NOAA CDOT dataset for those specific locations and time periods. Additionally, land use/land cover data from USGS EarthExplorer can be overlayed to further analyze how different land cover types within densely populated areas interact with weather conditions. This combined analysis can provide insights into how weather impacts human settlements and the environment.</p>

<p>In this research project, the goal is to explore the relationship between weather patterns, population density, and land use/land cover types. Specifically, we aim to understand how weather conditions vary across different types of human settlements and landscapes. By examining these relationships, we hope to identify patterns that can inform urban planning, disaster preparedness, and climate resilience strategies.</p>

    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
