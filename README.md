# Project Structure

```
├── SocialTrendsAnalyzer.ipynb  # [MAIN] The core analysis notebook (Code, Plots, AI Insights)
├── dashboard.py                # [BONUS] Interactive Streamlit dashboard
├── insight_prompts.txt         # [DOC] Prompts used for AI generation
├── report.pdf                  # [DOC] Final Report (Methodology, Findings, Conclusion)
├── api_key.yaml                # [CONFIG] API Key for AI features (Not included in Git)
├── data/                       # [DATA] Data files (Not included in Git)
│   ├── happiness/              # World Happiness Report CSVs (2015-2019)
│   ├── gdp_per_capita.csv      # World Bank GDP Data
│   └── education_expenditure.csv # World Bank Education Data
└── README.md                   # Project Documentation
```
> **Note**: The `data/` folder and `api_key.yaml` are excluded from version control to keep the repository clean and secure.

## Setup & Installation
1.  **Environment Setup**:
    ```bash
    conda create -n social_trends python=3.12
    conda activate social_trends
    pip install pandas numpy matplotlib seaborn plotly scikit-learn google-generativeai pyyaml streamlit
    ```

2.  **Data Setup**:
    Since the `data/` folder is gitignored, you need to place the source data files in the `data/` directory as shown in the structure above.
    *   **Happiness Data**: Put `2015.csv` to `2019.csv` inside `data/happiness/`.
    *   **World Bank Data**: Put `gdp_per_capita.csv` and `education_expenditure.csv` inside `data/`.

3.  **API Key Configuration**:
    Create a file named `api_key.yaml` in the root directory and add your Google Gemini API key:
    ```yaml
    Gemini_API_KEY: YOUR_API_KEY_HERE
    ```

## Usage

### 1. Run the Analysis (Notebook)
Open `SocialTrendsAnalyzer.ipynb` in Jupyter Notebook or VS Code and run all cells.
*   This will perform data cleaning, visualization, regression, clustering, and generate AI insights.

### 2. Run the Dashboard (Bonus)
To view the interactive dashboard:
```bash
streamlit run dashboard.py
```
