# plot_util.py

import pandas as pd
import numpy as np
import altair as alt

def generate_time_vs_feature_chart(model, feature_names, current_inputs, feature_to_vary, feature_range, title, x_axis_title):
    """
    Generates an Altair line chart showing the impact of one feature on prediction time.

    Args:
        model: The trained machine learning model.
        feature_names (list): The list of feature names in the correct order.
        current_inputs (dict): A dictionary of the user's current feature selections.
        feature_to_vary (str): The name of the feature to plot on the x-axis.
        feature_range (np.array): A numpy array of values for the feature to vary.
        title (str): The title of the chart.
        x_axis_title (str): The title for the x-axis.

    Returns:
        An Altair chart object.
    """
    # Create a base DataFrame with the user's fixed inputs
    plot_data = pd.DataFrame(current_inputs, index=[0])
    
    # Duplicate the row for every value in the feature range
    plot_data = pd.concat([plot_data] * len(feature_range), ignore_index=True)
    
    # Overwrite the column of the varying feature with its range of values
    plot_data[feature_to_vary] = feature_range
    
    # Make predictions on the generated data
    # Ensure the column order is correct before predicting
    plot_data['Predicted_Time'] = model.predict(plot_data[feature_names])

    # Create the base line chart
    line_chart = alt.Chart(plot_data).mark_line().encode(
        x=alt.X(f'{feature_to_vary}:Q', title=x_axis_title),
        y=alt.Y('Predicted_Time:Q', title='Predicted Time (min)')
    ).properties(
        title=title
    )
    
    # Create a vertical rule to show the user's current selection
    user_selection_value = current_inputs[feature_to_vary]
    vline = alt.Chart(pd.DataFrame({'x': [user_selection_value]})).mark_rule(color='red', strokeDash=[3,3]).encode(x='x:Q')

    return line_chart + vline