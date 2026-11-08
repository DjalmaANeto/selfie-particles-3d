import json
import subprocess
import os

os.environ["GH_CONFIG_DIR"] = os.path.expanduser("~/.config/gh-multfacil")

query = """
{
  user(login: "Djalma0multfacil") {
    projectV2(number: 1) {
      items(first: 50) {
        nodes {
          id
          content {
            ... on Issue {
              number
            }
          }
        }
      }
    }
  }
}
"""

res = subprocess.run(["gh", "api", "graphql", "-f", f"query={query}"], capture_output=True, text=True)
data = json.loads(res.stdout)
nodes = data["data"]["user"]["projectV2"]["items"]["nodes"]

start_date_field = "PVTF_lAHOB0onz84Bpu0PzhoQ4Ro"
target_date_field = "PVTF_lAHOB0onz84Bpu0PzhoQ4Rs"
project_id = "PVT_kwHOB0onz84Bpu0P"

prod_issues = {2438, 2439, 2440, 2441}
dev_issues = {2429, 2431, 2432, 2433, 2434, 2435, 2442, 2443, 2444, 2445}

for node in nodes:
    item_id = node["id"]
    content = node.get("content")
    if not content:
        continue
    num = content.get("number")
    
    if num in prod_issues:
        s_date = "2026-10-20"
        t_date = "2026-10-28"
        status = "Em produção"
    elif num in dev_issues:
        s_date = "2026-10-25"
        t_date = "2026-11-10"
        status = "Desenvolvimento"
    else:
        s_date = "2026-11-01"
        t_date = "2026-11-25"
        status = "Em esteira"

    mut = f"""
    mutation {{
      d1: updateProjectV2ItemFieldValue(input: {{ projectId: "{project_id}", itemId: "{item_id}", fieldId: "{start_date_field}", value: {{ date: "{s_date}" }} }}) {{ projectV2Item {{ id }} }}
      d2: updateProjectV2ItemFieldValue(input: {{ projectId: "{project_id}", itemId: "{item_id}", fieldId: "{target_date_field}", value: {{ date: "{t_date}" }} }}) {{ projectV2Item {{ id }} }}
    }}
    """
    sub_res = subprocess.run(["gh", "api", "graphql", "-f", f"query={mut}"], capture_output=True, text=True)
    print(f"Issue #{num} (Status: {status}) -> {s_date} to {t_date}: code {sub_res.returncode}")
