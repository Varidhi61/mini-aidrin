def analyze_data(df):
    report = {}

    # Missing values
    report['missing_values'] = df.isnull().sum().to_dict()

    # Duplicates
    report['duplicates'] = int(df.duplicated().sum())

    # Class distribution (last column)
    target_col = df.columns[-1]
    report['class_distribution'] = df[target_col].value_counts().to_dict()

    return report