def execute_actions(decisions):
    results = []

    for d in decisions:
        if d["action"] == "Shutdown":
            status = f"{d['resource_id']} stopped"
        elif d["action"] == "Reallocate Resources":
            status = f"{d['resource_id']} resources reallocated"
        elif d["action"] == "Remove Duplicate":
            status = f"{d['resource_id']} duplicate removed"
        else:
            status = "No action"

        results.append({
            "resource_id": d["resource_id"],
            "status": status,
            "impact_value": d["impact_value"]
        })

    return results