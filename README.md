# Retail Analytics Dashboard

This project implements an end-to-end analytics solution using Azure SQL and Power BI to visualize product performance and sales trends. The solution includes data cleaning pipelines built with Python and scheduled updates via Power Automate.

## Project Structure

- **data/sample_data.csv**: Contains sample data used for analysis, including product performance and sales information.
- **notebooks/data_cleaning.ipynb**: Jupyter notebook for data cleaning processes using Python.
- **pipelines/data_cleaning_pipeline.py**: Python script defining the data cleaning pipeline.
- **powerbi/product_performance_report.pbix**: Power BI report visualizing product performance and sales trends.
- **power_automate/schedule_update_flow.json**: JSON file defining a Power Automate flow for scheduling updates.
- **sql/create_tables.sql**: SQL script for creating necessary tables in Azure SQL.
- **requirements.txt**: Lists Python dependencies required for the project.

## Setup (Follow accordingly)

1. Clone the repository to your local machine.
2. Install the required Python packages listed in `requirements.txt` using pip:
   ```
   pip install -r requirements.txt
   ```
3. Set up the Azure SQL database and run the SQL commands in `create_tables.sql` to create the necessary tables.
4. Open the Jupyter notebook `data_cleaning.ipynb` to perform data cleaning and prepare the data for analysis.
5. Use Power BI to open the `product_performance_report.pbix` file and connect it to the cleaned data.
6. Configure the Power Automate flow in `schedule_update_flow.json` to automate data cleaning and report refreshing.

## Rules

- Ensure that the sample data is updated regularly for accurate analysis.
- Modify the data cleaning pipeline as needed to accommodate changes in data structure.
- Regularly check the Power BI report for insights on product performance and sales trends.
