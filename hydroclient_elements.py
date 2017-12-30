from site_element import SiteElement

class SearchPage:
    def __init__(self):
        self.search_now = SiteElement('button', el_id='btnSearchNow')
        self.filter_results = SiteElement('button', el_id='btnSearchSummary')
        self.location_search = SiteElement('input', el_id='pac-input')
        self.service_filter = SiteElement('button', el_id='btnSelectDataServices', el_content='Data Service(s)...')
        self.results_found = SiteElement('span', el_id='timeseriesFoundOrFilteredCount')
        self.date_filter = SiteElement('*', el_id='optionsDatesRange')
        self.date_start = SiteElement('*', el_id='startDateModal')
        self.date_end = SiteElement('*', el_id='endDateModal')
        self.date_clickout = SiteElement('h3', el_content='Please select your date range:')
        self.date_save = SiteElement('*', el_id='btnDateRangeModalSave')

class ServiceSearch:
    def __init__(self):
        self.sort_organization = SiteElement('th', el_content='Organization')
        self.save = SiteElement('button', el_id='btnServicesModalSave')
        self.search = SiteElement('button', el_id='btnServicesModalSearch')
        self.table_count = SiteElement('select', el_name='tblDataServices_length')
        self.archbold = SiteElement('td', el_content='Archbold Biological Station')
        self.nwis_uv = SiteElement('a', el_content='NWIS Unit Values', recursive_loc=[SiteElement(el_dom='./../..'), SiteElement(el_dom='./td[1]')])
        self.nasa_noah = SiteElement('a', el_content='NLDAS Hourly NOAH Data', recursive_loc=[SiteElement(el_dom='./../..'), SiteElement(el_dom='./td[1]')])
        self.nasa_forcing = SiteElement('a', el_content='NLDAS Hourly Primary Forcing Data', recursive_loc=[SiteElement(el_dom='./../..'), SiteElement(el_dom='./td[1]')])

class FilterResults:
    def __init__(self):
        self.choose_action = SiteElement('div', el_id='ddActionsDSR')
        self.table_count = SiteElement('select', el_name='tblDetailedSearchResults_length')
        self.export_workspace = SiteElement('a', el_id='anchorAddSelectionsToWorkspaceDSR')
        self.nav_exports = SiteElement('button', el_id='tableModal-DownloadMgrSearchSummary')
        self.nav_workspace = SiteElement('button', el_id='tableModal-DataMgrSearchSummary')
        self.nav_close = SiteElement('button', el_id='closeSearchSummary')
        self.search = SiteElement('div', el_id='tblDetailedSearchResults_filter', recursive_loc=[SiteElement(el_dom='./label'), SiteElement(el_dom='./input')])
        self.select_any = SiteElement('table', el_id='tblDetailedSearchResults', recursive_loc=[SiteElement(el_dom='./tbody'), SiteElement(el_dom='./tr'), SiteElement(el_dom='./td'), SiteElement(el_dom='./div')])
        self.select_derived_value = SiteElement('td', el_content='Derived Value')
        self.select_model_sim = SiteElement('td', el_content='Model Simulation Result')
        self.sort_service = SiteElement('div', el_id='tblDetailedSearchResults_wrapper', recursive_loc=[SiteElement('th', el_content='Service Title')])

SearchPage = SearchPage()
ServiceSearch = ServiceSearch()
FilterResults = FilterResults()

