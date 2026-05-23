#!/usr/bin/env python
"""
VTRecon is a Python tool that uses VirusTotal API for scanning
files, hashes, and URLs from your terminal
"""
import os
import asyncio
import vt

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
    API_LOAD = os.environ.get('API_KEY')
    # Using "async with" for the VT Client for unclosed connection
    async with vt.Client(str(API_LOAD)) as CLIENT:
        while True:
            # Get user input for VirusTotal
            VT_HAS = input(str("\nURL/HASH: "))
            try:
                if "https" in VT_HAS:
                    URL_ID = vt.url_id(VT_HAS)
                    URL = await CLIENT.get_object_async("/urls/{}", URL_ID)
                    print(f"\nResults for {VT_HAS}")
                    OBJECTS = URL.last_analysis_stats
                    for key, value in OBJECTS.items():
                        print(f"\n{key.title()}: {value}")
                else:
                    # Await async call
                    FILE_OBJ = await CLIENT.get_object_async(f"/files/{VT_HAS}")
                    print(f"\nResults for {VT_HAS}:")
                    OBJECTS = FILE_OBJ.last_analysis_stats
                    for key, value in OBJECTS.items():
                        print(f"\n{key.title()} : {value}")
                    
            except vt.error.APIError as e:
                # Display error message for VT
                print("An error has occurred: {e}")
            # Rescan checker
            confirm_scan = input("\nScan Again [Y/n]: ").title()
            if confirm_scan == 'Y':
                continue
            else:
                print("\nThank you for using VTRecon")
                break


if __name__ == "__main__":
    # Execute async function
    asyncio.run(API())
