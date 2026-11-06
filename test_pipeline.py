
import pandas as pd
from pipeline import clean


def test_clean():

    # Create messy sample data
    data = pd.DataFrame({
        " First Name ": [" Humna ", "Ali", " Humna "],
        "Age": [22, 17, 22],
        "Email": ["humna@gmail.com", "ali@gmail.com", "humna@gmail.com"]
    })

    # Run cleaning function
    result = clean(data)

    # Check column names are standardized
    assert "first_name" in result.columns

    # Check extra spaces are removed
    assert result.iloc[0]["first_name"] == "Humna"

    # Check duplicate records are removed
    assert len(result) == 2
