import re

def fix_logs():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the logs list response and replace keys
    # Example snippet: "action": "XXXX", "targetId": "YYYY", "details": "ZZZZ"
    # We will just do regex substitute
    html = re.sub(r'"action"\s*:\s*([^,]+),', r'"action_type": \1,\n                        "target_entity": "Unknown",', html)
    html = re.sub(r'"targetId"\s*:\s*([^,]+),', r'"target_id": \1,\n                        "before_value": null,\n                        "after_value": null,', html)
    
    # Also fix User schema response if needed
    html = html.replace('"id": "user_001"', '"user_id": "user_001"')
    html = html.replace('"id": "user_002"', '"user_id": "user_002"')
    
    # Store schema response
    html = html.replace('"localAreaId":', '"area_id":')

    with open('api.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed logs and misc")

fix_logs()
