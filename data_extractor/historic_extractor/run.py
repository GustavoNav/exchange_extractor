from data_extractor.historic_extractor.src.main import main_pipeline

def run_historic_extractor_pipeline(CompanyCode):
    main_pipeline.run_pipeline(CompanyCode)

main_pipeline.run_pipeline("PETR3.SA")