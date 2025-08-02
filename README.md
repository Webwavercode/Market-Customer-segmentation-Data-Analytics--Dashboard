# Market-Customer-segmentation-Data-Analytics--Dashboard
I developed a complete customer segmentation project using Python for data cleaning, clustering, and visualization. Integrated with Power BI for dynamic dashboard updates linked to live Excel data on OneDrive



## Project Overview
This project performs customer segmentation using clustering techniques to help businesses target personalized marketing campaigns effectively. The dataset contains customer demographics and behavioral data such as Age, Annual Income, and Spending Score.

Using Python (Pandas, Scikit-learn) for data analysis and clustering, and Power BI for visualization and dashboarding, the project demonstrates an end-to-end data analytics workflow including data cleaning, exploratory data analysis, machine learning modeling, and dynamic reporting.

A key feature of the project is an **auto-refreshing Power BI dashboard** that automatically updates when the connected Excel data stored on OneDrive/SharePoint is modified.

---


---

## Tools and Technologies Used

- Python 3.x
- Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn (KMeans Clustering)
- Power BI Desktop & Power BI Service
- OneDrive / SharePoint Online (for Excel data hosting)

---

## Step-by-Step Workflow

### 1. Setting up the Project Environment
- Create project folder and subfolders as above.
- Set up Python virtual environment and install required packages via `requirements.txt`.

### 2. Data Preparation and Exploration
- Download and place the dataset (`customers.csv`) inside `data/`.
- Use Jupyter Notebook (`customer_segmentation.ipynb`) to load data, clean missing values, remove duplicates.
- Perform exploratory data analysis (EDA) with visualizations such as pair plots.

*Insert Screenshot Placeholder:*  
`![Data Exploration](./screenshots/data_exploration.png)` 

### 3. Feature Selection and Scaling
- Select key features (`Age`, `Annual Income (k$)`, `Spending Score`) for clustering.
- Scale features using `StandardScaler`.

### 4. Finding Optimal Number of Clusters
- Use the Elbow Method to identify the optimal `k` value for KMeans.
- Visualize Sum of Squared Distances vs number of clusters.

*Insert Screenshot Placeholder:*  
`![Elbow Method](./screenshots/elbow_method.png)` 

### 5. Clustering and Analysis
- Fit KMeans with the optimal cluster number.
- Assign clusters back to data.
- Visualize clusters using scatter plots categorized by cluster labels.
- Summarize cluster characteristics by mean values.

*Insert Screenshot Placeholder:*  
`![Cluster Visualization](./screenshots/cluster_visualization.png)`

### 6. Reporting Insights
- Summarize actionable business insights for each cluster in the notebook.
- Export the notebook as a PDF report and save in `reports/segmentation_report.pdf`.

*Insert Screenshot Placeholder:*  
`![Report Sample](./screenshots/report_sample.png)`

### 7. Power BI Dashboard with Auto-refresh
- Save the clustered data as an Excel file (`customer_segments.xlsx`).
- Upload Excel to OneDrive or SharePoint Online.
- Connect Power BI Desktop to this Excel file via cloud connection.
- Create interactive visuals (scatter plots, bar charts) including cluster information.
- Publish the report to Power BI Service.
- Configure Scheduled Refresh in Power BI Service settings to enable automatic data updates when the Excel file changes.
- Dashboard reflects updated data after refresh without manual intervention.

*Insert Screenshot Placeholder:*  
"C:\Users\Priyanka\OneDrive\Pictures\Screenshots\Screenshot 2025-08-02 184938.png"

---

## How to Run This Project

1. Clone this repository to your local machine.
2. Set up and activate a Python environment and install packages:  



