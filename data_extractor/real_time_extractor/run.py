import argparse
from real_time_extractor.src.main import main_pipeline

'''run real time pipeline function'''
def run_real_time_pipeline(company_code):
    main_pipeline.run_pipeline(company_code)

'''start running. Receive 1 arg - company code'''
def main():
    parser = argparse.ArgumentParser(description="Execute the pipeline with 1 arg")
    parser.add_argument('company_code', type=str)

    args = parser.parse_args()

    run_real_time_pipeline(args.company_code)

if __name__ == "__main__":
    main()