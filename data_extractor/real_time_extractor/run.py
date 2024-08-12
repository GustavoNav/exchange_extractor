import argparse
from data_extractor.real_time_extractor.src.main import main_pipeline

def run_real_time_pipeline(company_code):
    main_pipeline.run_pipeline(company_code)


def main():
    parser = argparse.ArgumentParser(description="Execute the pipeline with 1 arg")
    parser.add_argument('company_code', type=str)

    args = parser.parse_args()

    run_real_time_pipeline(args.company_code)

if __name__ == "__main__":
    main()