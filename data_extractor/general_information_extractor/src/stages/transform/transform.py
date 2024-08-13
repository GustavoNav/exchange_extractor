from general_information_extractor.src.errors.transform_error import TransformError
import re

class TransformInformation:
    '''Transform the essential information, getting the required data'''
    def transform(self, essential_data):
        
        essential_information = essential_data['essential_information']
        try:
            transformed_data = {
                'company_code': essential_data['company_code'],
                'sector': self.__find_sector(essential_information),
                'net_sales': self.__find_net_sales(essential_information),   
                'net_income': self.__find_net_income(essential_information),
                'net_margin': self.__find_net_margin(essential_information),
                'ebitda': self.__find_ebitda(essential_information),
                'ebitda_margin': self.__find_ebitda_margin(essential_information),
                'total_assets': self.__find_total_assets(essential_information),
                'gross_debt': self.__find_gross_debt(essential_information),
                'equity': self.__find_equity(essential_information),
                'pe_ratio': self.__find_pe_ratio(essential_information)
            }

            return transformed_data
        
        except Exception as exception:
            raise TransformError(str(exception))
    
    def __find_sector(self, essential_information):
        match = None
        if not match:
            pattern = r'Setor: <strong>(.{1,30}?)</strong>'
            match = re.search(pattern, essential_information)

        if match:
            sector = match.group(1)
            return sector
        return match

    def __find_net_sales(self, essential_information):
        match = None
        if not match:
            pattern = r'Receita Líquida</a></td>\n<td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)

        if match:
            raw_net_sales = match.group(1)
            net_sales = self.__convert_to_numeric(raw_net_sales)

            return net_sales
        return match

    def __find_net_income(self, essential_information):
        match = None
        if not match:
            pattern = r'Lucro Líquido \(LL\)</a></td>\n<td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_net_income = match.group(1)
            net_income = self.__convert_to_numeric(raw_net_income)
            return net_income
        return match
    
    def __find_net_margin(self, essential_information):
        match = None
        if not match:
            pattern = r'Margem Líquida</a></td>\n<td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_net_margin = match.group(1)
            net_margin = float(raw_net_margin.replace('%',''))
            return net_margin
        return match
        
    def __find_ebitda(self, essential_information):
        match = None
        if not match:
            pattern = r'Ebitda</a></td>\n<td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)

        if match:
            raw_ebitda = match.group(1)
            ebitda = self.__convert_to_numeric(raw_ebitda)
            return ebitda
        return match
    
    def __find_ebitda_margin(self, essential_information):
        match = None
        if not match:
            pattern = r'Margem Ebitda</a></td>\n<td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_ebtida_margin = match.group(1)
            ebtida_margin = raw_ebtida_margin.replace('%','')
            return ebtida_margin
        return match
    
    def __find_total_assets(self, essential_information):
        match = None
        if not match:
            pattern = r'Ativo Total</a></td>\n<td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_total_assets = match.group(1)
            total_assets = self.__convert_to_numeric(raw_total_assets)
            return total_assets
        return match
    
    def __find_gross_debt(self, essential_information):
        match = None
        if not match:
            pattern = r'Dívida Bruta</a></td><td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_gross_debt = match.group(1)
            gross_debt = self.__convert_to_numeric(raw_gross_debt)
            return gross_debt
        return match
    
    def __find_equity(self, essential_information):
        match = None
        if not match:
            pattern = r'Patrimônio Líquido \(PL\)</a></td><td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_equity = match.group(1)
            equity = self.__convert_to_numeric(raw_equity)
            return equity
        return match

    def __find_pe_ratio(self, essential_information):
        match = None
        if not match:
            pattern = r'Índice de preço sobre lucro \(P/L\)</a></td><td> (.{1,30}?)</td>'
            match = re.search(pattern, essential_information)
        
        if match:
            raw_pe_ratio = match.group(1)
            pe_ratio = self.__convert_to_numeric(raw_pe_ratio)
            return pe_ratio
        return match


    def __convert_to_numeric(self, valor):
        valor = valor.replace("R$", "").strip()

        convert = 1
        if "B" in valor:
            convert = 1e9
        elif "M" in valor:
            convert = 1e6

        valor = valor[:-2]
        valor_numerico = float(valor.replace(",", "."))

        valor_numerico = valor_numerico * convert

        return valor_numerico
