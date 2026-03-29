def detect_duplicate_costs(df):
    duplicates = []
    seen_types = {}

    for _, row in df.iterrows():
        if row["type"] in seen_types:
            duplicates.append({
                "resource_id": row["resource_id"],
                "issue": "Duplicate Service",
                "cost": row["cost"]
            })
        else:
            seen_types[row["type"]] = row["resource_id"]

    return duplicates