import argparse
from historic_extractor.src.main import main_pipeline

def run_historic_extractor_pipeline(CompanyCode):
    main_pipeline.run_pipeline(CompanyCode)

def main():
    parser = argparse.ArgumentParser(description="Execute the pipeline with 1 arg")
    parser.add_argument('company_code', type=str)

    args = parser.parse_args()

    run_historic_extractor_pipeline(args.company_code)

if __name__ == "__main__":
    main()