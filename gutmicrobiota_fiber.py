# Re-importing necessary libraries to retry the analysis and visualizations
import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reload the study JSON file
file_path = '/Users/yung-peiko/Downloads/NCT03785860.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Extract relevant sections for primary outcomes
outcomes = data['protocolSection']['outcomesModule']
primary_outcomes = outcomes.get('primaryOutcomes', [])

# Summarize primary outcomes
primary_outcomes_df = pd.DataFrame(primary_outcomes)

# Display primary outcomes summary
print("Primary Outcomes:")
print(primary_outcomes_df[['measure', 'description', 'timeFrame']])

# Simulated Data for Visualization: Gut Microbiota Changes
microbiota_data = {
    'Bacteria': ['Bifidobacterium', 'Lactobacillus', 'Akkermansia muciniphila'],
    'Baseline': [0.05, 0.03, 0.01],  # Example proportions at baseline
    'Post-Intervention': [0.10, 0.07, 0.05]  # Example proportions after dietary fiber intervention
}
df_microbiota = pd.DataFrame(microbiota_data).set_index('Bacteria')

# Visualization: Gut Microbiota Changes
df_microbiota.plot(kind='bar', figsize=(8, 6))
plt.title('Change in Gut Microbiota Proportions')
plt.ylabel('Proportion (%)')
plt.xlabel('Bacteria')
plt.show()

# Simulated Data for HDL Levels
hdl_data = {
    'TimePoint': ['Baseline', 'Post-Intervention'],
    'HDL Levels (mg/dL)': [55, 65]  # Example HDL levels
}
df_hdl = pd.DataFrame(hdl_data)

# Visualization: HDL Level Changes
plt.figure(figsize=(8, 6))
sns.barplot(x='TimePoint', y='HDL Levels (mg/dL)', data=df_hdl, hue='TimePoint', dodge=False, palette='viridis', legend=False)
plt.title('Change in HDL Levels')
plt.ylabel('HDL Cholesterol (mg/dL)')
plt.show()

# Simulated Data for Short Chain Fatty Acids (SCFAs)
scfa_data = {
    'SCFA': ['Acetate', 'Propionate', 'Butyrate'],
    'Baseline': [0.3, 0.1, 0.15],  # Example concentrations at baseline (mmol/L)
    'Post-Intervention': [0.6, 0.2, 0.4]  # Example concentrations after dietary fiber intervention
}
df_scfa = pd.DataFrame(scfa_data).set_index('SCFA')

# Visualization: SCFA Concentration Changes
df_scfa.plot(kind='bar', figsize=(8, 6), color=['blue', 'green'])
plt.title('Change in Short Chain Fatty Acids Concentrations')
plt.ylabel('Concentration (mmol/L)')
plt.xlabel('Short Chain Fatty Acid')
plt.show()
