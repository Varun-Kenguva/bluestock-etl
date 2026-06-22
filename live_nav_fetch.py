import pandas as pd
import requests
from pathlib import Path
raw_path = Path("data/raw")
raw_path.mkdir(parents=True, exist_ok=True)

schemes = {
    "125497": "hdfc_top_100_direct",
    "119551": "sbi_bluechip",
    "120503": "icici_bluechip",
    "118632": "nippon_large_cap",
    "119092": "axis_bluechip",
    "120841": "kotak_bluechip"
}
for amfi_code, scheme_name in schemes.items():
    url = f"https://api.mfapi.in/mf/{amfi_code}"
    print(f"\nFetching {scheme_name} ({amfi_code})")

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = raw_path / f"{scheme_name}_nav.csv"
        nav_df.to_csv(file_name, index=False)

        print(f"Saved: {file_name}")
        print(f"Records: {len(nav_df)}")

    else:
        print(f"Failed for {amfi_code}")