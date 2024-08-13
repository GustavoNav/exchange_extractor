import argparse
from general_information_extractor.src.main import main_pipeline

def run_general_pipeline(url, company_code):
    main_pipeline.run_pipeline(url, company_code)

def main():
    parser = argparse.ArgumentParser(description="Execute the pipeline with 2 args")
    parser.add_argument('url', type=str)
    parser.add_argument('company_code', type=str)

    args = parser.parse_args()

    run_general_pipeline(args.url, args.company_code)

if __name__ == "__main__":
    main()