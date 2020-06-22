import csv
import glob
import json
from collections import OrderedDict
from datetime import datetime, timedelta
from typing import Dict, Any, List

import pytz
import yaml

from miniconf.utils import merge_committees


def load_site_data(
    site_data_path: str,
    site_data: Dict[str, Any],
    by_uid: Dict[str, Any],
    qa_session_length_hr: int,
) -> List[str]:
    """Loads all site data at once.

    Populates the `site_data` and `by_uid` using files under `site_data_path`.
    """
    extra_files = ["README.md"]
    # Load all for your sitedata one time.
    for f in glob.glob(site_data_path + "/*"):
        extra_files.append(f)
        name, typ = f.split("/")[-1].split(".")

        if name == "acl2020_accepted_papers":
            continue

        if typ == "json":
            site_data[name] = json.load(open(f))
        elif typ in {"csv", "tsv"}:
            site_data[name] = list(csv.DictReader(open(f)))
        elif typ == "yml":
            site_data[name] = yaml.load(open(f).read(), Loader=yaml.SafeLoader)

    for typ in ["papers", "speakers", "tutorials", "workshops", "demos"]:
        by_uid[typ] = {}
        for p in site_data[typ]:
            by_uid[typ][p["UID"]] = p

    display_time_format = "%H:%M"
    for session_name, session_info in site_data["poster_schedule"].items():
        for paper in session_info["posters"]:
            if "sessions" not in by_uid["papers"][paper["id"]]:
                by_uid["papers"][paper["id"]]["sessions"] = []
            time = datetime.strptime(session_info["date"], "%Y-%m-%d_%H:%M:%S")
            start_time = time.strftime(display_time_format)
            start_day = time.strftime("%a")
            end_time = time + timedelta(hours=qa_session_length_hr)
            end_time = end_time.strftime(display_time_format)
            time_string = "({}-{} GMT)".format(start_time, end_time)
            current_num_sessions = len(by_uid["papers"][paper["id"]]["sessions"])
            calendar_stub = site_data["config"]["site_url"].replace("https", "webcal")
            by_uid["papers"][paper["id"]]["sessions"].append(
                {
                    "time": time,
                    "time_string": time_string,
                    "session": " ".join([start_day, "Session", session_name]),
                    "zoom_link": paper["join_link"],
                    "ical_link": calendar_stub
                    + "/poster_{}.{}.ics".format(paper["id"], current_num_sessions),
                }
            )

    # TODO: should assign UID by sponsor name? What about sponsors with multiple levels?
    by_uid["sponsors"] = {
        sponsor["UID"]: sponsor
        for sponsors_at_level in site_data["sponsors"]
        for sponsor in sponsors_at_level["sponsors"]
    }

    # Format the session start and end times
    for sponsor in by_uid["sponsors"].values():
        sponsor["zoom_times"] = OrderedDict()
        for zoom in sponsor.get("zooms", []):
            start = zoom["start"].astimezone(pytz.timezone("GMT"))
            end = start + timedelta(hours=zoom["duration"])
            day = start.strftime("%A")
            start_time = start.strftime(display_time_format)
            end_time = end.strftime(display_time_format)
            time_string = "{} ({}-{} GMT)".format(day, start_time, end_time)

            if day not in sponsor["zoom_times"]:
                sponsor["zoom_times"][day] = []

            sponsor["zoom_times"][day].append((time_string, zoom["label"]))

    site_data["committee"] = merge_committees(site_data)

    print("Data Successfully Loaded")
    return extra_files
