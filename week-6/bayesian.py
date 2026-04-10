
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.inference import VariableElimination
import pandas as pd

# Step 1: Define Dataset
data = pd.DataFrame({
    'Rain': ['No', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No'],
    'ArriveLate': ['Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No']
})

# Step 2: Define Bayesian Network Structure
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# Step 3: Train Model (Parameter Learning using MLE)
model.fit(data)

# Step 4: Display CPDs
print("Conditional Probability Distributions (CPDs):")
for cpd in model.get_cpds():
    print(cpd)

# Step 5: Initialize Inference Engine
inference = VariableElimination(model)

# Step 6: Perform Query
query_result = inference.query(
    variables=['ArriveLate'],
    evidence={'TrafficJam': 'No'}
)

# Step 7: Display Result
print("\nInference Result:")
print(query_result)