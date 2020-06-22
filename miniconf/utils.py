from typing import Dict, Any, List


def get_paper_rocketchat(paper_id):
    return "paper-" + paper_id.replace(".", "-")


def format_paper(v, by_uid):
    list_keys = ["authors", "keywords"]
    list_fields = {}
    for key in list_keys:
        list_fields[key] = extract_list_field(v, key)

    return {
        "id": v["UID"],
        "forum": v["UID"],
        "rocketchat_channel": get_paper_rocketchat(v["UID"]),
        "content": {
            "title": v["title"],
            "authors": list_fields["authors"],
            "keywords": list_fields["keywords"],
            "abstract": v["abstract"],
            "TLDR": v["abstract"][:250] + "...",
            "pdf_url": v.get("pdf_url", ""),
            "demo_url": by_uid["demos"].get(v["UID"], {}).get("demo_url", ""),
            "track": v.get("track", ""),
            "sessions": v["sessions"],
            "recs": [],
        },
    }


def format_tutorial(v):
    list_keys = ["organizers"]
    list_fields = {}
    for key in list_keys:
        list_fields[key] = extract_list_field(v, key)

    return {
        "id": v["UID"],
        "title": v["title"],
        "organizers": list_fields["organizers"],
        "abstract": v["abstract"],
        "material": v["material"],
    }


def format_workshop(v):
    list_keys = ["organizers"]
    list_fields = {}
    for key in list_keys:
        list_fields[key] = extract_list_field(v, key)

    return {
        "id": v["UID"],
        "title": v["title"],
        "organizers": list_fields["organizers"],
        "abstract": v["abstract"],
        "material": v["material"],
    }


def extract_list_field(v, key):
    value = v.get(key, "")
    if isinstance(value, list):
        return value
    else:
        return value.split("|")


def merge_committees(site_data: Dict[str, Any]) -> List[Dict[str, Any]]:
    index = 0
    tmp_data = {}
    committees = site_data["committee"]["committee"]
    merged_committees = []
    for committee in committees:
        name = committee["name"]
        if name in tmp_data:
            ### duplicated found ###
            c_index = tmp_data[name]["index"]
            role = merged_committees[c_index]["role"] + " & " + committee["role"]
            merged_committees[c_index]["role"] = role
            print("duplicated committee: %s" % name)
        else:
            tmp_data[name] = committee
            tmp_data[name]["index"] = index
            merged_committees.append(committee)
            index = index + 1

    return merged_committees
