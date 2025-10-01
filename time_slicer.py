#!/usr/bin/env python3
import pandas as pd
import argparse
from pathlib import Path
import sys

def slice_data(input_file, output_file, start, end):
    try:
        # Load data
        df = pd.read_csv(input_file)
        
        # Convert timestamps (handles multiple formats)
        df['timestamp'] = pd.to_datetime(
            df['timestamp'],
            dayfirst=False,  # Set True if dates are DD/MM/YYYY
            yearfirst=True  # Prioritize YYYY-MM-DD format
        )
        
        print(f"\nData covers: {df['timestamp'].min()} to {df['timestamp'].max()}")
        
        # Convert input times
        start = pd.to_datetime(start)
        end = pd.to_datetime(end)
        
        # Validate requested range
        if start < df['timestamp'].min() or end > df['timestamp'].max():
            raise ValueError(
                f"Requested range ({start} to {end}) "
                f"is outside data range!"
            )
        
        # Slice and save
        sliced = df[(df['timestamp'] >= start) & (df['timestamp'] <= end)]
        sliced.to_csv(output_file, index=False)
        
        print(f"Saved {len(sliced)} rows to {output_file}")
        print(f"Sliced range: {sliced['timestamp'].min()} to {sliced['timestamp'].max()}")

    except Exception as e:
        print(f"\nERROR: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    args = parser.parse_args()
    slice_data(args.input, args.output, args.start, args.end)