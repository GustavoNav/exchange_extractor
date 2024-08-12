from data_extractor.real_time_extractor.src.main import main_pipeline

def run_real_time_pipeline(company_code):
    main_pipeline.run_pipeline(company_code)


run_real_time_pipeline('PETR3.SA')