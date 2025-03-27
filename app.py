import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page configuration
st.set_page_config(
    page_title="Ophthalmologist Compensation Calculator",
    page_icon="💰",
    layout="wide"
)

# Title and description
st.title("Ophthalmologist Compensation Calculator")
st.markdown("""
This tool helps ophthalmologists compare different compensation models side by side.
Enter your parameters below to see how different formulas affect your total compensation.
""")

# Create a function to calculate compensation based on different formulas
def calculate_compensation(formula1_params, formula2_params, formula3_params, net_collections):
    """Calculate compensation using three different formulas with their own parameters."""
    
    # Extract formula 1 parameters
    base_salary1 = formula1_params["base_salary"]
    multiplier1 = formula1_params["multiplier"]
    bonus_percentage1 = formula1_params["bonus_percentage"]
    
    # Extract formula 2 parameters
    base_salary2 = formula2_params["base_salary"]
    multiplier2 = formula2_params["multiplier"]
    bonus_percentage2 = formula2_params["bonus_percentage"]
    
    # Extract formula 3 parameters
    base_salary3 = formula3_params["base_salary"]
    multiplier3 = formula3_params["multiplier"]
    bonus_percentage3 = formula3_params["bonus_percentage"]
    
    # Formula 1: Base + Bonus over threshold
    formula1_threshold = base_salary1 * multiplier1
    formula1_bonus = max(0, net_collections - formula1_threshold) * (bonus_percentage1 / 100)
    formula1_total = base_salary1 + formula1_bonus
    
    # Formula 2: Base + Bonus over threshold (same approach as Formula 1)
    formula2_threshold = base_salary2 * multiplier2
    formula2_bonus = max(0, net_collections - formula2_threshold) * (bonus_percentage2 / 100)
    formula2_total = base_salary2 + formula2_bonus
    
    # Formula 3: Base + Bonus over threshold (same approach as Formula 1)
    formula3_threshold = base_salary3 * multiplier3
    formula3_bonus = max(0, net_collections - formula3_threshold) * (bonus_percentage3 / 100)
    formula3_total = base_salary3 + formula3_bonus
    
    return {
        "Formula 1: Base + Bonus": {
            "description": "Base salary plus bonus percentage of collections above threshold",
            "base_component": base_salary1,
            "bonus_component": formula1_bonus,
            "total": formula1_total,
            "details": {
                "Bonus Threshold": f"${formula1_threshold:,.2f}",
                "Collections Above Threshold": f"${max(0, net_collections - formula1_threshold):,.2f}",
                "Bonus Rate": f"{bonus_percentage1}%"
            }
        },
        "Formula 2: Base + Bonus": {
            "description": "Base salary plus bonus percentage of collections above threshold",
            "base_component": base_salary2,
            "bonus_component": formula2_bonus,
            "total": formula2_total,
            "details": {
                "Bonus Threshold": f"${formula2_threshold:,.2f}",
                "Collections Above Threshold": f"${max(0, net_collections - formula2_threshold):,.2f}",
                "Bonus Rate": f"{bonus_percentage2}%"
            }
        },
        "Formula 3: Base + Bonus": {
            "description": "Base salary plus bonus percentage of collections above threshold",
            "base_component": base_salary3,
            "bonus_component": formula3_bonus,
            "total": formula3_total,
            "details": {
                "Bonus Threshold": f"${formula3_threshold:,.2f}",
                "Collections Above Threshold": f"${max(0, net_collections - formula3_threshold):,.2f}",
                "Bonus Rate": f"{bonus_percentage3}%"
            }
        }
    }

# Create sidebar for inputs
st.sidebar.header("Net Collections")

# Net collections slider - common for all formulas
net_collections = st.sidebar.slider(
    "Net Collections ($)",
    min_value=100000,
    max_value=3000000,
    value=1000000,
    step=50000,
    help="Total amount collected after adjustments"
)

# Formula 1 inputs
st.sidebar.header("Formula 1 Parameters")
base_salary1 = st.sidebar.number_input(
    "Base Salary ($) - Formula 1",
    min_value=0,
    max_value=1000000,
    value=300000,
    step=10000,
    help="Enter base annual salary for Formula 1"
)

multiplier1 = st.sidebar.number_input(
    "Base Salary Multiplier - Formula 1",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.1,
    help="Multiplier used to determine bonus threshold for Formula 1"
)

bonus_percentage1 = st.sidebar.number_input(
    "Bonus Percentage (%) - Formula 1",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0,
    help="Percentage of collections above bonus threshold that will be paid as bonus for Formula 1"
)

# Formula 2 inputs
st.sidebar.header("Formula 2 Parameters")
base_salary2 = st.sidebar.number_input(
    "Base Salary ($) - Formula 2",
    min_value=0,
    max_value=1000000,
    value=300000,
    step=10000,
    help="Enter base annual salary for Formula 2"
)

multiplier2 = st.sidebar.number_input(
    "Base Salary Multiplier - Formula 2",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.1,
    help="Multiplier used to determine bonus threshold for Formula 2"
)

bonus_percentage2 = st.sidebar.number_input(
    "Bonus Percentage (%) - Formula 2",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0,
    help="Percentage of collections above bonus threshold that will be paid as bonus for Formula 2"
)

# Formula 3 inputs
st.sidebar.header("Formula 3 Parameters")
base_salary3 = st.sidebar.number_input(
    "Base Salary ($) - Formula 3",
    min_value=0,
    max_value=1000000,
    value=300000,
    step=10000,
    help="Enter base annual salary for Formula 3"
)

multiplier3 = st.sidebar.number_input(
    "Base Salary Multiplier - Formula 3",
    min_value=1.0,
    max_value=5.0,
    value=3.0,
    step=0.1,
    help="Multiplier used to determine bonus threshold for Formula 3"
)

bonus_percentage3 = st.sidebar.number_input(
    "Bonus Percentage (%) - Formula 3",
    min_value=0.0,
    max_value=100.0,
    value=30.0,
    step=1.0,
    help="Percentage of collections above bonus threshold that will be paid as bonus for Formula 3"
)

# Create parameter dictionaries for each formula
formula1_params = {
    "base_salary": base_salary1,
    "multiplier": multiplier1,
    "bonus_percentage": bonus_percentage1
}

formula2_params = {
    "base_salary": base_salary2,
    "multiplier": multiplier2,
    "bonus_percentage": bonus_percentage2
}

formula3_params = {
    "base_salary": base_salary3,
    "multiplier": multiplier3,
    "bonus_percentage": bonus_percentage3
}

# Calculate the compensation using the three formulas
results = calculate_compensation(formula1_params, formula2_params, formula3_params, net_collections)

# Display the thresholds for reference
threshold1 = base_salary1 * multiplier1
threshold2 = base_salary2 * multiplier2
threshold3 = base_salary3 * multiplier3

# Display the results in three columns
col1, col2, col3 = st.columns(3)

# Helper function to display the threshold and formula results
def display_formula(container, formula_name, data, params, threshold):
    with container:
        st.subheader(formula_name)
        
        # Display the parameters
        st.markdown("#### Parameters Used")
        st.markdown(f"Base Salary: ${params['base_salary']:,.2f}")
        st.markdown(f"Multiplier: {params['multiplier']:.1f}")
        st.markdown(f"Bonus %: {params['bonus_percentage']}%")
        
        # Create a gauge-like metric for the total
        st.metric(
            label="Total Compensation",
            value=f"${data['total']:,.2f}"
        )

        # Display the bonus threshold below the total compensation
        st.info(f"Bonus Threshold: ${threshold:,.2f}")

# Display each formula in its own column
display_formula(col1, "Formula 1", results["Formula 1: Base + Bonus"], formula1_params, threshold1)
display_formula(col2, "Formula 2", results["Formula 2: Base + Bonus"], formula2_params, threshold2)
display_formula(col3, "Formula 3", results["Formula 3: Base + Bonus"], formula3_params, threshold3)

# Create visualization comparing the formulas
st.subheader("Compensation Comparison")

# Prepare data for the graph
collection_range = np.linspace(100000, 3000000, 100)  # Fixed range from $100k to $3M
comparison_data = []

for collection in collection_range:
    comp_results = calculate_compensation(formula1_params, formula2_params, formula3_params, collection)
    comparison_data.append({
        "Net Collections": collection,
        "Formula 1": comp_results["Formula 1: Base + Bonus"]["total"],
        "Formula 2": comp_results["Formula 2: Base + Bonus"]["total"],
        "Formula 3": comp_results["Formula 3: Base + Bonus"]["total"]
    })

comparison_df = pd.DataFrame(comparison_data)

# Create and display the line chart using Plotly
fig = px.line(
    comparison_df, 
    x="Net Collections",
    y=["Formula 1", "Formula 2", "Formula 3"],
    labels={"value": "Total Compensation ($)", "variable": "Formula"},
    title="Compensation Comparison by Net Collections"
)

# Add vertical lines at the thresholds with vertical text
fig.add_shape(
    type="line",
    x0=threshold1,
    x1=threshold1,
    y0=0,
    y1=1,
    yref="paper",
    line=dict(color="blue", dash="dash")
)

fig.add_annotation(
    x=threshold1,
    y=0.5,
    yref="paper",
    text="Formula 1 Bonus Threshold",
    textangle=-90,
    showarrow=False,
    font=dict(color="blue")
)

fig.add_shape(
    type="line",
    x0=threshold2,
    x1=threshold2,
    y0=0,
    y1=1,
    yref="paper",
    line=dict(color="green", dash="dash")
)

fig.add_annotation(
    x=threshold2,
    y=0.5,
    yref="paper",
    text="Formula 2 Bonus Threshold",
    textangle=-90,
    showarrow=False,
    font=dict(color="green")
)

fig.add_shape(
    type="line",
    x0=threshold3,
    x1=threshold3,
    y0=0,
    y1=1,
    yref="paper",
    line=dict(color="red", dash="dash")
)

fig.add_annotation(
    x=threshold3,
    y=0.5,
    yref="paper",
    text="Formula 3 Bonus Threshold",
    textangle=-90,
    showarrow=False,
    font=dict(color="red")
)

# Add a point for the current collection level
for formula in ["Formula 1", "Formula 2", "Formula 3"]:
    current_point = comparison_df.loc[comparison_df["Net Collections"] == collection_range[np.argmin(np.abs(collection_range - net_collections))]]
    
    fig.add_trace(
        go.Scatter(
            x=current_point["Net Collections"],
            y=current_point[formula],
            mode="markers",
            marker=dict(size=10),
            name=f"Current: {formula}",
            showlegend=False
        )
    )

# Improve the layout
fig.update_layout(
    xaxis_title="Net Collections ($)",
    yaxis_title="Total Compensation ($)",
    legend_title="Formula",
    hovermode="x unified",
    height=500
)

# Format the axes to display as currency
fig.update_xaxes(tickprefix="$", tickformat=",.0f")
fig.update_yaxes(tickprefix="$", tickformat=",.0f")

st.plotly_chart(fig, use_container_width=True)

# Add a section to explain each formula
with st.expander("Formula Explanations"):
    st.markdown("""
    ### Formula 1: Base + Bonus
    This is a traditional model where you receive a fixed base salary plus a percentage of collections above a bonus threshold (usually a multiple of your base salary).
    
    **Calculation**: Base Salary + (Collections above bonus threshold × Bonus %)
    
    ### Formula 2: Base + Bonus
    This uses the same approach as Formula 1 but allows you to set different parameter values to compare different scenarios.
    
    **Calculation**: Base Salary + (Collections above bonus threshold × Bonus %)
    
    ### Formula 3: Base + Bonus
    This uses the same approach as Formulas 1 and 2 but allows you to set a third set of parameter values for comparison.
    
    **Calculation**: Base Salary + (Collections above bonus threshold × Bonus %)
    """)

# Add notes about calculations
with st.expander("Notes on Calculations"):
    st.markdown("""
    - The bonus threshold is calculated as Base Salary × Multiplier
    - Each formula uses the same calculation method (Base Salary + Bonus)
    - This is the most common compensation formula in medical practices
    - All three formulas can be configured with different parameters to compare scenarios
    - All calculations are simplified models and may not reflect specific contractual terms
    - Tax implications are not considered in these calculations
    """)

# Footer
st.markdown("---")
st.caption("This calculator is for informational purposes only and does not constitute financial advice.")
