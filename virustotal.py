import vt 
import os 
import asyncio


# Filename to become created
FILENAME = 'VirusTotalAPI.txt'
# Full Path to file
FILE_PATH = os.getcwd()

def API_FILE():
    """Creates the API key file correctly using strings."""
    try:
        # Get API Key and write to a file
        API_INP = input("API: ").strip()
        with open(FILENAME, 'w') as api_object:
            # Write to file
            api_object.write(API_INP)
        return FILENAME
    except Exception as e:
        print(f"An error occurred while creating the API file: {e}")
        return None


# ASYNC API Function
async def API(file_to_read):
    """Main code for VirusTotal."""
    try:
        with open(file_to_read, 'r') as api_key_file:
            get_api = api_key_file.read().strip()
    except Exception as e:
        print(f"Error reading API file: {e}")
        return
    
    if not get_api:
        print("API key is empty. Please ensure you have entered a valid API key.")
        return

    # Using "async with" for the VT Client for unclosed connection
    async with vt.Client(get_api) as CLIENT:
        # Get user input for VirusTotal
        VT_HAS = input(str("Enter a hash value: "))
        try:
            # Await async call
            FILE_OBJ = await CLIENT.get_object_async(f"/files/{VT_HAS}")
            print(f"\nResults for {VT_HAS}:")
            print(FILE_OBJ.last_analysis_stats)
            
        except vt.error.APIError as e:
            # Display error message for VT
            print("An error has occurred: {e}")

def main():
    # Ensure FILE_CREATE is NEVER None
    if not os.path.exists(FILENAME):
        FILE_CREATE = API_FILE()
    else:
        FILE_CREATE = FILENAME
    
    # Only run if we actually have a valid filename string 
    if FILE_CREATE:
        try:
            asyncio.run(API(FILE_CREATE))
        except KeyboardInterrupt:
            print("\nExiting...")
    else:
        print("Failed to initialize API file. Exiting.")
        

if __name__ == "__main__":
    main()
