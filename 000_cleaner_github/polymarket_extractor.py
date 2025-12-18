import requests
import json

def extract_polymarket_positions():
    """
    Connect to Polymarket API and extract asset lists as JSON files based on currentValue > 0
    """

    # API URL
    
    url = "https://data-api.polymarket.com/positions?user=YOUR_ADDRESS&limit=500&offset=0" #C40


    try:
        # Make the API request
        print("Connecting to Polymarket API...")
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse JSON data
        data = response.json()
        print(f"Retrieved {len(data)} positions")

        # Filter positions where currentValue > 0
        filtered_positions = [pos for pos in data if pos.get('currentValue', 0) > 0]
        print(f"Found {len(filtered_positions)} positions with currentValue > 0")

        if not filtered_positions:
            print("No positions found with currentValue > 0")
            # Create empty JSON files
            with open('ASSETLIST.json', 'w') as f:
                json.dump([], f, indent=2)
            with open('assetandsize.json', 'w') as f:
                json.dump({}, f, indent=2)
            return

        # Extract assets list
        assets = [pos['asset'] for pos in filtered_positions]

        # Create ASSETLIST.json
        with open('ASSETLIST.json', 'w') as f:
            json.dump(assets, f, indent=2)
        print(f"Created ASSETLIST.json with {len(assets)} assets")

        # Create asset:size dictionary
        asset_size_dict = {pos['asset']: pos['size'] for pos in filtered_positions}

        # Create assetandsize.json
        with open('assetandsize.json', 'w') as f:
            json.dump(asset_size_dict, f, indent=2)
        print(f"Created assetandsize.json with {len(asset_size_dict)} asset:size pairs")

        # Print summary
        print("\nSummary:")
        print(f"Total positions retrieved: {len(data)}")
        print(f"Positions with currentValue > 0: {len(filtered_positions)}")

        if filtered_positions:
            print("\nPositions with currentValue > 0:")
            for pos in filtered_positions:
                print(f"  Asset: {pos['asset']}")
                print(f"  Size: {pos['size']}")
                print(f"  Current Value: {pos['currentValue']}")
                print(f"  Title: {pos.get('title', 'N/A')}")
                print("  ---")

    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    extract_polymarket_positions()
