# vehicles_project

##  Project Links

- GitHub Repository: (https://github.com/santy7272/vehicles_project)
- Render: (https://vehicles-project-5398.onrender.com)

This is a small web-based data analysis project using Streamlit, focused on used car listings in the U.S.

The goal was to explore trends in vehicle prices, mileage, fuel types and conditions using interactive visualizations.

## Tools Used as mandatory in the project

- Python
- Streamlit
- pandas
- plotly.express

## What the app shows

- A dataset preview with a checkbox
- A price distribution histogram
- A scatter plot of price vs. model year (filterable by condition)
- A histogram just for Jeep Wrangler (because it’s my favorite)
- A comparison of price by fuel type (this one is not that nice visualy as there are a lot of pretol instead of diesel)

I tried to keep it simple and not overload the app. It could be improved later by adding filters or dropdowns for model or year (I ran out of time for that...).

## How to run

Clone the repo and run (make sure vehicles_us.csv is in the root folder):

```bash

git clone  https://github.com/santy7272/vehicles_project.git
cd your-repo-name
pip install -r requirements.txt
streamlit run app.py


