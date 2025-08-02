# Market-Customer-segmentation-Data-Analytics--Dashboard
I developed a complete customer segmentation project using Python for data cleaning, clustering, and visualization. Integrated with Power BI for dynamic dashboard updates linked to live Excel data on OneDrive



## Project Overview
This project performs customer segmentation using clustering techniques to help businesses target personalized marketing campaigns effectively. The dataset contains customer demographics and behavioral data such as Age, Annual Income, and Spending Score.

Using Python (Pandas, Scikit-learn) for data analysis and clustering, and Power BI for visualization and dashboarding, the project demonstrates an end-to-end data analytics workflow including data cleaning, exploratory data analysis, machine learning modeling, and dynamic reporting.

A key feature of the project is an **auto-refreshing Power BI dashboard** that automatically updates when the connected Excel data stored on OneDrive/SharePoint is modified.

---
Dataset Used:
kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python
---

## Tools and Technologies Used

- Python 3.x
- Jupyter Notebook
- Pandas, NumPy, Matplotlib, Seaborn
- Scikit-learn (KMeans Clustering)
- Power BI Desktop


---

## Step-by-Step Workflow

 1. Setting up the Project Environment
- Create project folder and subfolders as above.
- Set up Python virtual environment and install required packages via `requirements.txt`.

 2. Data Preparation and Exploration
- Download and place the dataset (`customers.csv`) inside `data/`.
- Use Jupyter Notebook (`customer_segmentation.ipynb`) to load data, clean missing values, remove duplicates.
- Perform exploratory data analysis (EDA) with visualizations such as pair plots. 

 3. Feature Selection and Scaling
- Select key features (`Age`, `Annual Income (k$)`, `Spending Score`) for clustering.
- Scale features using `StandardScaler`.

 4. Finding Optimal Number of Clusters
- Use the Elbow Method to identify the optimal `k` value for KMeans.
- Visualize Sum of Squared Distances vs number of clusters.
<img width="905" height="857" alt="Screenshot 2025-08-02 223539" src="https://github.com/user-attachments/assets/36944116-0f39-49b2-80f8-d591ec573321" />

 5. Clustering and Analysis
- Fit KMeans with the optimal cluster number.
- Assign clusters back to data.
- Visualize clusters using scatter plots categorized by cluster labels.
- Summarize cluster characteristics by mean values.
- 

<img width="725" height="764" alt="Screenshot 2025-08-02 223551" src="https://github.com/user-attachments/assets/ea305f96-df4a-451b-a4f8-7236b3829d59" />
<img width="916" height="582" alt="Screenshot 2025-08-02 223603" src="https://github.com/user-attachments/assets/12ee9029-074f-4164-98e3-71414d44a91f" />

 6. Power BI Dashboard with Auto-refresh
- Save the clustered data as an Excel file (`customer_segments.xlsx`).
- Upload Excel to OneDrive or SharePoint Online.
- Connect Power BI Desktop to this Excel file via cloud connection.
- Create interactive visuals (scatter plots, bar charts) including cluster information.
- Publish the report to Power BI Service.
- Configure Scheduled Refresh in Power BI Service settings to enable automatic data updates when the Excel file changes.
- Dashboard reflects updated data after refresh without manual intervention.

<img width="1168" height="660" alt="Screenshot 2025-08-02 184938" src="https://github.com/user-attachments/assets/37c1b25f-0e33-4671-94f8-eff8fa533ee9" />

---

## How to Run This Project

1. Clone this repository to your local machine.
2. Set up and activate a Python environment and install packages:  



