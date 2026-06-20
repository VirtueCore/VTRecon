#!/usr/bin/env python
"""
VTRecon is a Python tool that uses VirusTotal API for scanning
files, hashes, and URLs from your terminal
"""
import os
import asyncio
import vt
import tkinter as tk
from tkinter import filedialog

# ASCII Art
ART = r"""
██╗   ██╗████████╗██████╗ ███████╗ ██████╗ ██████╗ ███╗   ██╗
██║   ██║╚══██╔══╝██╔══██╗██╔════╝██╔════╝██╔═══██╗████╗  ██║
██║   ██║   ██║   ██████╔╝█████╗  ██║     ██║   ██║██╔██╗ ██║
╚██╗ ██╔╝   ██║   ██╔══██╗██╔══╝  ██║     ██║   ██║██║╚██╗██║
 ╚████╔╝    ██║   ██║  ██║███████╗╚██████╗╚██████╔╝██║ ╚████║
  ╚═══╝     ╚═╝   ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝                                                 
"""
print(ART)

# ASYNC API Function
async def API():
    """Main code for VirusTotal."""
    # API Key from user environment
    API_LOAD = os.getenv('API_KEY')
    
    if API_LOAD is None:
        raise ValueError("API_KEY environment variable not found. ❌")
    API_LOAD = API_LOAD.strip()
    
    # Using "async with" for the VT Client for unclosed connection
    async with vt.Client(API_LOAD) as CLIENT:
        while True:
            # Get user input for VirusTotal
            VT_Choice = input(str("\nURL/HASH/FILE ➜] ")).upper()
            try:
                if "URL" in VT_Choice:
                    VT_URL = input("Enter URL ➜] ")
                    if "http" in VT_URL or "https" in VT_URL:
                        URL_ID = vt.url_id(VT_URL)
                        URL = await CLIENT.get_object_async("/urls/{}", URL_ID)
                        print(f"\nResults for {VT_URL} 📜")
                        OBJECTS = URL.last_analysis_stats
                        for key, value in OBJECTS.items():
                            print(f"\n{key.title()}: {value}")

                elif "FILE" in VT_Choice:
                    # Hide the main Tkinter window
                    root = tk.Tk()
                    root.withdraw()
                    
                    # Open the file picker
                    file_path = filedialog.askopenfilename(
                        title="Select a file",
                        filetypes=[
                            ("Text Files", "*.txt"),
                            ("CSV Files", "*.csv"),
                            ("Python Files", "*.py"),
                            ("PDF Files", "*.pdf"),
                            ("All Files", "*.*")
                        ]
                    )
                    
                    # Kill tkinter after file selection
                    root.destroy()
                    
                    # Check if the user selected a file
                    if file_path:
                        print(f"Selected file: {file_path} 💡")
                        
                        # Read file binary
                        with open(file_path, "rb") as file:
                            analysis = await CLIENT.scan_file_async(file, wait_for_completion=True)
                            results = await CLIENT.get_object_async("/analyses/{}", analysis.id)
                        print(results.status)
                    else:
                        print("No file selected. 😔")

                elif "HASH" in VT_Choice:
                    HAH = input("Enter Hash Value ➜] ")
                    hash_read = await CLIENT.get_object_async(f"/files/{HAH}")
                    print(f"\nResults for {VT_Choice} 📜")
                    OBJECTS = hash_read.last_analysis_stats
                    for key, value in OBJECTS.items():
                        print(f"\n{key.title()}: {value}")
      
                else:
                    print("Sad to see you go! 🫡")
                    
            except vt.error.APIError as e:
                # Display error message for VT
                print(f"An error has occurred: {e} 🪲")
            # Rescan checker
            confirm_scan = input("\nScan Again [Y/n] 🔄 ").title()
            if confirm_scan == 'Y':
                continue
            else:
                print("\nThank you for using VTRecon 🙇‍♂️")
                break


if __name__ == "__main__":
    # Execute async function
    asyncio.run(API())
