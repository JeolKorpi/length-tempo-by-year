import os

def inflate_file(original_file_path, target_size_gb):
    # Convert GB to bytes (1GB = 1024^3 bytes)
    target_size_bytes = target_size_gb * 1024**3
    
    # Get the size of the original file
    original_size_bytes = os.path.getsize(original_file_path)
    
    # Calculate how many times the original file needs to be duplicated
    duplication_factor = target_size_bytes // original_size_bytes + 1
    
    # Set the path for the inflated file
    inflated_file_path = f"{original_file_path.split('.')[0]}_{target_size_gb}GB.csv"
    
    # Read the original file content
    with open(original_file_path, 'r') as original_file:
        original_content = original_file.read()
        
    # Write the duplicated content to a new file until the target size is reached
    with open(inflated_file_path, 'w') as inflated_file:
        for _ in range(duplication_factor):
            inflated_file.write(original_content)
            # Check if the file has reached or exceeded the target size
            if os.path.getsize(inflated_file_path) >= target_size_bytes:
                break

    print(f"Inflated file created at: {inflated_file_path} with size: {os.path.getsize(inflated_file_path) / (1024**3):.2f} GB")

# # Example usage: Inflate the file to 1GB
# original_file_path = '/mnt/data/MillionSongSubset_aggregated.csv'
# inflate_file(original_file_path, 1)

def main():
    # Example usage: Inflate the file to 1GB
    original_file_path = '/Users/antonnaslund/Documents/skola/dataengineering/MillionSongSubset_aggregated.csv'
    target_size_gb = 4  # Modify this as needed
    inflate_file(original_file_path, target_size_gb)

if __name__ == "__main__":
    main()